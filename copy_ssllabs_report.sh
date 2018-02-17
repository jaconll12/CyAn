#!/bin/bash
source config.sh

local_path=out_ssllabs.csv


cp $local_path results/
echo "put $local_path $remote_path" | sftp -i @$remote_scanner_ip

rm -f out_ssllabs.csv


