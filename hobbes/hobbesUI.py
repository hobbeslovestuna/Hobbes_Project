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
    import maya.cmds as cmds
    inNuke = False
    inMaya = True
except:
    inNuke = True
    import nuke
import hobbes
reload(hobbes)

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

        self.listTwo     = QListWidget(parent = self)
        self.listThree   = QListWidget(parent = self)

        self.layoutList = QHBoxLayout()
        self.layoutList.addWidget(self.listType)
        self.layoutList.addWidget(self.listTwo)
        self.layoutList.addWidget(self.listThree)

        #BUTTONS TO LOAD/SAVE/CLOSE
        self.load_btn   = QPushButton('Load Scene/Asset')
        self.save_btn   = QPushButton('Save Scene/Asset')
        self.close_btn  = QPushButton('Close')

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.addWidget(self.load_btn)
        self.buttonLayout.addWidget(self.save_btn)
        self.buttonLayout.addWidget(self.close_btn)

        #ADDING VARIOUS LAYOUTS TO THE MAIN LAYOUT
        self.layoutMain.addLayout(self.layoutProjects)
        self.layoutMain.addLayout(self.layoutList)
        self.layoutMain.addLayout(self.buttonLayout)

        #CONNECTIONS
        self.connect(self.liste, SIGNAL('currentIndexChanged(QString)'), self.updateProject)
        self.connect(self.listType, SIGNAL('itemSelectionChanged()'), self.updateTwo)
        self.connect(self.listTwo, SIGNAL('itemSelectionChanged()'), self.updateThree)
        self.connect(self.load_btn, SIGNAL('clicked()'), self.loadFile)
        self.connect(self.close_btn, SIGNAL('clicked()'), self.close)
        # self.liste.currentIndexChanged['QString'].connect(self.updateProject)
        self.show()

    def updateProject(self):
        '''
            Update the UI based on the project selected
        '''
        self.listTwo.clear()
        self.listThree.clear()
        print 

    def updateTwo(self):
        '''
            Based on what is selected in listType, we update the second column
        '''
        self.listThree.clear()
        self.listTwo.clear()

        for item in self.listType.selectedItems():
            selection = item.text()

        if selection == 'Shots':
            self._print('PROJECT : '+str(self.liste.currentText()))
            self.shots = self.hobbes.listShots(project = self.liste.currentText())
            #self.hobbes.listShots(project = )
            self.listTwo.addItems(self.shots)
        elif selection == 'Asset':
            self._print('PROJECT : '+str(self.liste.currentText()))
            self.assets = self.hobbes.listAssets(project = self.liste.currentText())
            self.listTwo.addItems(self.assets)
    
    def updateThree(self):
        '''
            Updates the third column of the UI
        '''
        self.listThree.clear()

        selection = self.listTwo.currentItem().text()
        types = self.listType.currentItem().text()

        if types == 'Shots':
            files = self.hobbes.listFiles(shots = True, proj = self.liste.currentText(), types = types, selection = selection)
            self.listThree.addItems(files)
        elif types == 'Asset':
            #files = self.hobbes.listFilesAsset()
            pass
        self.hobbes.getPath
    
    def loadFile(self):
        '''
            Opens a nuke openNukeScript
        '''
        typ = self.listType.currentItem().text()#itemSelected()[0].text()
        shot = self.listTwo.currentItem().text()
        fil = self.listThree.currentItem().text()
        path = self.hobbes.getPath(self.liste.currentText(), typ, shot, fil)
        print path
        if inNuke:
            nuke.scriptOpen(path)
        elif inMaya:
            print 'Opening : '+path
            cmds.file(path, o = True)