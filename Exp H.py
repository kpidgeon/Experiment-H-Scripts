# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 18:21:45 2018

#@author: kyle"""

#For extracting pressure make sure data file is in same directory
#as this script.
#
#
#

def isFloat(string):
    try:
        float(string)
    except ValueError:
        return False
    return True

def extractPressure(readFile, writeFile):
    values, towrite = [], ""

    with open(readFile) as f:
        for line in f:
            for indStr in line.split():
                if (len(indStr) == 5 and "." in indStr
                    and not indStr.isalpha() and isFloat(indStr)):
                    if "\n" in indStr:
                        indStr.replace("\n", "")
                values.append(indStr)

    for val in values:
        towrite += val + "\n"

    with open(writeFile, "w") as t:
        t.write(towrite)
    
