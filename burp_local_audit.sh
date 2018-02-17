#!/bin/bash
source config.sh


java -jar -Xmx2g /pathto burp/burpsuite_free.jar   https $environment 443 /

#java -jar -Djava.awt.headless=true -Xmx2g /pathto burp/burpsuite_free.jar   https $environment 443 /