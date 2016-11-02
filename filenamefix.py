import os
import sys
rootdir = "."
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        if ".markdown" in file:
            fullfilename = os.path.join(root, file)
            fixedfilename = fullfilename.replace("-01", "-1")
            os.rename(fullfilename, fixedfilename)
