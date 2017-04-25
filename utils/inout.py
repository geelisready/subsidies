#!/usr/bin/env python
# coding: utf-8

"""
	functions for feature selection
"""
# Author: Geel
import pandas as pd
from pandas import DataFrame, Series
import cPickle as pickle
from datetime import datetime 


## txt的读取
def readTxt2Df(path, splitChar = ','):
    """read txt file to DataFrame without naming columns
        Parameters
        --------
        path : str
            the path of the txt file
        splitChar : str
            the character that splits different columns

        Returns
        --------
        df : DataFrame            
    """
    file = open(path).readlines()
    data= []
    isColumns = 1
    for line in file:
        line = line.replace('\n', '')
        array = line.split(splitChar)
        data.append(array)

    df = DataFrame(data)
    return df

def writeDf2Txt(df, path):
    """save DataFrame as txt file
        Parameters
        --------
        df : DataFrame
            the target object         
        path : str
            the path to save      
    """
    pass


## csv的读取    
def readCsv2Df(path):
    """read csv file to DataFrame without naming columns
        Parameters
        --------
        path : str
            the path of the csv file   
            
        Returns
        --------
        df : DataFrame                
    """
    df = pd.read_csv(path)
    return df
    
def readCsvToList(path):
    """read csv file to List
        Parameters
        --------
        path : str
            the path of the csv file 

        Returns
        --------
        list : List                
    """
	const = open(path).readlines()
	list = []
	for elem in const:
		if elem[0] == 'u':
			continue
		list.append(elem.replace('\n', ''));
	return list
    
def saveToCsv(df, path):
    """read DataFrame as csv
        Parameters
        --------
        df : DataFrame
            the target object        
        path : str
            the path of the txt file
      
    """
	df.to_csv(path, index = False, mode = 'w')

	
    
## 序列化读取    
def saveToPickle(ob, path):
    """serialize object as pkl
        Parameters
        --------
        ob : object
            the target object        
        path : str
            the path of the pkl file
      
    """
	with open(path, 'w') as f: 
		pickle.dump(ob, f)

def readFromPickle(path):
    """read object from pkl
        Parameters
        --------    
        path : str
            the path of the pkl file

        Returns
        --------
        ob : object                
    """
	with open(path, 'r') as f:
		ob = pickle.load(f)
	return ob
		