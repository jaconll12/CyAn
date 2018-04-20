#!/bin/bash
import os
import json


with open('config.json') as json_data:
    d = json.load(json_data)

target = d["environment"]["target"]

os.system("java -jar -Djava.awt.headless=true -Xmx2g /Applications/Burp\ Suite\ Community\ Edition.app/Contents/java/app/burpsuite_community.jar    https " +target+ " 443 /")
