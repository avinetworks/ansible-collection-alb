#!/bin/bash -x
############################################################################
# ========================================================================
# Copyright 2024 VMware, Inc. All rights reserved. VMware Confidential
# ========================================================================
###

start()
{
    if [[ -f /opt/avitest_python_version ]]; then
        # For testing against python2 and python3
        version=$(cat /opt/avitest_python_version)
    else
        # Ref: https://stackoverflow.com/a/38485534/9328077
        version='0'
        command -v python >/dev/null 2>&1 && version=''
        command -v python2 >/dev/null 2>&1 && version='2'
        command -v python3 >/dev/null 2>&1 && version='3'
    fi

    if [[ $version != '0' ]]; then
        exec python$version /usr/sbin/avi_host_server.py
    else
        echo "Unable to find any installed python"
        exit 1
    fi
}

stop()
{
    pkill -f avi_host_server.py
}

case "$1" in
    "start")
        start
    ;;
    "stop")
        stop
    ;;
    *)
        echo "unhandled case for avihost service"
        exit 1
    ;;
esac
