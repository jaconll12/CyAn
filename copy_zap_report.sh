#!/bin/bash
source config.sh

local_path=results/
remote_path=zap_report.xml

echo "get $remote_path $local_path" | sftp -i ../../ scanner@$remote_scanner_ip