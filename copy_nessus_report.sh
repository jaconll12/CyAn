#!/bin/bash
source config.sh

local_path=results/*.nessus
remote_path=/

echo "put $local_path $remote_path" | sftp -i $key scanner@$remote_scanner_ip
