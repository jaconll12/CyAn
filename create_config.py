# python create config.json file
import json
tar = "https://localhost"

data = {'environment':[{'target': tar, 'path': 'remote path'}]}
out_file = open("config1.json","w")
#json.dumps(data, indent=4)
json.dump(data,out_file, indent=4)  
