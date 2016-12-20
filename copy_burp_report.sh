#!/bin/bash
source config.sh

local_path=*.xml
local_path2=*.csv
remote_path=/
cp $local_path results/

echo "put $local_path $remote_path" | sftp -i $key scanner@$remote_scanner_ip
echo "put $local_path2 $remote_path" | sftp -i $key scanner@$remote_scanner_ip

rm -f *.xml
