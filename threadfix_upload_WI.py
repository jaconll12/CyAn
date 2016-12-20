# This script will upload the HP WebInspect port from XML
# format to the Internal Ensighten Threadfix server

from threadfix_api import threadfix
import glob
import json

# Open JSON File for conf data
with open('path to json file') as json_data:
    config = json.load(json_data)

# Setup threadfix connection information
host = config["threadfix"]["host"]
api_key = config["threadfix"]["api_key"]

WI_Array = glob.glob('path to WI report')
WI_File = WI_Array[0]

print "Files to be loaded:"
print str(WI_File)

print "Uploading WebInspect report..."
tf = threadfix.ThreadFixAPI(host, api_key, verify_ssl=False)
response = tf.upload_scan(
  application_id=x,
  file_path=str(WI_File)
)

print "WebInspect report Uploaded, response:"
print response
