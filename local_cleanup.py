#source config.sh


import time
import os, errno

 
now = time.strftime("%c")
year = time.strftime("%y")
month = time.strftime("%B")
day = time.strftime("%d")
folder = day + month + year
print folder



os.system("cd archive")

directory = os.path.dirname(folder)
if not os.path.exists(directory):
    os.makedirs(directory)


'''
try:
    os.makedirs(directory)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

if os.path.exists(folder) == true;
    os.system("cp ../results/* $folder")
'''

os.system("cd ../")
os.system("rm results/*")