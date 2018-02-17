#!/bin/bash
source config.sh

local_path=results/*.nessus
remote_path=/
#sftp -v -oIdentityFile=path user@server <<EOF
#cp $local_path results/

echo "put $local_path $remote_path" | sftp -i ../../ scanner@$remote_scanner_ip

