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

PATH_TO_PROJECT = '/home/victor/PROJECTS/'

class Hobbes(object):
    '''
        The Main class for loading assets, saving and versionning files
    '''

    def __init__(self):
        '''
            Init of the class.
            Here we set the main variables we'll need to access
        '''
        
        self._pathProject = PATH_TO_PROJECT
