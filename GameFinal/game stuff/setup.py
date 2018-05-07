from distutils.core import setup
import py2exe
import os

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
        if os.path.basename(pathname).lower() in ("libogg-0.dll", "dsdl_ttf.dll", "sdl_ttf.dll"):
                return 0
        return origIsSystemDLL(pathname)
    
py2exe.build_exe.isSystemDLL = isSystemDLL


setup(
windows=["Main.py"]
)
