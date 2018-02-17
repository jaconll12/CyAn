#!/bin/bash
source config.sh

local_path=PS
remote_path=*.ps1
echo "get $remote_path $local_path" | sftp -i ../../ scanner@$remote_scanner_ip