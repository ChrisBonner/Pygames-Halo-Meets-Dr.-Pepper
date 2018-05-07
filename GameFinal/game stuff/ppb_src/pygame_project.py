# pygame_project.py -- Encapsulates all of the project variables
# into a single class for easy saving and loading using the pickle interface
import sys, os, shutil, glob
import pygame
from DirCalc import *
from distutils.errors import *
import fnmatch

# Need to make sure that we can get to a default icon
# so the system has a sane build foundation
PYGAMEDIR = os.path.split(pygame.base.__file__)[0]
if not os.path.exists(os.path.join(PYGAMEDIR,'pygame.ico')):
    PYGAMEDIR = os.path.abspath(os.path.curdir)

# PyGameProject encapsulates 
# all of the storage and functions
# to help build a pygame app package using pyg2exe
# and possibly py2app
class PyGameProject:
    def __init__(self):
        self.authorName = ''
        self.gameVersion = '1.0'
        self.authorEmail = ''
        self.gameURL = ''
        self.gameName = ''
        self.versionString = ''
        self.useDefaultIcon = 1
        self.iconFile = None
        self.extraFiles = []
        self.optimizeLevel = 2
        self.mainScript = None
        self.baseGameDir = None
        self.compression = 1
        self.removeBuildOnExit = 1
        # Dist directory
        self.distDir = 'dist'
        self.target = 'py2exe'
        self.targetType = 'win'
        self.exe_name = None
        self.bundleLevel = 2
        self.useASCIIOnly = 1
        self.ignoreModules = []
        self.excludeModules = []
        self.includeSDL = 0
        self.libraryFile = 'library.zip'
        # Post-build instructions
        self.runScriptPost = 0    # Run a Python script after build
        self.runScriptPostOnFail = 0 # Only run the script if the build fails
        self.postScript = None    # Path to Python script to run post
        
    # end __init__     
#end Class

class ExtraGameData:
    def __init__(self, path, type, recurse, wildcard, target):
        self.type = type    # 0 - File, 1 - Folder
        self.path = path
        self.recurse = recurse # Recursively search?
        self.wildcard = wildcard
        self.target = target    # target output folder (relative to root of dist)
    
    def gatherFiles(self):
        if self.type == 0:  # File
            return self.target, [self.path,]
        if self.type == 1:  # Folder
            if not self.recurse:
                return self.target, glob.glob(os.path.join(self.path,self.wildcard))
            else:
                # Do a recursive, glob-like search for files and return
                # the list
                filepaths = []
                for dirpath, dirnames, filenames in os.walk(self.path):
                    filepaths.extend (os.path.join (dirpath, f) for f in fnmatch.filter (filenames, self.wildcard))
                return self.target, filepaths
    # end gatherFiles
#end class


# Build Engine exceptions
class BuildEngineError(Exception):
    pass
#end class

class NoProjectError(BuildEngineError):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
#end class

class NoIconError(BuildEngineError):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
#end class

class BuildError(BuildEngineError):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
# end class

# Encapsulates the project build logic,
# fed by a PyGameProject object
class PyGameBuildEngine:
    def __init__(self,prj = None):
        self.Project = prj
        self.buildPassed = False
        
    def RunBuild(self):
        if self.Project is None: raise NoProjectError("No project selected for build")
    
        # Customized executable builder for Pygame-based projects
        from distutils.core import setup
        import py2exe

        # First, take care of the icon file
        ICONFILE = None
        if self.Project.useDefaultIcon:
            print "Copying default icon from %s..." % (PYGAMEDIR,)
            icon_file = os.path.join(PYGAMEDIR, 'pygame.ico')
            if not os.path.exists(icon_file): raise NoIconError("Default Pygame icon file not found")
            shutil.copyfile(icon_file,os.path.join(self.Project.baseGameDir,'pygame.ico'))
            ICONFILE = 'pygame.ico'
        else:
            # Custom icons are a little trickier
            if not os.path.dirname(self.Project.iconFile) != self.Project.baseGameDir and not os.path.exists(os.path.join(self.Project.baseGameDir,os.path.basename(self.Project.iconFile))):
                print "Copying icon file %s..." % (os.path.basename(self.Project.iconFile),)
                if not os.path.exists(self.Project.iconFile): raise NoIconError("Custom icon %s not found" % (os.path.basename(self.Project.iconFile),))
                shutil.copyfile(self.Project.iconFile,os.path.join(self.Project.baseGameDir,os.path.basename(self.Project.iconFile)))
            ICONFILE = os.path.basename(self.Project.iconFile)
        
        print "Game Name: %s" % (self.Project.gameName)
        print "Executable Binary: %s" % (self.Project.exe_name)
        print "Changing directory to %s" % (self.Project.baseGameDir,)
        print "Main Script: %s" % (self.Project.mainScript,)
        print
        output_directory = os.path.join(self.Project.baseGameDir,self.Project.distDir)
        # This allows the game's modules to be found and compiled
        os.environ['PYTHONPATH'] = self.Project.baseGameDir
        #print "os.environ['PYTHONPATH'] = %s" % (os.environ['PYTHONPATH'],)
        # If the dist directory already exists, we have to remove it, otherwise it will cause Distutils to choke
        if os.path.exists(output_directory): 
            print "Output directory exists, removing and recreating..."
            shutil.rmtree(output_directory)
        print "Output directory is %s" % (output_directory,)
        try:
            sys.path.remove(self.Project.baseGameDir)
        except ValueError:
            sys.path.append(self.Project.baseGameDir)
        
        INCLUDE_MODULES = None

        IGNORE_MODS = []
        EXCLUDE_MODS = []
        
        print "*** Excluded Modules ***"
        for x in range(0,len(self.Project.excludeModules)):
            EXCLUDE_MODS.append(self.Project.excludeModules[x])
            print self.Project.excludeModules[x]
        print
        
        print "*** Ignored Modules ***"
        for x in range(0,len(self.Project.ignoreModules)):
            IGNORE_MODS.append(self.Project.ignoreModules[x])
            print self.Project.ignoreModules[x]
        print
        
        extra_files = []
        for i in range(0,len(self.Project.extraFiles)):
            target, flist = self.Project.extraFiles[i].gatherFiles()
            extra_files.append((target,flist))
            
        print "Project Target: %s %s" % (self.Project.targetType,self.Project.target)
        #Project.bundleLevel = 1
        ZIPOUTFILE = None
        
        if self.Project.compression and self.Project.bundleLevel == 1:
            ZIPOUTFILE = self.Project.libraryFile
        
        os.chdir(self.Project.baseGameDir)

        BUILD_OPTIONS = {self.Project.target: { 
                                    "optimize": self.Project.optimizeLevel, 
                                    "includes": INCLUDE_MODULES, 
                                    "compressed": self.Project.compression, 
                                    "ascii": self.Project.useASCIIOnly, 
                                    "bundle_files": self.Project.bundleLevel, 
                                    "ignores": IGNORE_MODS, 
                                    "excludes": EXCLUDE_MODS, 
                                    "unbuffered": 1
                                } 
                        }
        print
        print "Build options used: "
        print 
        print BUILD_OPTIONS
        print
        print
        print "*** Extra Files Included ***"
        print
        print extra_files
        print 
        
        if self.Project.targetType == 'win':
            try:
                setup(windows=[{'script': str(self.Project.mainScript),
                                'other_resources': [(u"VERSIONTAG",1,str(self.Project.gameName) + ' ' + str(self.Project.gameVersion))],
                                'icon_resources': [(1,ICONFILE)]
                               }],
                        options = BUILD_OPTIONS,
                        name = str(self.Project.gameName),
                        version = str(self.Project.gameVersion),
                        data_files = extra_files,
                        zipfile = ZIPOUTFILE,
                        author = str(self.Project.authorName),
                        author_email = str(self.Project.authorEmail),
                        url = str(self.Project.gameURL)
                )
                if sys.platform == 'win32' and self.Project.includeSDL:
                    self.copyCoreFiles()
                # "exe_name": self.Project.exe_name
                root, ext = os.path.splitext(self.Project.mainScript)
                tmp_exe = os.path.join('dist',root,'.exe')
                fin_exe = os.path.join('dist',self.Project.exe_name,'.exe')
                shutil.move(tmp_exe,fin_exe)
            except Exception, err:
                raise BuildError(err)
            except:
                raise BuildError('Unspecified error occurred during build')
        elif self.Project.targetType == 'con':
            try:
                setup(console=[{'script': str(self.Project.mainScript),
                            'other_resources': [(u"VERSIONTAG",1,str(self.Project.gameName) + ' ' + str(self.Project.gameVersion))],
                                         'icon_resources': [(1,ICONFILE)]
                           }],
                        options = BUILD_OPTIONS,
                        name = str(self.Project.gameName),
                        version = str(self.Project.gameVersion),
                        data_files = extra_files,
                        zipfile = ZIPOUTFILE,
                        author = str(self.Project.authorName),
                        author_email = str(self.Project.authorEmail),
                        url = str(self.Project.gameURL)
                )
                if sys.platform == 'win32' and self.Project.includeSDL:
                    self.copyCoreFiles()
                root, ext = os.path.splitext(str(self.Project.mainScript))
                tmp_exe = os.path.join('dist',str(root),'.exe')
                fin_exe = os.path.join('dist',str(self.Project.exe_name),'.exe')
                shutil.move(tmp_exe,fin_exe)
            except Exception, err:
                raise BuildError(err)
            except:
                raise BuildError('Unspecified error occurred during build')
            
        self.buildPassed = True
    #end RunBuild()
    
    # Tries to do a reasonable job of cleaning up after a build job
    # Checks to see if the build finished successfully or not, then
    # does its cleanup job based on that
    def Cleanup(self):
        output_directory = os.path.join(self.Project.baseGameDir,self.Project.distDir)
        
        if self.buildPassed:
            if os.path.exists(os.path.join(self.Project.baseGameDir,self.Project.distDir,'tcl')): shutil.rmtree(os.path.join(self.Project.baseGameDir,self.Project.distDir,'tcl'))
            if os.path.exists(os.path.join(self.Project.baseGameDir,self.Project.distDir,'tcl84.dll')): os.unlink(os.path.join(self.Project.baseGameDir,self.Project.distDir,'tcl84.dll'))
            if os.path.exists(os.path.join(self.Project.baseGameDir,self.Project.distDir,'tk84.dll')): os.unlink(os.path.join(self.Project.baseGameDir,self.Project.distDir,'tk84.dll'))

            if self.Project.useDefaultIcon and os.path.exists(os.path.join(self.Project.baseGameDir,'pygame.ico')):
                os.unlink(os.path.join(self.Project.baseGameDir,'pygame.ico'))

            if self.Project.removeBuildOnExit:
                print "Removing /build subdirectory"
                if os.path.exists(os.path.join(self.Project.baseGameDir,'build')):
                    shutil.rmtree(os.path.join(self.Project.baseGameDir,'build'))

            buildSize = getDirSize(output_directory)

            if self.Project.useDefaultIcon:
                shutil.copyfile(os.path.join(PYGAMEDIR, 'pygame.ico'),os.path.join(self.Project.baseGameDir,self.Project.distDir,'pygame.ico'))
    
            # Copy in the default font file, so Pygame doesn't choke without having it.
            # This seems to be an intermittent error, but this will ensure it doesn't happen
            shutil.copyfile(os.path.join(PYGAMEDIR, pygame.font.get_default_font()),os.path.join(self.Project.baseGameDir,self.Project.distDir,pygame.font.get_default_font()))

            print "Build finished. Package is %s %s" % (buildSize[0],buildSize[1])
            print self.Project.gameName + " is in " + os.path.join(self.Project.baseGameDir,self.Project.distDir)

        else:
            print 
            print "Build failed. Cleaning up..."
            print
            if self.Project.useDefaultIcon and os.path.exists(os.path.join(self.Project.baseGameDir,'pygame.ico')):
                os.unlink(os.path.join(self.Project.baseGameDir,'pygame.ico'))

            if os.path.exists(os.path.join(self.Project.baseGameDir,'build')):
                shutil.rmtree(os.path.join(self.Project.baseGameDir,'build'))
    # end Cleanup()
    
    # Windows function that copies the core
    # SDL dll files into the dist directory
    def copyCoreFiles(self):
        if sys.platform == 'win32' and self.Project.includeSDL:
            print "*** Copy SDL Libraries ***"
            os.chdir(self.Project.baseGameDir)
            dll_list = glob.glob(os.path.join(PYGAMEDIR,'*.dll'))
            for f in dll_list:
                fname = os.path.basename(f)
                try:
                    shutil.copyfile(f,os.path.join(self.Project.baseGameDir,self.Project.distDir,fname))
                    print "Copying %s to %s" % (f, os.path.join(self.Project.baseGameDir,self.Project.distDir))
                except: pass
            print
    #end copyCoreFiles
    
    def runPost(self):
        last_path = os.path.abspath(os.getcwd())
        if self.Project.runScriptPost == 1 and self.Project.postScript is not None and os.path.exists(self.Project.postScript):
            if (self.buildPassed and self.Project.runScriptPostOnFail == 0) or (self.buildPassed == False and self.Project.runScriptPostOnFail == 1):
                print "Executing post-build script %s" % (self.Project.postScript,)
                os.chdir(os.path.dirname(self.Project.postScript))
                o_file = open(self.Project.postScript,'r')
                script_contents = o_file.read()
                o_file.close()
                try:
                    exec(script_contents)
                except Exception, e:
                    print "Error in post-build script: %s" % (e,)
                finally:
                    os.chdir(last_path)
                print
    #end runPost

Project = PyGameProject()