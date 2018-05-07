#!/usr/bin/env python

import os
import sys

def calcDirSize(arg, dir, files):
	for file in files:
		stats = os.stat(os.path.join(dir, file))
		size = stats[6]
		arg.append(size)

def getDirSize(dir):
	
	sizes = []
	os.path.walk(dir, calcDirSize, sizes)
	total = 0
	for size in sizes:
		total = total + size
	if total > 1073741824:
		return (round(total/1073741824.0, 2), 'GB')
	if total > 1048576:
		return (round(total/1048576.0, 2), 'MB')
	if total > 1024:
		return (round(total/1024.0, 2), 'KB')
	return (total, 'bytes')
#end getDirSize()

def testDirScan():
	
     dir = sys.argv[1]

     print "Testing directorySize..."
     print "Directory: %s" % (dir,)
     amount, units = getDirSize(dir)
     print "Size: %s %s" % (amount, units)

if __name__ == '__main__':
     testDirScan()
