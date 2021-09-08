#this script shall read and print the services versions that are located in the package.json files of the directory 
#run this script from the folder containing the services folder

import os
import json
import glob

packagefiles = []
for root, dirnames, filenames in os.walk("."):
    packagefiles.extend(glob.glob(root + "/*package.json"))

for i in range (0,len(packagefiles)):
    with open (packagefiles[i]) as f:
      data = json.load(f)
    print("Name:", data['name']," ,Version:", data['version'] )