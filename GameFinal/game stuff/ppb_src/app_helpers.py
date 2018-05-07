# app_helpers.py -- Extra functions

import os, sys
USE_SHELL = True
try:
    import pythoncom
    from win32com.shell import shell, shellcon
except ImportError:
    USE_SHELL = False

# Creates a shortcut on the desktop to the app
def createAppShortcut(to_file, iconfile, desc="Pygame Package Builder"):
    assert sys.platform == 'win32', 'This feature is only available on Windows'
    shortcut = pythoncom.CoCreateInstance (
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink
    )
    shortcut.SetPath (sys.executable)
    shortcut.SetArguments("-OO " + to_file)
    if desc is None:
        desc = "Python %s" % sys.version
    shortcut.SetDescription (desc)
    shortcut.SetIconLocation (iconfile,0)
    shortcut.SetWorkingDirectory(os.path.abspath(os.curdir))

    desktop_path = shell.SHGetFolderPath (0, shellcon.CSIDL_DESKTOP, 0, 0)
    persist_file = shortcut.QueryInterface (pythoncom.IID_IPersistFile)
    persist_file.Save (os.path.join (desktop_path, "Pygame Package Builder.lnk"), 0)
# end createAppShortcut

# Checks for shortcut on desktop
def shortcutExists():
    assert sys.platform == 'win32', 'This feature is only available on Windows'
    desktop_path = shell.SHGetFolderPath (0, shellcon.CSIDL_DESKTOP, 0, 0)
    if os.path.exists(os.path.join(desktop_path,'Pygame Package Builder.lnk')): return True
    return False
# end shortcutExists

if __name__ == '__main__':
    createAppShortcut('pygame_builder.py', os.path.join(os.path.abspath(os.curdir),'pygame.ico'),"Pygame Package Builder")