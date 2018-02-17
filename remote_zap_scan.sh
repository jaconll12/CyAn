#!/bin/bash
source config.sh
ssh -i  scanner@$remote_scanner_ip $ps $path/powershell-zap/zapscan.ps1
