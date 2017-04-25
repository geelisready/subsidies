#!/usr/bin/env python
# coding: utf-8

"""
    Some work of os handle 
"""
# Author: Geel
import sys
import os

def unload(moduleName):
    """unload a module
        moduleName : 
            module name; for example: unload(pandas)
     """
    del sys.modules[moduleName]


def getDir(nLevel, file):
    """get all file names under the directory
        Parameters
        --------
        nLevel : str
            the recursive level of the directory, the expected nLevel shouid be larger than 0
        file : str
            you should imput __file__, which is the file name of the current module
            
        Returns
        --------
        path : str
    """   
    path = os.path.dirname(file)
    for i in range(nLevel - 1):
        path = os.path.dirname(path)
    path = path.replace('\\', '/')
    return path
    
def getAllFilenameUnderThisDir(dir):
    """get all file names under the directory
        Parameters
        --------
        dir : str
            the directory

        Returns
        --------
        fileNames : List                
    """   
    names = os.listdir(dir)
    fileNames = []
    for elem in names:
        if os.path.isfile(dir + '/' + elem) == True:
            fileNames.append(elem)    
    return fileNames


    
if __name__ == '__main__':
    # dir = getDir(__file__, 3) + "/dataset/"
    dir = getDir(1, __file__)
    for filename in getAllFilenameUnderThisDir(dir):
        print(filename)