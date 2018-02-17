# This script will upload the Tenable Nessus Report from .nessus 
# format to the Internal Ensighten Threadfix server

# import the package
from threadfix_api import threadfix
import glob 
import json
# Open JSON File for login 
with open('../../threadfix.json') as json_data:
    d = json.load(json_data)

host1 = d["threadfix"]["host"]
key = d["threadfix"]["api_key"]
# setup threadfix connection information
host = host1
api_key = key
Nessus_Array = glob.glob('results/*.nessus')
Nessus_File1 = Nessus_Array[0]
#Print out file name as a verification step to make sure you have the file name
print str(Nessus_File1)
tf = threadfix.ThreadFixAPI(host, api_key,verify_ssl=False)
response = tf.upload_scan(
  application_id=,
  file_path=str(Nessus_File1)
)
print "Nessus report Uploaded"
#Print output from function to verify that the file has been uploaded 
print response
