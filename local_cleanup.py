


import time
import os, errno

 
now = time.strftime("%c")
year = time.strftime("%y")
month = time.strftime("%B")
day = time.strftime("%d")
folder = day + month + year
print folder

directory = os.path.dirname(folder)
#print(os.path.exists(folder))
if (os.path.exists("archive/" +folder+ "/"))==False:
    os.system("mkdir archive/" +folder+ "/")
    os.system("cp results/* archive/" +folder+ "/")
else:
    print "Its there"
    os.system("cp results/* archive/" +folder+ "/")

os.system("cd ../")
os.system("rm results/*")
print "Cleanup Complete"