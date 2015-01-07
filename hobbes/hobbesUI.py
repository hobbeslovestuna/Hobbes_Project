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
    inNuke = False
except:
    inNuke = True
import hobbes
# reload(hobbes)

''''def getMayaWindow():
   
   Get the maya main window as a QMainWindow instance
   
   ptr = mui.MQtUtil.mainWindow()
   return shiboken.wrapInstance(long(ptr), QWidget)
'''
class HobbesUI(QWidget):
    '''
        The HobbesUI to manage project both in nuke and Maya
    '''
    def __init__(self, parent = None, verbose = True):
        if not inNuke:
            super(HobbesUI, self).__init__(parent)
        else:
            super(HobbesUI, self).__init__(parent)
        self.verbose = verbose
        self.hobbes = hobbes.Hobbes()        

    
    def _print(self, msg):
        '''
            Verbose for debug
        '''
        if self.verbose:
            print msg

    def ui(self):
        '''
            The UI of the HPM
            2 QBox and one
        '''

        self.version    = '0.1'
        self.title      = 'Hobbes Project Manager '+self.version

        self.setWindowTitle(self.title)
        self.layoutMain = QBoxLayout(QBoxLayout.TopToBottom, self)
        
        #LAYOUT FOR THE PROJECT CHOOSING PART ----------- BEGIN
        self.label      = QLabel('Choose your project ! :')
        self.liste      = QComboBox()
        self.liste.addItems(self.hobbes.getListProjects())

        self.layoutProjects = QHBoxLayout()
        self.layoutProjects.addWidget(self.label)
        self.layoutProjects.addWidget(self.liste)
        #LAYOUT FOR THE PROJECT CHOOSING PART ----------- END

        #LAYOUT FOR THE LIST WIDGET -------------------- BEGIN
        self.listType   = QListWidget(parent = self)
        self.listType.addItems(['Shots', 'Asset'])

        self.listSeq    = QListWidget(parent = self)
        self.listShot   = QListWidget(parent = self)

        self.layoutList = QHBoxLayout()
        self.layoutList.addWidget(self.listType)
        self.layoutList.addWidget(self.listSeq)
        self.layoutList.addWidget(self.listShot)


        #ADDING VARIOUS LAYOUTS TO THE MAIN LAYOUT
        self.layoutMain.addLayout(self.layoutProjects)
        self.layoutMain.addLayout(self.layoutList)

        #CONNECTIONS
        self.connect(self.listType, SIGNAL('itemSelectionChanged()'), self.typeSelected)
        self.show()

    def typeSelected(self):

        for item in self.listType.selectedItems():
            selection = item.text()

        if selection == "Shots":
            self._print'PROJECT : '+str(self.liste.currentText())
            #self.hobbes.listShots(project = )
            #self.listSeq.addItems()