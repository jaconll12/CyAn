#!/bin/bash
source config.sh
#Auto Security Scanner
# Agrigated script to run all scripts
echo "CyAn Start on $environment"
ssh-add -K ../../scanner 
#Choose Which Environment to run CyAn on
#./config.sh

PS3="Please choose an option "
select option in Burp Nessus Zap All Quit
do
    case $option in
        Burp)
            echo "Burp"
            break;;
        Nessus)
            echo "Nessus"
            break;;
        Zap)
            echo "Zap"
            break;;
        All)
            echo "All Scanners"
            break;;
        Quit)
            break;;
        
     esac
done

if [ "$option" == "Quit" ];then
    echo "Qutting"
    exit
fi


#Burp Scan of Manage New UI
if [ "$option" == "Burp" ];then
    echo "Burp scan started"
    ./remote_burp_scan.sh
    echo "Waiting for Burp Scan to complete ....will wait 20 min"
    sleep 1200
    #./burp_local_audit.sh
elif [ "$option" == "All" ];then
    echo "Burp scan started"
    ./remote_burp_scan.sh
    echo "Waiting for Burp Scan to complete ....will wait 20 min"
    sleep 1200
fi



#sleep(5)
#Nessus Scanner
if [ "$option" == "Nessus" ];then
    python nessus_audit_scan.py
    sleep 45
    echo "Nessus scan started"
elif [ "$option" == "All" ];then
    python nessus_audit_scan.py
    echo "Nessus scan started"
    sleep 45
fi

#Zap Scanner
if [ "$option" == "Zap" ];then
    #./zap_fullrun.sh 
    #python zap_api.py
    ./remote_zap_scan.sh
    echo "Zap scan started"
elif [ "$option" == "All" ];then
    #./zap_fullrun.sh 
     #python zap_api.py
    ./remote_zap_scan.sh
    echo "Zap scan started"
fi

#SSL Labs Scan 
python pyssltest.py -i in.txt -o out_manage_ssllabs.csv
echo "SSL Labs scan started"


#Copy Burp report up
./copy_burp_report.sh

#copy Nessus report up
./copy_nessus_report.sh

#copy Zap scan down
./copy_zap_report.sh

#copy ssl_labs up
./copy_ssllabs_report.sh

#remote S3 Upload Script
./remote_ps.sh $path/s3_upload_NUI.ps1

#remote email sript
#Removing temporarily because of login issues.
#./remote_ps.sh $path/email_NewUI.ps1


#TheadFix API Uploads
#Burp
if [ "$option" == "Burp" ];then
    python threadfix_upload_burp.py
    echo "Burp Scan Uploaded"
elif [ "$option" == "All" ];then
    python threadfix_upload_burp.py
    echo "Burp Scan Uploaded"
fi

#Nessus
if [ "$option" == "Nessus" ];then
    python threadfix_upload_nessus.py
    echo "Nessus Scan Uploaded"
elif [ "$option" == "All" ];then
    python threadfix_upload_nessus.py
    echo "Nessus Scan Uploaded"
fi

#Zap
if [ "$option" == "Zap" ];then
    python threadfix_upload_ZAP.py 
    echo "ZAP Scan Uploaded"
elif [ "$option" == "All" ];then
    python threadfix_upload_ZAP.py 
    echo "ZAP Scan Uploaded"
fi
echo  
#remote archive script
./remote_cleanup.sh

#local cleanup
./local_cleanup.sh 
echo $option "Cybernetic Analyzer Scans Completed for $environment"

