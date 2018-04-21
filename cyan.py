#converted cyan bash to Python
#Auto Security Scanner
# Agrigated script to run all scripts
# Created by Jmmy Lloyd
# All rights reserved
# This is open source software

import os
import subprocess
import time
from pprint import pprint
import sys
import nessus_scan
import docker_start_threadfix
import json
import local_cleanup

with open('config.json') as json_data:
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
    print "2. Web Inspect"
    print "3. Nessus"
    print "4. Zap"
    print "5. All"
    print "6. Exit"
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
        answer = "Web Inspect"
        print  "WebInspect was selected"
        print answer
        loop=False
    elif choice==3:
        answer = "nessus"
        print  "Nessus was selected"
        print answer
        loop=False
    elif choice==4:
        answer = "zap"
        print  "Zap was selected"
        print answer
        loop=False
    elif choice==5:
        answer = "all"
        print  "All Scanners was selected"
        print answer
        loop=False
    elif choice==6:
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
elif answer == "Web Inspect":     
        print  "Web Inspect scan started"
        os.system("python remote_ps.py WI.ps1")
        import threadfix_upload_WI
        threadfix_upload_WI
        print "WebInspect Report Uploaded"
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
        os.system("python remote_ps.py WI.ps1")
        nessus_scan
        os.system("python python zap_scan_api.py")
        os.system("python remote_ps.py WI.ps1")
        import threadfix_upload_burp
        threadfix_upload_burp
        import threadfix_upload_WI
        threadfix_upload_WI
        import threadfix_upload_nessus
        threadfix_upload_nessus
        import threadfix_upload_ZAP
        threadfix_upload_ZAP
else:
    print "Something else"
    #sys.exit()
#SSL Labs Scan
os.system("python pyssltest.py -i in.txt -o out_ssllabs.csv")
print "SSL Labs scan started"
print "Cybernetic Analyzer Scans Completed"

'''
#remote S3 Upload Script
os.system("./remote_ps.sh $path/s3_upload.ps1")
#remote email sript
os.system(./remote_ps.sh $path/email.ps1")
'''
