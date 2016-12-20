#!/bin/bash
source config.sh
ssh -i $key scanner@$scanner_ip powershell.exe $path/cleanup.ps1
