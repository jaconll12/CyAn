# python create config.json file
import json
import sys
tar = sys.argv[1]

with open('config1.json', 'r') as json_data:
    d = json.load(json_data)
    d["environment"]["target"] = tar
with open('config1.json', 'w') as json_data:
    json.dump(d, json_data, indent=4)
    json_data.close()
