#!/bin/bash
source config.sh

local_path=results/
remote_path=$Environement/*

echo "get $remote_path $local_path" | sftp -i $key scanner@$remote_scanner_ip

now=$(date +"%m-%d-%Y")
first="results/Environement/"$now".xml"
