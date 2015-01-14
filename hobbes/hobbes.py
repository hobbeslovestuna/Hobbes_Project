"""
    This is the base Module for the Hobbes Project.
    An Asset Manager cross plateform for both Maya and Nuke.

    Author  : Victor
    Version : 0.1
    Date Last Modification : 05/01/2015
"""

import os
import re
#Check if launched in Nuke or Maya
try:
    import nuke
    inNuke = True
except:
    inNuke = False

try:
    import maya.cmds as cmds
    inMaya = True
except:
    inMaya = False

_PATH_TO_PROJECT = os.path.join('/home/victor/', 'PROJECTS/')

class Hobbes(object):
    '''
        The Main class for loading assets, saving and versionning files
    '''
    #PROJECTS -- Class Attributes to access directory structure
    PROJECTS    = _PATH_TO_PROJECT
    COMP        = 'COMP'
    _3D         = '3D'
    RENDER      = 'RENDER'
    SHOTS       = 'SHOTS'
    ASSETS       = 'ASSETS'

    def __init__(self, verbose = True):
        '''
            Init of the class.
            Here we set the main variables we'll need to access
        '''
        
        # self._pathProject = self.PROJECTS
        self.verbose = verbose
        self._print('In Nuke : '+str(inNuke))
        self._print('In Maya : '+str(inMaya))
    
    
    def _print(self, msg):
        '''
            A method to print output only if verbose is True
        '''
        if self.verbose:
            print msg

    def getListProjects(self):
        '''
            Getting allr the projects in the folder, to help build the UI and to load assets
        '''
        projects = []

        for project in os.listdir(self.PROJECTS):
            #We build the complete path to access the Project and we check if it's a dir or not, if yes then it's a Project according to our standards
            fullPath = os.path.join(self.PROJECTS, project)
            if os.path.isdir(fullPath):
                projects.append(project)
        projects.sort()
        print projects
        print '_'*10
        return projects

    def loadFile(self, path):
        '''
            LoadFile : 
                Will try to lad the file given in param.
        '''
        if inNuke:
            print 'yeah'
            #nukescriptOpen(path of the script)
        elif inMaya:
            filePath = ''
        else:
            self._print('You must launch the tool from Nuke or Maya')

    def listShots(self, path = PROJECTS, project = None ):
        '''
            List the files from a given path and returns them
        '''
        listshots = []
        if inNuke:
            pathToProj = os.path.join(path, project)
            pathToShots = os.path.join(pathToProj, self.SHOTS, self.COMP)
            self._print(pathToShots)
            try:
                listshots = os.listdir(pathToShots)
            except:
                self._print("Error retriving the project's shots")
        elif inMaya:
            pathToProj = os.path.join(path, project)
            pathToShots = os.path.join(pathToProj, self.SHOTS, self._3D)
            self._print(pathToShots)
            try:
                listshots = os.listdir(pathToShots)
            except:
                self._print("Error retriving the project's shots")

        return listshots

    def listAssets(self, path = PROJECTS, project = None):
        '''
            List the assests from a given path and returns them
        '''
        listassets = []
        if inNuke:
            pathToProj = os.path.join(path, project)
            pathToShots = os.path.join(pathToProj, self.ASSETS)
            self._print(pathToShots)
            try:
                listassets = os.listdir(pathToShots)
            except:
                self._print("Error retriving the project's shots")
        elif inMaya:
            pathToProj = os.path.join(path, project)
            pathToShots = os.path.join(pathToProj, self.ASSETS)
            self._print(pathToShots)
            try:
                listassets = os.listdir(pathToShots)
            except:
                self._print("Error retriving the project's shots")

        print listassets
        print '---'
        return listassets

    def listFiles(self, shots = False, assets = False, proj = None, types = None, selection = None):
        '''
            Returns a list of file based on a path given
        '''
        listFile = []
        if inNuke:
            pathToProj = os.path.join(self.PROJECTS, proj)
            if shots:
                pathToFiles = os.path.join(pathToProj, self.SHOTS, self.COMP, selection)
                self._print(pathToFiles)
            elif assets:
                pathtoFiles = os.path.join(pathToProj, self.SHOTS, self._3D, selection)
            listFile = os.listdir(pathToFiles)
        
        elif inMaya:
            pathToProj = os.path.join(self.PROJECTS, proj)
            if shots:
                pathToFiles = os.path.join(pathToProj, self.SHOTS, self._3D, selection)
            listFile = os.listdir(pathToFiles)

        return listFile

    def getPath(self, project, type, shot, file):
        path = ''
        if inNuke:
            if type == 'Shots':
                path = os.path.join(self.PROJECTS, project, self.SHOTS, self.COMP, shot, file)
            elif type == 'Asset':
                path = os.path.join(self.PROJECTS, project, self.ASSETS, shot, file)
        elif inMaya:
            if type == 'Shots':
                path = os.path.join(self.PROJECTS, project, self.SHOTS, self._3D, shot, file)
        return path

    def versionIt(self, path):
        '''
            A methods that returns a path with the new version of the file
        '''
        root, fileName = os.path.split(path)
        if inNuke:
            if not re.match('v[0-9]*', fileName):
                self._print('Wrong file format')
# h = Hobbes()
# h.loadFile()