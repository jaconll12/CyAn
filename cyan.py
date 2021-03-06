#converted cyan bash to Python
#Auto Security Scanner
# Agrigated script to run all scripts
# Created by Jimmy Lloyd
# All rights reserved
# This is open source software
#adding comment for Jenkins more

import os
import subprocess
import time
from pprint import pprint
import sys
import nessus_scan
import docker_start_threadfix
import json
import local_cleanup
import sys 
import create_config

tar = sys.argv[1]
os.system(" python create_config.py " +tar)

with open('config1.json') as json_data:
    d = json.load(json_data)

target = d["environment"]["target"]

print "CyAn Start on ", target
print "Starting Threadfix Docker Image"
docker_start_threadfix
import createin
createin
## Text menu in Python
def print_menu():       ## Your menu design here
    print 30 * "-" , "MENU" , 30 * "-"
    print "1. Burp"
    print "2. Nessus"
    print "3. Zap"
    print "4. All"
    print "5. Exit"
    print 67 * "-"
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-6]: ")
     
    if choice==1:     
        answer = "burp"
        print  "Burp was selected"
        print answer
        loop=False
    elif choice==2:
        answer = "nessus"
        print  "Nessus was selected"
        print answer
        loop=False
    elif choice==3:
        answer = "zap"
        print  "Zap was selected"
        print answer
        loop=False
    elif choice==4:
        answer = "all"
        print  "All Scanners was selected"
        print answer
        loop=False
    elif choice==5:
        answer = "exit"
        print  "Exiting"
        sys.exit()
        break
        
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")

print answer

print "Lets Clean up a bit First"
#local cleanup
local_cleanup

if answer == "burp":     
        print  "Burp scan started"
        import burp_local
        burp_local
        import threadfix_upload_burp
        threadfix_upload_burp
elif answer == "nessus":     
        print  "Nessus scan started"
        nessus_scan
        import threadfix_upload_nessus
        threadfix_upload_nessus
        print "Nessus Report Uploaded"
elif answer == "zap":     
        print  "Zap scan started"
        os.system("python zap_api.py")
        import threadfix_upload_ZAP
        threadfix_upload_ZAP
        print "ZAP Scan Uploaded"
elif answer == "all":     
        print  "All Scanners started"
        import burp_local
        burp_local
        nessus_scan
        os.system("python python zap_scan_api.py")
        import threadfix_upload_burp
        threadfix_upload_burp
        import threadfix_upload_nessus
        threadfix_upload_nessus
        import threadfix_upload_ZAP
        threadfix_upload_ZAP
else:
    print "Something else"
    #sys.exit()
#SSL Labs Scan
os.system("python pyssltest.py -i in.txt -o out_ssllabs.csv")
os.system("powershell /Users/jacoll/CyAn/s3_upload.ps1")
os.system("powershell /Users/jacoll/CyAn/s3_upload.ps1")
print "SSL Labs scan started"
print "Cybernetic Analyzer Scans Completed"

'''
need to rebuild report cloud upload portion
#remote S3 Upload Script
os.system("python remote_ps.py WI.ps1")

os.system("./remote_ps.sh $path/s3_upload.ps1")
#remote email sript
os.system(./remote_ps.sh $path/email.ps1")
'''
