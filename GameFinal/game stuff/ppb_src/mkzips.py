# Make a zip file of all of the files for PPB
import sys
import os
import glob, shutil
import zipfile

OUTFILE = 'ppb_src.zip'
ZIP_SRC_FILES = []
WILDCARDS = ["*.py","*.ico","*.txt","*.pyd","*.dll","*.exe","*.wxg","*.conf"]

for x in WILDCARDS:
    for y in glob.glob(x):
        ZIP_SRC_FILES.append(y)

if os.path.exists(OUTFILE): os.unlink(OUTFILE)

srczip = zipfile.ZipFile(file=OUTFILE,mode='w',compression=zipfile.ZIP_DEFLATED)

for x in ZIP_SRC_FILES:
    print "*** Adding: %s" % (x,)
    srczip.write(x)
#end loop

srczip.close()

print "Done. Zip file is %s" % (OUTFILE,)