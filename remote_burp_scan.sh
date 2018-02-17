#!/bin/bash
source config.sh
ssh -i  scanner@$remote_scanner_ip $ps $path/burp_remote.ps1
