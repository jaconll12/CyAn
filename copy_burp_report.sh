#!/bin/bash
source config.sh

local_path=results/
remote_path=*.zip
#remote_path=*.xml


echo "get $remote_path $local_path" | sftp -i ..scanner key@$remote_scanner_ip