import os
import json
import sys 
with open('config.json') as json_data:
    d = json.load(json_data)


target = d["environment"]["target"]
path = d["environment"]["path"]
remote_scanner_ip = d["scanner"]["IP"]
ps = d["scanner"]["ps"]
remote_script = (sys.argv[0])  
os.system("ssh -i  scanner@" +remote_scanner_ip +ps +remote_script)