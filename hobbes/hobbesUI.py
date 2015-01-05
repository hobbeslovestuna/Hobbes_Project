"""
    This is the UI Module for the Hobbes Project.
    An Asset Manager cross plateform for both Maya and Nuke.

    Author  : Victor
    Version : 0.1
    Date Last Modification : 05/01/2015
"""

from PySide.QtGui import *
from PySide.QtCore import *
try:
    import maya.OpenMayaUI as mui
    import shiboken
except:
    inNuke = True
import hobbes


def getMayaWindow():
   '''
   Get the maya main window as a QMainWindow instance
   '''
   ptr = mui.MQtUtil.mainWindow()
   return shiboken.wrapInstance(long(ptr), QWidget)

class HobbesUI(QWidget):
    '''
        The HobbesUI to manage project both in nuke and Maya
    '''
    def __init__(self, parent=getMayaWindow()):
        if not inNuke:
            super(HobbesUI).__init__(parent)
        else:
            super(HobbesUI).__init__()