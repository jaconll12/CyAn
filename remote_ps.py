import os
with open('config.json') as json_data:
    d = json.load(json_data)


URL = d["environment"]["URL"]
path = d["environment"]["path"]
remote_scanner_ip = d["scanner"]["IP"]
ps = d["scanner"]["ps"]
remote_script = (sys.argv[0])  
os.system('ssh -i  scanner@$remote_scanner_ip $ps (sys.argv[0])')