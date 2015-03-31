#!/usr/bin/python

import os

cwd=os.getcwd()

## traversal all files in current working dir
def TraverFiles(path):
    for root,dirs,files in os.walk(path):
        for file in files:
            print file

TraverFiles(cwd)
