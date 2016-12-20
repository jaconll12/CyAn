# This script will upload the Burp Suite Report from XML
# format to the Internal Ensighten Threadfix server.

# import the package
from threadfix_api import threadfix
import glob
import json
# Open JSON File for login
with open('path to json file') as json_data:
    d = json.load(json_data)


host1 = d["threadfix"]["host"]
key = d["threadfix"]["api_key"]
# setup threadfix connection information
host = host1
api_key = key
Burp_Array = glob.glob('path to Burp XML File')
Burp_File = Burp_Array[0]
#Print out file name as a verification step to make sure you have the file name
print str(Burp_File)
tf = threadfix.ThreadFixAPI(host, api_key,verify_ssl=False)
response = tf.upload_scan(
  application_id=x,
  file_path=str(Burp_File)

)
print "Burp report Uploaded"
print response
