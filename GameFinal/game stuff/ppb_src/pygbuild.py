#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# pygbuild.py -- Pygame Package Builder for CLI

# Author: Devin Watson
# This uses the same underlying build engine as the GUI version
# 
# Command-line options:
#
# --project= or -p= : Project file
# --log or -l= : Log to file instead of stdout/stderr
# --version or -v : Print version information and exit

import sys, os
import getopt
import pickle
from pygame_project import *

import datetime

try:
    import psyco
    psyco.full()
except ImportError: pass

__version__ = '1.1 BETA'
APP_NAME = "PygBuild"

STARTDIR = os.path.abspath(os.path.curdir)
#sys.path.append(os.path.curdir)

os.environ['PYTHONPATH'] = os.path.curdir

logfile = None
project_file = None

short_opts = 'p:l:v'
long_opts = ['project=','logfile=','version']
opts_desc = ['PPF project file to build against. Short form: -p','Log output to a file instead of stdout/stderr. Short form: -l','Print version information. Short form: -v']

# Small override class used to 
# shunt the output to a file
class BuildTextShunt:
    def __init__(self, txtfile):
        if os.path.exists(txtfile): os.unlink(txtfile)
        self._txt_obj = open(txtfile,'w')
    def write(self, new_text):
        try:
            self._txt_obj.write(new_text)
        except:
            pass

    def flush(self):
        self._txt_obj.flush()
        
    def __del__(self):
        self._txt_obj.close()

def print_version():
    print APP_NAME + ' ' + __version__
    pyver = sys.version_info
    print "Built with Python " + str(pyver[0]) + "." + str(pyver[1]) + "." + str(pyver[2])
    print

def usage():
    print_version()
    print "Usage:"
    print
    for x in range(0,len(long_opts)):
        print "--%s\t\t%s" % (long_opts[x],opts_desc[x])
# end usage()

options, remainder = getopt.getopt(sys.argv[1:], short_opts, long_opts)

if len(options) == 0:
    usage()
    sys.exit()

#print options
#print sys.argv[1:]
for opt, arg in options:
    if opt in ('-p', '--project'):
        try:
            sys.argv.remove("-p %s" % (arg,))
        except ValueError: pass
        try:
            sys.argv.remove("--project=%s" % (arg,))
        except ValueError: pass
        project_file = arg
    elif opt in ('-v', '--version'):
        print_version()
        sys.exit()
    elif opt in ('-l', '--logfile'):
        try:
            sys.argv.remove("-l %s" % (arg,))
        except ValueError: pass
        try:
            sys.argv.remove("--logfile=%s" % (arg,))
        except ValueError: pass
        logfile = arg
#end for loop

if project_file is None or project_file.strip() == '':
    print "*** Missing project file name. Use --project= or -p"
    print
    usage()
    sys.exit()
#end if 

if not os.path.exists(project_file):
    print "*** Cannot find project file %s " % (project_file,)
    sys.exit()
#end if

# We get this far then the project_file is valid, and we can load it
Project = pickle.load(open(project_file,'rb'))

if logfile is not None and logfile.strip() != '':
    print "Logging to %s" % (logfile,)
    TextShunt = BuildTextShunt(logfile)
    sys.stdout = TextShunt
    sys.stderr = TextShunt
# end if

# In order to call pyg2exe without having it fail out because of our own
# parameters, we have to clear out everything then append in pyg2exe
sys.argv.append("pyg2exe")

right_now = datetime.datetime.today()

print "Build process started on %s-%s-%s %s\n" % (right_now.year,right_now.month,right_now.day,right_now.time())
print "Base game directory: %s" % (Project.baseGameDir,)

BuildEngine = PyGameBuildEngine(Project)

try:
    BuildEngine.RunBuild()
except NoProjectError:
    print "Error: No valid PPF file found .. Build aborted."
except NoIconError:
    print "Error: No icon found"
except NameError, e:
    print "*** Fatal Build Error ***"
    print e
    print e.args
    #print "Fatal error: " + str(type(inst)) + " " + inst + " .. Build aborted."
except BuildError, e:
    print "*** Fatal Build Error ***"
    print e
finally:
    BuildEngine.Cleanup()
    
BuildEngine.runPost()