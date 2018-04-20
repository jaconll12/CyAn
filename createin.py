#python file to create in.txt file
import json
with open('config.json') as json_data:
    d = json.load(json_data)

target = d["environment"]["target"]
with open("in.txt", "w") as text_file:
    text_file.write(target) 
 
 
text_file.close() 