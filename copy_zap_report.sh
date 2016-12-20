#!/bin/bash
source config.sh
cd results/
local_path=zap*.xml
remote_path=/

echo $local_path
echo "put $local_path $remote_path" | sftp -i $key scanner@$remote_scanner_ip
