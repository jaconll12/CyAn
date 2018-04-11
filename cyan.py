#converted cyan bash to Python

#source config.sh
#Auto Security Scanner
# Agrigated script to run all scripts

import os
import subprocess
import time
from pprint import pprint
import sys
import nessus_scan
#import zap_scan_api


print "CyAn Start on $Environment"

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
    choice = input("Enter your choice [1-5]: ")
     
    if choice==1:     
        answer = "burp"
        print  "Burp was selected"
        print answer
        loop=False
        ## You can add your code or functions here
    elif choice==2:
        answer = "Web Inspect"
        print  "WebInspect was selected"
        print answer
        loop=False
        ## You can add your code or functions here
    elif choice==3:
        answer = "nessus"
        print  "Nessus was selected"
        print answer
        loop=False
        ## You can add your code or functions here
    elif choice==4:
        answer = "zap"
        print  "Zap was selected"
        print answer
        loop=False
        ## You can add your code or functions here
    elif choice==5:
        answer = "all"
        print  "All Scanners was selected"
        print answer
        loop=False
        ## You can add your code or functions here
    elif choice==6:
        answer = "exit"
        print  "Exiting"
        sys.exit()
        break
        
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")


print answer
#

print "Lets Clean up a bit First"
#remote archive script
os.system("./remote_cleanup.sh")

#local cleanup
os.system("./local_cleanup.sh")

if answer == "burp":     
        print  "Burp scan started"
        os.system("./burp_local.sh")
        ## You can add your code or functions here
elif answer == "Web Inspect":     
        print  "Web Inspect scan started"
        os.system("./remote_ps.sh $path/WI.ps1")
        ## You can add your code or functions here
elif answer == "nessus":     
        print  "Nessus scan started"
        nessus_scan
        #os.system("./remote_ps.sh $path/WI.ps1")
        ## You can add your code or functions here
elif answer == "zap":     
        print  "Zap scan started"
        os.system("python python zap_scan_api.py")
        #subprocess.call("python zap_scan_api.py")
        #os.system("./remote_ps.sh $path/WI.ps1")
        ## You can add your code or functions here\
elif answer == "all":     
        print  "All Scanners started"
        os.system("./burp_local.sh")
        os.system("./remote_ps.sh $path/WI.ps1")
        nessus_scan
        os.system("python python zap_scan_api.py")
        #subprocess.call("python zap_scan_api.py")
        #os.system("./remote_ps.sh $path/WI.ps1")
        ## You can add your code or functions here
else:
    print "Something else"
    #sys.exit()
#SSL Labs Scan
os.system("python pyssltest.py -i in.txt -o out_ssllabs.csv")
print "SSL Labs scan started"

#Start of the Threadfix Uploads
'''



#TheadFix API Uploads
#Burp
if [ "$option" == "Burp" ];then
    python threadfix_upload_burp.py
    ./copy_burp_report.sh
    echo "Burp Report Uploaded"
elif [ "$option" == "All" ];then
    python threadfix_upload_burp.py
    ./copy_burp_report.sh
    echo "Burp Report Uploaded"
fi

  #WebInspect
if [ "$option" == "WI" ];then
    python threadfix_upload_WI.py
    ./copy_down_WI_report.sh
    echo "WebInspect Report Uploaded"
elif [ "$option" == "All" ];then
    python threadfix_upload_WI.py
    ./copy_down_WI_report.sh
    echo "WebInspect Report Uploaded"
fi

#Nessus
if [ "$option" == "Nessus" ];then
    python threadfix_upload_nessus.py
    ./copy_nessus_report.sh
    echo "Nessus Report Uploaded"
elif [ "$option" == "All" ];then
    python threadfix_upload_nessus.py
    ./copy_nessus_report.sh
    echo "Nessus Report Uploaded"
fi

#Zap
if [ "$option" == "Zap" ];then
    python threadfix_upload_ZAP.py
    ./copy_zap_report.sh
    echo "ZAP Scan Uploaded"
elif [ "$option" == "All" ];then
    python threadfix_upload_ZAP.py
    ./copy_zap_report.sh
    echo "ZAP Scan Uploaded"
fi


#copy ssl_labs up
./copy_ssllabs_report.sh

#remote S3 Upload Script
./remote_ps.sh $path/s3_upload.ps1

#remote email sript
./remote_ps.sh $path/email.ps1

echo $option "Cybernetic Analyzer Scans Completed"
'''