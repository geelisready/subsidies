#!/usr/bin/env python
# coding: utf-8

"""
    Some work of the wrappers for debug
"""
# Author: Geel
import sys
import os

def timer(func):
    """add a decorator for calculate the processing time of a function
    
    """   
    def wrapper(*args, **kwargs):
        import time as ti
        t0 = ti.time()
        result = func(*args, **kwargs)
        print func.__name__ + ' cost: ' + str(ti.time() - t0)
        return result
        # remember return
    return wrapper