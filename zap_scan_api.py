#!/usr/bin/env python
#start zap daemon
# encoding=utf8
# -*- coding: utf-8 -*-

import os
import subprocess
import time
from pprint import pprint
from zapv2 import ZAPv2
from shutil import copyfile

print 'Starting ZAP ...'
subprocess.Popen(['/Applications/OWASP ZAP.app/Contents/Java/zap.sh','-daemon'],stdout=open(os.devnull,'w'))
print 'Waiting for ZAP to load, 10 seconds ...'
time.sleep(10)

# Here the target is defined and an instance of ZAP is created.
 
target = "http://localhost"
zap = ZAPv2()

# Use the line below if ZAP is not listening on 8090.
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})


# ZAP starts accessing the target.
print 'Accessing target %s' % target
zap.urlopen(target)
time.sleep(2)

# The spider starts crawling the website for URLs
print 'Spidering target %s' % target
zap.spider.scan(target)
# Progress of spider
time.sleep(2)


time.sleep(200)

print 'Spider completed'

# Give the passive scanner a chance to finish
time.sleep(5)

# The active scanning starts
print 'Scanning target %s' % target
zap.ascan.scan(target)



time.sleep(300)

print 'Scan completed'

# Report the results
print 'Hosts: ' + ', '.join(zap.core.hosts)
#print 'Alerts: '
#pprint(zap.core.alerts())

#export report to XML
#with open("zap_report.xml", 'w') as f:
#    f.write(zap.core.xmlreport())

report_type = 'xml'
report_file = 'results/zap_report.xml'
with open(report_file, 'a') as f:
    xml = zap.core.xmlreport()
    f.write(xml)
    print('Success: {1} report saved to {0}'.format(report_file, report_type.upper()))

#os.system("mv zap_report.xml results/")

#

# To close ZAP:
zap.core.shutdown()
