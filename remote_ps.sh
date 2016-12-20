#!/bin/bash
source config.sh
ssh -i $key scanner@$remote_scanner_ip powershell.exe $1