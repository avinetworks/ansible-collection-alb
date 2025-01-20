############################################################################
# ========================================================================
# Copyright 2024 VMware, Inc. All rights reserved. VMware Confidential
# ========================================================================
###

"""
What is the service functionality?
> To accept a command as string on Unix Domain Socket and respond with out, err and return code

How is the service started?
> The service is started by Cloud Connector before SE container comes up in LSC.

How is the service stopped?
> Stopping avise service automatically stop avihost service in its post stop section

Where does it run?
> The service runs on the host of SE in LSC mode. NOTE: The service is applicable only for container based deployments

What happens when exceptions are hit?
> The service is run with auto-restart by systemd and it is stateless.

What is the location of its log-files on the host.
> Logs are stored at `/var/log/avi_host.log` of the host with logrotation enabled

Are there any service dependencies with respect to SE container?
> It needs python2 / python3 to be installed in the host

If the SE container is stopped, will avihost service get stopped?
> Yes, it is done as a part of poststop section of avise

Can the service run when the container is not running?
> We will stop the service upon SE service termination.
The service running post SE stopped causes no harm, though.

Any upgrade implications? when a SE container is upgraded from x to x+1, will the host service also get upgraded from x to x+1 ?
> The avihost is written and maintained in such a fashion that it is lightweight and can support different versions of AVI SE.
Having said that, we upgrade avihost and related items, whenever SE is getting upgraded.
"""

import socket
import sys
import os
import subprocess
import signal
import logging
import traceback
import re
from logging.handlers import RotatingFileHandler

log_file="/var/log/avi_host.log"
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
#20MB file limit for logging
handler = RotatingFileHandler(log_file, maxBytes=20*1024*1024, backupCount=1)
formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

SERVER_ADDRESS = '/root/se_domain_socket'
CURRENT_VERSION = "v1"

def send_response(conn, version, returncode, output, error):
    # Send the response back to the client

    output, error = output.strip(), error.strip()

    if version == CURRENT_VERSION:
        conn.sendall("#version:{}#ret:{}#aviout:".format(CURRENT_VERSION, returncode).encode("utf-8"))
        conn.sendall(output)
        conn.sendall("#avierror:".encode("utf-8"))
        conn.sendall(error)
        conn.sendall("#avidone#".encode("utf-8"))
        logger.debug("Sent response for {}".format(CURRENT_VERSION))
        return

    # Legacy handling of o/p and error differently
    if returncode:
        logger.error("command execution failed {} {}".format(error, returncode))
        conn.sendall(error)
        conn.sendall("#ret:{}#avierror#".format(returncode).encode("utf-8"))
    else:
        logger.debug("command output {}".format(output))
        conn.sendall(output)
        conn.sendall("#avidone#".encode("utf-8"))
    logger.debug("Sent response for Legacy version")

def block_and_recv(conn):
    # Receive the data in small chunks and retransmit it
    input_str = ""
    while True:
        data = conn.recv(64)
        input_str = input_str + data.decode("utf-8")
        logger.debug("input_str={}".format(input_str))
        if "#avicmddone#" in input_str:
            split_list = re.split("#version:|#cmd:|#avicmddone#", input_str)
            if len(split_list) == 2:
                # Legacy format: "<command>#avicmddone#"
                # split_list = ["<command>", ""]
                return [split_list[1], split_list[0]]
            else:
                # v1 format: "#version:{version_tag}#cmd:{command}#avicmddone#"
                # split_list = ["", "<command>", "<version_tag>", ""]
                return split_list[1:-1]

def create_uds_socket():
    # Make sure the socket does not already exist
    try:
        os.unlink(SERVER_ADDRESS)
    except OSError as error:
        if os.path.exists(SERVER_ADDRESS):
            exception = traceback.format_exc()
            logger.error("Failed to unlink domain stream socket: {}".format(exception))
            raise Exception("Failed to unlink domain stream socket: {}".format(exception))

    # Create a UDS socket
    try:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(SERVER_ADDRESS)
        # Listen for incoming connections
        sock.listen(1)
        logger.info("Listening on %s", SERVER_ADDRESS)
        return sock
    except:
        exception = traceback.format_exc()
        logger.error("socket listen failed: {}".format(exception))
        raise Exception("socket listen failed: {}".format(exception))

def run():
    sock = create_uds_socket()
    while True:
        # Valid Formats:
        # Legacy: (20.1.4 - <21.1.1)
        #    Input  : {command}#avicmddone#
        #    Output :
        #        * If error : {error}#ret:{return_code}#avierror#
        #        * Else     : {output}#avidone#
        #
        # v1: (21.1.1 and above)
        #    Input  : #version:{version_tag}#{command}#avicmddone#
        #    Output : #version:{version_tag}#ret:{return_code}#aviout:{output}#avierror:{error}#avidone#

        # Wait for a connection
        logger.debug('waiting for a connection')
        conn, client_address = sock.accept()
        version = CURRENT_VERSION
        try:
            version, command = block_and_recv(conn)
            version, command = version.strip(), command.strip()

            # Empty command, send error response
            if not command:
                send_response(conn, version, 255, b"", b"Received empty command")
                continue

            # AVI induced crash (A way to restart the service)
            if command == "#avicrash#":
                raise Exception("AVI induced crash")

            # If process needs to be run in background
            if command.endswith("&"):
                returncode = os.system(command)
                send_response(conn, version, returncode, b"", b"")
                continue

            # Execute command with timeout of 120 seconds and send response for other commands
            logger.debug("received command {}".format(command))
            command = "timeout 120 " + command
            op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output, error = op.communicate()
            returncode = op.returncode
            send_response(conn, version, returncode, output, error)

        # If exception is hit, log the exception, send it to the client,
        # raise another exception and let the process crash
        except Exception as ex:
            exception = traceback.format_exc()
            logger.error("Exception hit: {}".format(exception))
            send_response(conn, version, 255, b"", exception.encode("utf-8"))
            raise Exception("Exception hit: {}".format(exception))

        # Clean up the connection
        finally:
            conn.close()

if __name__ == "__main__":
    run()
