#!/bin/bash
source config.sh

local_path=results/
remote_path=Test_*

echo "get $remote_path $local_path" | sftp -i ../../scanner @$remote_scanner_ip




now=$(date +"%m-%d-%Y")
first="results/"$now".xml"
echo $first