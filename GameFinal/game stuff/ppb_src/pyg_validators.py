#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# pyg_validators.py -- wxPython control validator classes for PPB

import wx
import string

# Special validator class for setting executable
# names.
# Currently allowed:
# Letters, Numbers, Dots (.), Underscores (_)
class EXEValidator(wx.PyValidator):
    def __init__(self, flag = None, pyVar = None):
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)
        self.allowedKeys = ['.','_']
        for x in string.letters:
            self.allowedKeys.append(x)
        for x in string.digits:
            self.allowedKeys.append(x)
        
    def Clone(self):
        return EXEValidator(self.flag)
        
    def Validate(self, win):
        tc = self.GetWindow()
        val = tc.GetValue()
        for x in val:
            if not x in self.allowedKeys:
                return False
        return True
        
    def OnChar(self, event):
        key = event.GetKeyCode()
        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return

        if chr(key) in self.allowedKeys:
            event.Skip()
            return

        # Returning without calling event.Skip eats the event before it
        # gets to the text control
        return
# end class EXEValidator

# Data validation class for e-mail addresses
# Note that this only checks to make sure it has
# legal characters in the string, not if it's a valid
# e-mail address at all!
# Currently allowed:
# Letters, Numbers, Dots (.), Underscores (_), @ symbol
class EMailValidator(wx.PyValidator):
    def __init__(self, flag = None, pyVar = None):
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)
        self.allowedKeys = ['.','_',chr(64)]
        for x in string.letters:
            self.allowedKeys.append(x)
        for x in string.digits:
            self.allowedKeys.append(x)
        
    def Clone(self):
        return EMailValidator(self.flag)
        
    def Validate(self, win):
        tc = self.GetWindow()
        val = tc.GetValue()
        for x in val:
            if not x in self.allowedKeys:
                return False
        return True
        
    def OnChar(self, event):
        key = event.GetKeyCode()
        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return

        if chr(key) in self.allowedKeys:
            event.Skip()
            return

        # Returning without calling event.Skip eats the event before it
        # gets to the text control
        return
# end class EMailValidator

# Small override class used to 
# shunt the stdout and stderr into
# a wxTextCtrl so it can be saved later from the GUI
class BuildTextShunt:
    def __init__(self, txt_obj):
        self._txt_obj = txt_obj
    def write(self, new_text):
        try:
            self._txt_obj.AppendText(new_text)
        except:
            pass

    def flush(self):
        self._txt_obj.Refresh()