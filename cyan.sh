#!/bin/bash
source config.sh
#Auto Security Scanner
# Agrigated script to run all scripts
echo "CyAn Start on $Environment"



PS3="Please choose an option "
select option in Burp WebInspect Nessus Zap All
do
    case $option in
        Burp)
            echo "Burp"
            break;;
        WebInspect)
            echo "WebInspect"
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
     esac
done

echo "Lets Clean up a bit First"
#remote archive script
./remote_cleanup.sh

#local cleanup
./local_cleanup.sh

#Burp Scan of Manage New UI
if [ "$option" == "Burp" ];then
    echo "Burp scan started"
    ./burp_local.sh
elif [ "$option" == "All" ];then
    echo "Burp scan started"
    ./burp_local.sh
fi


#Remote WebInspect Scan
if [ "$option" == "WebInspect" ];then
    ./remote_ps.sh $path/WI.ps1
    echo "WebInsoect Scan Completed"
elif [ "$option" == "All" ];then
     ./remote_ps.sh $path/WI.ps1
    echo "WebInsoect Scan Completed"
fi


#sleep(5)
#Nessus Scanner
if [ "$option" == "Nessus" ];then
    python nessus_scan.py
    echo "Nessus scan started"
elif [ "$option" == "All" ];then
    python nessus_scan.py
    echo "Nessus scan started"
fi

#Zap Scanner
if [ "$option" == "Zap" ];then
    python zap_scan_api.py
    echo "Zap scan started"
elif [ "$option" == "All" ];then
    python zap_scan_api.py
    echo "Zap scan started"
fi

#SSL Labs Scan
python pyssltest.py -i in.txt -o out_manage_ssllabs.csv
echo "SSL Labs scan started"

#copy down WI report for parsing
./copy_down_WI_report.sh

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
