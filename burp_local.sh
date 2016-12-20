#!/bin/bash
source config.sh
java -jar -Djava.awt.headless=true -Xmx2g /Applications/Burp\ Suite\ Professional.app/Contents/java/app/burpsuite_pro.jar   https $environment 443 /
