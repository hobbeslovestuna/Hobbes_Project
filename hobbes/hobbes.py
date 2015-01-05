"""
    This is the base Module for the Hobbes Project.
    An Asset Manager cross plateform for both Maya and Nuke.

    Author  : Victor
    Version : 0.1
    Date Last Modification : 05/01/2015
"""

import os

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

    PROJECTS = _PATH_TO_PROJECT
    
    def __init__(self, verbose = False):
        '''
            Init of the class.
            Here we set the main variables we'll need to access
        '''
        
        self._pathProject = PROJECTS
        self.verbose = verbose
    
    
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
        
        for project in os.listdir(self._pathProject):
            fullPath = os.path.join(self._pathProject, project)
            if os.path.isdir(fullPath):
                projects.append(project)
        return projects