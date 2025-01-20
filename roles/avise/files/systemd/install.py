#!/usr/bin/python3
############################################################################
# ========================================================================
# Copyright 2024 VMware, Inc. All rights reserved. VMware Confidential
# ========================================================================
###

"""
===================================
Avihost service migration Tool
===================================

"""

import traceback
import os
import logging
import sys
import time
import subprocess
import shlex

from avi.infrastructure.avi_logging import get_root_logger

log = logging.getLogger(__name__)

def print_info(msg):
    """
    Wrapper function to prints the msg into stdout and log-file.
    """
    msg = 'SEUC:: [' + time.ctime() + ']' + str(msg) + '::SEUC'
    print(msg)
    log.info(msg)

def print_error(msg):
    """
    Wrapper function to prints the msg into stderr and log-file.
    """
    msg = 'SEUC:: [' + time.ctime() + ']' + str(msg) + '::SEUC'
    print(msg)
    log.error(msg)

def copy_avihost_service_to_hostroot():
    """
    SCP and Copy the latest avi_host service files from controller to /hostroot
    """
    print_info("Copying new avihost service from controller to /hostroot")
    try:
        parent_folder = os.path.dirname(os.path.realpath(__file__))
        host_files = {
                        'avihost.service' : '/hostroot/etc/systemd/system/',
                        'avihost_service_script.sh' : '/hostroot/etc/systemd/system/', 
                        'avi_host_server.py' : '/hostroot/usr/sbin/' 
        }
        replace_host_files = False
        for host_file, local_folder in host_files.items():

            remote_host_file = os.path.join(parent_folder,host_file)
            local_host_file = os.path.join(local_folder, host_file)
            if os.path.exists(remote_host_file):
                print_info("Copied latest: %s" % remote_host_file)
                cmd = 'sha512sum %s' %(remote_host_file)
                latest_avi_host_md5 = subprocess.check_output(shlex.split(cmd))
                if not isinstance(latest_avi_host_md5, str):
                    latest_avi_host_md5 = latest_avi_host_md5.decode(sys.stdout.encoding)
                latest_avi_host_md5 = latest_avi_host_md5.split(' ')[0]
                cmd = 'sha512sum %s' %(local_host_file)
                current_avi_host_md5 = None
                try:
                    current_avi_host_md5 = subprocess.check_output(shlex.split(cmd))
                    if not isinstance(current_avi_host_md5, str):
                        current_avi_host_md5 = current_avi_host_md5.decode(sys.stdout.encoding)
                    current_avi_host_md5 = current_avi_host_md5.split(' ')[0]
                except Exception as e:
                    pass
                print_info("Receive avihost checksum from controller: %s and current is: %s" % (latest_avi_host_md5, current_avi_host_md5))
                if latest_avi_host_md5 and current_avi_host_md5 and current_avi_host_md5 == latest_avi_host_md5:
                    print_info("No differences detected in file %s, controller checksum: %s and current checksum is: %s" % (host_file, latest_avi_host_md5, current_avi_host_md5))
                    continue
                else:
                    print_info("Migration needed, differences detected in file %s, controller checksum: %s and current checksum is: %s" % (host_file, latest_avi_host_md5, current_avi_host_md5))
                    replace_host_files = True
                    break

        if replace_host_files:
            #download aviservice files and replace it on hostroot
            print_info("Copying latest avihost files from controller.")
            for host_file, local_folder in host_files.items():
                remote_tmp_file = os.path.join(parent_folder, host_file)
                local_tmp_file = os.path.join(local_folder, host_file)
                cmd = 'cp %s %s' % (remote_tmp_file, local_tmp_file)
                move_out = subprocess.check_output(shlex.split(cmd))
                msg = 'move %s to %s completed - done, out: %s' %(remote_tmp_file, local_tmp_file, move_out)
                print_info(msg)
        else:
            print_info("Migration of avihost service not needed")
            return 2
    except subprocess.CalledProcessError as e:
        msg = 'Failed to replace avihost service files, error exception:%s' % str(e)
        print_error(msg)
        return 1
    print_info("Successfully replaced avihost service files.")
    return 0

if __name__ == '__main__':
    exitCode = 0
    try:
        exitCode = copy_avihost_service_to_hostroot()
    except Exception as e:
        traceback.print_exc()
        print_error('Failed to migrate avihost service files, error exception:%s' % str(e))
        sys.exit(1)
    sys.exit(exitCode)
