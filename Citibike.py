#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 13:27:13 2017

@author: JC
"""
import csv
import math
#from datetime import time
import time
from collections import Counter
from collections import defaultdict

############# Pre-Process the data #############

def preProcessData(inputFile,outputFile):
    with (open(outputFile,'w+')) as _output:
        writer=csv.writer(_output,delimiter=',')
        with(open(inputFile,'r')) as _input:
            reader=csv.reader(_input,delimiter=',')
            for row in reader:
                for index in range(len(row)):
                    if row[index] in ['T','yes']:
                        row[index]='1'
                    elif row[index] in ['A','no']:
                        row[index]='0'                                        
                #print(row)
                writer.writerow(row)
    return
        
"""
############# CSV loading function #############

def loadCsv(filename):
    #lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",", quotechar='\'')
    lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",",quotechar = None,quoting = csv.QUOTE_NONE)
    dataset=[]
    i=0
    for row in lines:
        #if i!=0:
            for index in range(len(row)):
                row[index] =int(row[index])
                dataset.append(row)
        #i=i+1
    print(i)
    return dataset
"""
def loadCsv(filename):
    #lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",", quotechar='\'')
    lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",",quotechar = None,quoting = csv.QUOTE_NONE)
    dataset=[]
    i=0
    for row in lines: #through samples
        if row is None:
            print("NULL detected")
        if i !=0:
            selectRow=[]
            #print(row[14])
            for index in range(len(row)): #through columns
                #print(row[index])
                if index in [0,3,7,11]:
                    selectRow.append(int(row[index]))
                elif index in [12]:
                    if row[index] in ['Subscriber']:
                        #print(row[index])
                        row[index]=1
                    elif row[index] in ['Customer']:
                        #print(row[index])
                        row[index]=0
                    else:
                        row[index]=2            
                    selectRow.append(int(row[index]))
                if index in [13]:
                    if row[index] in ['']:
                        row[index]=0
                    selectRow.append(int(row[index]))
                        #print("row[index] is None")
                elif index in [14]:
                    selectRow.append(int(row[index]))
                    
            dataset.append(selectRow)
        i=i+1
    #print(dataset[-1])
    #del dataset[-1]
    #print(len(dataset))
    #print(dataset)
    print(len(dataset))
    #print(i)
    return dataset

def loadMultipleCsv(file1,file2):
    dataset=loadCsvClassified(file1)
    dataset2=loadCsvClassified(file2)
    for sample in dataset2:
        dataset.append(sample)
    return dataset

def appendToDataset(dataset,appendFile):
    appendset=loadCsvClassified(appendFile)
    for sample in appendset:
        dataset.append(sample)
    return dataset

def appendToDatasetNaiveAge(dataset,appendFile):
    #appendset=loadCsvClassified(appendFile)
    appendset=loadCsvClassifiedNaiveAge(appendFile)
    for sample in appendset:
        dataset.append(sample)
    return dataset

def appendToDatasetNaiveEnd(dataset,appendFile):
    #appendset=loadCsvClassified(appendFile)
    appendset=loadCsvClassifiedNaiveEnd(appendFile)
    for sample in appendset:
        dataset.append(sample)
    return dataset

def appendToDatasetNaiveStart(dataset,appendFile):
    #appendset=loadCsvClassified(appendFile)
    appendset=loadCsvClassifiedNaiveStart(appendFile)
    for sample in appendset:
        dataset.append(sample)
    return dataset

def appendToDatasetNoHour(dataset,appendFile):
    #appendset=loadCsvClassified(appendFile)
    appendset=loadCsvClassifiedNoHour(appendFile)
    for sample in appendset:
        dataset.append(sample)
    return dataset

def appendToDatasetNoGender(dataset,appendFile):
    #appendset=loadCsvClassified(appendFile)
    appendset=loadCsvClassifiedNoGender(appendFile)
    for sample in appendset:
        dataset.append(sample)
    return dataset

    
def loadCsvClassified(filename):
    #lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",", quotechar='\'')
    lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",",quotechar = None,quoting = csv.QUOTE_NONE)
    dataset=[]
    i=0
    for row in lines: #through samples
        if row is None:
            print("NULL detected")
        if i !=0:
            selectRow=[]
            for index in range(len(row)): #through columns
                #print(row[index])                       
                if index in [0]:
                    if int(row[index]) < 60:
                        row[index]=1
                    elif (int(row[index]) >= 60) and (int(row[index]) < 120):
                        row[index]=2
                    elif (int(row[index]) >= 120) and (int(row[index]) < 180):
                        row[index]=3
                    elif (int(row[index]) >= 180) and (int(row[index]) < 240):
                        row[index]=4
                    elif (int(row[index]) >= 240) and (int(row[index]) < 300):
                        row[index]=5
                    elif (int(row[index]) >= 300) and (int(row[index]) < 360):
                        row[index]=6
                    elif (int(row[index]) >= 360) and (int(row[index]) < 420):
                        row[index]=7
                    elif (int(row[index]) >= 420) and (int(row[index]) < 480):
                        row[index]=8
                    elif (int(row[index]) >= 480) and (int(row[index]) < 540):
                        row[index]=9
                    elif (int(row[index]) >= 540) and (int(row[index]) < 600):
                        row[index]=10
                    elif (int(row[index]) >= 600) and (int(row[index]) < 660):
                        row[index]=11
                    elif (int(row[index]) >= 660) and (int(row[index]) < 720):
                        row[index]=12
                    elif (int(row[index]) >= 720) and (int(row[index]) < 780):
                        row[index]=13
                    elif (int(row[index]) >= 780) and (int(row[index]) < 840):
                        row[index]=14
                    elif (int(row[index]) >= 840) and (int(row[index]) < 900):
                        row[index]=15
                    elif (int(row[index]) >= 900) and (int(row[index]) < 960):
                        row[index]=16
                    elif (int(row[index]) >= 960) and (int(row[index]) < 1020):
                        row[index]=17
                    elif (int(row[index]) >= 1020) and (int(row[index]) < 1080):
                        row[index]=18
                    elif (int(row[index]) >= 1080) and (int(row[index]) < 1140):
                        row[index]=19
                    elif (int(row[index]) >= 1140) and (int(row[index]) < 1200):
                        row[index]=20
                    elif (int(row[index]) >= 1200) and (int(row[index]) < 1260):
                        row[index]=21
                    elif (int(row[index]) >= 1260) and (int(row[index]) < 1320):
                        row[index]=22
                    elif (int(row[index]) >= 1320) and (int(row[index]) < 1380):
                        row[index]=23
                    elif (int(row[index]) >= 1380) and (int(row[index]) < 1440):
                        row[index]=24
                    elif (int(row[index]) >= 1440) and (int(row[index]) < 1500):
                        row[index]=25
                    elif (int(row[index]) >= 1500) and (int(row[index]) < 1560):
                        row[index]=26
                    elif (int(row[index]) >= 1560) and (int(row[index]) < 1620):
                        row[index]=27
                    elif (int(row[index]) >= 1620) and (int(row[index]) < 1680):
                        row[index]=28
                    elif (int(row[index]) >= 1680) and (int(row[index]) < 1740):
                        row[index]=29
                    elif (int(row[index]) >= 1740) and (int(row[index]) < 1800):
                        row[index]=30
                    elif (int(row[index]) >= 1800) and (int(row[index]) < 1860):
                        row[index]=31
                    elif (int(row[index]) >= 1860) and (int(row[index]) < 1920):
                        row[index]=32
                    elif (int(row[index]) >= 1920) and (int(row[index]) < 1980):
                        row[index]=33
                    elif (int(row[index]) >= 1980) and (int(row[index]) < 2040):
                        row[index]=34
                    elif (int(row[index]) >= 2040) and (int(row[index]) < 2100):
                        row[index]=35
                    elif (int(row[index]) >= 2100) and (int(row[index]) < 2160):
                        row[index]=36
                    elif (int(row[index]) >= 2160) and (int(row[index]) < 2220):
                        row[index]=37
                    elif (int(row[index]) >= 2220) and (int(row[index]) < 2280):
                        row[index]=38
                    elif (int(row[index]) >= 2280) and (int(row[index]) < 2340):
                        row[index]=39
                    elif (int(row[index]) >= 2340) and (int(row[index]) < 2400):
                        row[index]=40
                    elif (int(row[index]) >= 2400) and (int(row[index]) < 2460):
                        row[index]=41
                    else:
                        row[index]=42
                    selectRow.append(int(row[index]))
                if index in [1]:#time.strptime("2016-12-01 07:35:17","%Y-%m-%d %H:%M:%S")
                    #print(row[index])
                    theTime=time.strptime(row[index],"%Y-%m-%d %H:%M:%S")
                    #print(theTime.tm_hour)
                    if theTime.tm_hour < 2:
                        row[index]=1
                    elif theTime.tm_hour >= 2 and theTime.tm_hour < 4:
                        row[index]=3
                    elif theTime.tm_hour >= 4 and theTime.tm_hour < 6:
                        row[index]=5
                    elif theTime.tm_hour >= 6 and theTime.tm_hour < 8:
                        row[index]=7
                    elif theTime.tm_hour >= 8 and theTime.tm_hour < 10:
                        row[index]=9
                    elif theTime.tm_hour >= 10 and theTime.tm_hour < 12:
                        row[index]=11
                    elif theTime.tm_hour >= 12 and theTime.tm_hour < 14:
                        row[index]=13
                    elif theTime.tm_hour >= 14 and theTime.tm_hour < 16:
                        row[index]=15
                    elif theTime.tm_hour >= 16 and theTime.tm_hour < 18:
                        row[index]=17
                    elif theTime.tm_hour >= 18 and theTime.tm_hour < 20:
                        row[index]=19
                    elif theTime.tm_hour >= 20 and theTime.tm_hour < 22:
                        row[index]=21
                    elif theTime.tm_hour >= 22 and theTime.tm_hour < 24:
                        row[index]=23
                    #if time(row[index]) < time(07):
                    #    print("time success") 
                    selectRow.append(int(row[index]))
                if index in [3]:
                    selectRow.append(int(row[index]))
                if index in [7]:
                    selectRow.append(int(row[index]))
                if index in [12]:
                    if row[index] in ['Subscriber']:
                        #print(row[index])
                        row[index]=1
                    elif row[index] in ['Customer']:
                        #print(row[index])
                        row[index]=0
                    else:
                        row[index]=2            
                    selectRow.append(int(row[index]))
                if index in [13]:
                    if row[index] in ['']:
                        row[index]=0
                        age=0
                    elif int(row[index]) > 2011:
                        age=3
                    elif (int(row[index]) > 2006) and (int(row[index]) <= 2011):
                        age=8
                    elif (int(row[index]) > 2001) and (int(row[index]) <= 2006):
                        age=13
                    elif (int(row[index]) > 1996) and (int(row[index]) <= 2001):
                        age=18
                    elif (int(row[index]) > 1991) and (int(row[index]) <= 1996):
                        age=23
                    elif (int(row[index]) > 1986) and (int(row[index]) <= 1991):
                        age=28
                    elif (int(row[index]) > 1981) and (int(row[index]) <= 1986):
                        age=33
                    elif (int(row[index]) > 1976) and (int(row[index]) <= 1981):
                        age=38
                    elif (int(row[index]) > 1971) and (int(row[index]) <= 1976):
                        age=43
                    elif (int(row[index]) > 1966) and (int(row[index]) <= 1971):
                        age=48
                    elif (int(row[index]) > 1961) and (int(row[index]) <= 1966):
                        age=53
                    elif (int(row[index]) > 1956) and (int(row[index]) <= 1961):
                        age=58
                    elif (int(row[index]) > 1951) and (int(row[index]) <= 1956):
                        age=63
                    elif (int(row[index]) > 1946) and (int(row[index]) <= 1951):
                        age=68
                    elif (int(row[index]) > 1941) and (int(row[index]) <= 1946):
                        age=73
                    elif (int(row[index]) > 1936) and (int(row[index]) <= 1941):
                        age=78
                    elif (int(row[index]) > 1931) and (int(row[index]) <= 1936):
                        age=83
                    elif (int(row[index]) > 1926) and (int(row[index]) <= 1931):
                        age=88
                    elif (int(row[index]) > 1921) and (int(row[index]) <= 1926):
                        age=93
                    elif (int(row[index]) > 1916) and (int(row[index]) <= 1921):
                        age=98
                    selectRow.extend([age])
                if index in [14]:
                    selectRow.append(int(row[index]))

            dataset.append(selectRow)
        i=i+1
    #print(dataset[-1])
    #del dataset[-1]
    #print(len(dataset))
    #print(dataset)
    #print(len(dataset))
    #print(i)
    return dataset

def loadCsvClassifiedNaiveAge(filename):
    #lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",", quotechar='\'')
    lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",",quotechar = None,quoting = csv.QUOTE_NONE)
    dataset=[]
    i=0
    for row in lines: #through samples
        if row is None:
            print("NULL detected")
        if i !=0:
            selectRow=[]
            for index in range(len(row)): #through columns
                #print(row[index])                       
                if index in [0]:
                    if int(row[index]) < 60:
                        row[index]=1
                    elif (int(row[index]) >= 60) and (int(row[index]) < 120):
                        row[index]=2
                    elif (int(row[index]) >= 120) and (int(row[index]) < 180):
                        row[index]=3
                    elif (int(row[index]) >= 180) and (int(row[index]) < 240):
                        row[index]=4
                    elif (int(row[index]) >= 240) and (int(row[index]) < 300):
                        row[index]=5
                    elif (int(row[index]) >= 300) and (int(row[index]) < 360):
                        row[index]=6
                    elif (int(row[index]) >= 360) and (int(row[index]) < 420):
                        row[index]=7
                    elif (int(row[index]) >= 420) and (int(row[index]) < 480):
                        row[index]=8
                    elif (int(row[index]) >= 480) and (int(row[index]) < 540):
                        row[index]=9
                    elif (int(row[index]) >= 540) and (int(row[index]) < 600):
                        row[index]=10
                    elif (int(row[index]) >= 600) and (int(row[index]) < 660):
                        row[index]=11
                    elif (int(row[index]) >= 660) and (int(row[index]) < 720):
                        row[index]=12
                    elif (int(row[index]) >= 720) and (int(row[index]) < 780):
                        row[index]=13
                    elif (int(row[index]) >= 780) and (int(row[index]) < 840):
                        row[index]=14
                    elif (int(row[index]) >= 840) and (int(row[index]) < 900):
                        row[index]=15
                    elif (int(row[index]) >= 900) and (int(row[index]) < 960):
                        row[index]=16
                    elif (int(row[index]) >= 960) and (int(row[index]) < 1020):
                        row[index]=17
                    elif (int(row[index]) >= 1020) and (int(row[index]) < 1080):
                        row[index]=18
                    elif (int(row[index]) >= 1080) and (int(row[index]) < 1140):
                        row[index]=19
                    elif (int(row[index]) >= 1140) and (int(row[index]) < 1200):
                        row[index]=20
                    elif (int(row[index]) >= 1200) and (int(row[index]) < 1260):
                        row[index]=21
                    elif (int(row[index]) >= 1260) and (int(row[index]) < 1320):
                        row[index]=22
                    elif (int(row[index]) >= 1320) and (int(row[index]) < 1380):
                        row[index]=23
                    elif (int(row[index]) >= 1380) and (int(row[index]) < 1440):
                        row[index]=24
                    elif (int(row[index]) >= 1440) and (int(row[index]) < 1500):
                        row[index]=25
                    elif (int(row[index]) >= 1500) and (int(row[index]) < 1560):
                        row[index]=26
                    elif (int(row[index]) >= 1560) and (int(row[index]) < 1620):
                        row[index]=27
                    elif (int(row[index]) >= 1620) and (int(row[index]) < 1680):
                        row[index]=28
                    elif (int(row[index]) >= 1680) and (int(row[index]) < 1740):
                        row[index]=29
                    elif (int(row[index]) >= 1740) and (int(row[index]) < 1800):
                        row[index]=30
                    elif (int(row[index]) >= 1800) and (int(row[index]) < 1860):
                        row[index]=31
                    elif (int(row[index]) >= 1860) and (int(row[index]) < 1920):
                        row[index]=32
                    elif (int(row[index]) >= 1920) and (int(row[index]) < 1980):
                        row[index]=33
                    elif (int(row[index]) >= 1980) and (int(row[index]) < 2040):
                        row[index]=34
                    elif (int(row[index]) >= 2040) and (int(row[index]) < 2100):
                        row[index]=35
                    elif (int(row[index]) >= 2100) and (int(row[index]) < 2160):
                        row[index]=36
                    elif (int(row[index]) >= 2160) and (int(row[index]) < 2220):
                        row[index]=37
                    elif (int(row[index]) >= 2220) and (int(row[index]) < 2280):
                        row[index]=38
                    elif (int(row[index]) >= 2280) and (int(row[index]) < 2340):
                        row[index]=39
                    elif (int(row[index]) >= 2340) and (int(row[index]) < 2400):
                        row[index]=40
                    elif (int(row[index]) >= 2400) and (int(row[index]) < 2460):
                        row[index]=41
                    else:
                        row[index]=42
                    selectRow.append(int(row[index]))
                if index in [1]:#time.strptime("2016-12-01 07:35:17","%Y-%m-%d %H:%M:%S")
                    #print(row[index])
                    theTime=time.strptime(row[index],"%Y-%m-%d %H:%M:%S")
                    #print(theTime.tm_hour)
                    if theTime.tm_hour < 2:
                        row[index]=1
                    elif theTime.tm_hour >= 2 and theTime.tm_hour < 4:
                        row[index]=3
                    elif theTime.tm_hour >= 4 and theTime.tm_hour < 6:
                        row[index]=5
                    elif theTime.tm_hour >= 6 and theTime.tm_hour < 8:
                        row[index]=7
                    elif theTime.tm_hour >= 8 and theTime.tm_hour < 10:
                        row[index]=9
                    elif theTime.tm_hour >= 10 and theTime.tm_hour < 12:
                        row[index]=11
                    elif theTime.tm_hour >= 12 and theTime.tm_hour < 14:
                        row[index]=13
                    elif theTime.tm_hour >= 14 and theTime.tm_hour < 16:
                        row[index]=15
                    elif theTime.tm_hour >= 16 and theTime.tm_hour < 18:
                        row[index]=17
                    elif theTime.tm_hour >= 18 and theTime.tm_hour < 20:
                        row[index]=19
                    elif theTime.tm_hour >= 20 and theTime.tm_hour < 22:
                        row[index]=21
                    elif theTime.tm_hour >= 22 and theTime.tm_hour < 24:
                        row[index]=23
                    #if time(row[index]) < time(07):
                    #    print("time success") 
                    selectRow.append(int(row[index]))
                if index in [3]:
                    selectRow.append(int(row[index]))
                if index in [7]:
                    selectRow.append(int(row[index]))
                if index in [12]:
                    if row[index] in ['Subscriber']:
                        #print(row[index])
                        row[index]=1
                    elif row[index] in ['Customer']:
                        #print(row[index])
                        row[index]=0
                    else:
                        row[index]=2            
                    selectRow.append(int(row[index]))
                if index in [14]:
                    selectRow.append(int(row[index]))
            for index in range(len(row)): #through columns                    
                if index in [13]:
                    if row[index] in ['']:
                        row[index]=0
                        age=0
                    elif int(row[index]) > 2011:
                        age=3
                    elif (int(row[index]) > 2006) and (int(row[index]) <= 2011):
                        age=8
                    elif (int(row[index]) > 2001) and (int(row[index]) <= 2006):
                        age=13
                    elif (int(row[index]) > 1996) and (int(row[index]) <= 2001):
                        age=18
                    elif (int(row[index]) > 1991) and (int(row[index]) <= 1996):
                        age=23
                    elif (int(row[index]) > 1986) and (int(row[index]) <= 1991):
                        age=28
                    elif (int(row[index]) > 1981) and (int(row[index]) <= 1986):
                        age=33
                    elif (int(row[index]) > 1976) and (int(row[index]) <= 1981):
                        age=38
                    elif (int(row[index]) > 1971) and (int(row[index]) <= 1976):
                        age=43
                    elif (int(row[index]) > 1966) and (int(row[index]) <= 1971):
                        age=48
                    elif (int(row[index]) > 1961) and (int(row[index]) <= 1966):
                        age=53
                    elif (int(row[index]) > 1956) and (int(row[index]) <= 1961):
                        age=58
                    elif (int(row[index]) > 1951) and (int(row[index]) <= 1956):
                        age=63
                    elif (int(row[index]) > 1946) and (int(row[index]) <= 1951):
                        age=68
                    elif (int(row[index]) > 1941) and (int(row[index]) <= 1946):
                        age=73
                    elif (int(row[index]) > 1936) and (int(row[index]) <= 1941):
                        age=78
                    elif (int(row[index]) > 1931) and (int(row[index]) <= 1936):
                        age=83
                    elif (int(row[index]) > 1926) and (int(row[index]) <= 1931):
                        age=88
                    elif (int(row[index]) > 1921) and (int(row[index]) <= 1926):
                        age=93
                    elif (int(row[index]) > 1916) and (int(row[index]) <= 1921):
                        age=98
                    selectRow.extend([age])

            dataset.append(selectRow)
        i=i+1
    return dataset

def loadCsvClassifiedNaiveEnd(filename):
    #lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",", quotechar='\'')
    lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",",quotechar = None,quoting = csv.QUOTE_NONE)
    dataset=[]
    i=0
    for row in lines: #through samples
        if row is None:
            print("NULL detected")
        if i !=0:
            selectRow=[]
            for index in range(len(row)): #through columns
                #print(row[index])                       
                if index in [0]:
                    if int(row[index]) < 60:
                        row[index]=1
                    elif (int(row[index]) >= 60) and (int(row[index]) < 120):
                        row[index]=2
                    elif (int(row[index]) >= 120) and (int(row[index]) < 180):
                        row[index]=3
                    elif (int(row[index]) >= 180) and (int(row[index]) < 240):
                        row[index]=4
                    elif (int(row[index]) >= 240) and (int(row[index]) < 300):
                        row[index]=5
                    elif (int(row[index]) >= 300) and (int(row[index]) < 360):
                        row[index]=6
                    elif (int(row[index]) >= 360) and (int(row[index]) < 420):
                        row[index]=7
                    elif (int(row[index]) >= 420) and (int(row[index]) < 480):
                        row[index]=8
                    elif (int(row[index]) >= 480) and (int(row[index]) < 540):
                        row[index]=9
                    elif (int(row[index]) >= 540) and (int(row[index]) < 600):
                        row[index]=10
                    elif (int(row[index]) >= 600) and (int(row[index]) < 660):
                        row[index]=11
                    elif (int(row[index]) >= 660) and (int(row[index]) < 720):
                        row[index]=12
                    elif (int(row[index]) >= 720) and (int(row[index]) < 780):
                        row[index]=13
                    elif (int(row[index]) >= 780) and (int(row[index]) < 840):
                        row[index]=14
                    elif (int(row[index]) >= 840) and (int(row[index]) < 900):
                        row[index]=15
                    elif (int(row[index]) >= 900) and (int(row[index]) < 960):
                        row[index]=16
                    elif (int(row[index]) >= 960) and (int(row[index]) < 1020):
                        row[index]=17
                    elif (int(row[index]) >= 1020) and (int(row[index]) < 1080):
                        row[index]=18
                    elif (int(row[index]) >= 1080) and (int(row[index]) < 1140):
                        row[index]=19
                    elif (int(row[index]) >= 1140) and (int(row[index]) < 1200):
                        row[index]=20
                    elif (int(row[index]) >= 1200) and (int(row[index]) < 1260):
                        row[index]=21
                    elif (int(row[index]) >= 1260) and (int(row[index]) < 1320):
                        row[index]=22
                    elif (int(row[index]) >= 1320) and (int(row[index]) < 1380):
                        row[index]=23
                    elif (int(row[index]) >= 1380) and (int(row[index]) < 1440):
                        row[index]=24
                    elif (int(row[index]) >= 1440) and (int(row[index]) < 1500):
                        row[index]=25
                    elif (int(row[index]) >= 1500) and (int(row[index]) < 1560):
                        row[index]=26
                    elif (int(row[index]) >= 1560) and (int(row[index]) < 1620):
                        row[index]=27
                    elif (int(row[index]) >= 1620) and (int(row[index]) < 1680):
                        row[index]=28
                    elif (int(row[index]) >= 1680) and (int(row[index]) < 1740):
                        row[index]=29
                    elif (int(row[index]) >= 1740) and (int(row[index]) < 1800):
                        row[index]=30
                    elif (int(row[index]) >= 1800) and (int(row[index]) < 1860):
                        row[index]=31
                    elif (int(row[index]) >= 1860) and (int(row[index]) < 1920):
                        row[index]=32
                    elif (int(row[index]) >= 1920) and (int(row[index]) < 1980):
                        row[index]=33
                    elif (int(row[index]) >= 1980) and (int(row[index]) < 2040):
                        row[index]=34
                    elif (int(row[index]) >= 2040) and (int(row[index]) < 2100):
                        row[index]=35
                    elif (int(row[index]) >= 2100) and (int(row[index]) < 2160):
                        row[index]=36
                    elif (int(row[index]) >= 2160) and (int(row[index]) < 2220):
                        row[index]=37
                    elif (int(row[index]) >= 2220) and (int(row[index]) < 2280):
                        row[index]=38
                    elif (int(row[index]) >= 2280) and (int(row[index]) < 2340):
                        row[index]=39
                    elif (int(row[index]) >= 2340) and (int(row[index]) < 2400):
                        row[index]=40
                    elif (int(row[index]) >= 2400) and (int(row[index]) < 2460):
                        row[index]=41
                    else:
                        row[index]=42
                    selectRow.append(int(row[index]))
                if index in [1]:#time.strptime("2016-12-01 07:35:17","%Y-%m-%d %H:%M:%S")
                    #print(row[index])
                    theTime=time.strptime(row[index],"%Y-%m-%d %H:%M:%S")
                    #print(theTime.tm_hour)
                    if theTime.tm_hour < 2:
                        row[index]=1
                    elif theTime.tm_hour >= 2 and theTime.tm_hour < 4:
                        row[index]=3
                    elif theTime.tm_hour >= 4 and theTime.tm_hour < 6:
                        row[index]=5
                    elif theTime.tm_hour >= 6 and theTime.tm_hour < 8:
                        row[index]=7
                    elif theTime.tm_hour >= 8 and theTime.tm_hour < 10:
                        row[index]=9
                    elif theTime.tm_hour >= 10 and theTime.tm_hour < 12:
                        row[index]=11
                    elif theTime.tm_hour >= 12 and theTime.tm_hour < 14:
                        row[index]=13
                    elif theTime.tm_hour >= 14 and theTime.tm_hour < 16:
                        row[index]=15
                    elif theTime.tm_hour >= 16 and theTime.tm_hour < 18:
                        row[index]=17
                    elif theTime.tm_hour >= 18 and theTime.tm_hour < 20:
                        row[index]=19
                    elif theTime.tm_hour >= 20 and theTime.tm_hour < 22:
                        row[index]=21
                    elif theTime.tm_hour >= 22 and theTime.tm_hour < 24:
                        row[index]=23
                    #if time(row[index]) < time(07):
                    #    print("time success") 
                    selectRow.append(int(row[index]))
                if index in [3]:
                    selectRow.append(int(row[index]))
                if index in [12]:
                    if row[index] in ['Subscriber']:
                        #print(row[index])
                        row[index]=1
                    elif row[index] in ['Customer']:
                        #print(row[index])
                        row[index]=0
                    else:
                        row[index]=2            
                    selectRow.append(int(row[index]))
                if index in [13]:
                    if row[index] in ['']:
                        row[index]=0
                        age=0
                    elif int(row[index]) > 2011:
                        age=3
                    elif (int(row[index]) > 2006) and (int(row[index]) <= 2011):
                        age=8
                    elif (int(row[index]) > 2001) and (int(row[index]) <= 2006):
                        age=13
                    elif (int(row[index]) > 1996) and (int(row[index]) <= 2001):
                        age=18
                    elif (int(row[index]) > 1991) and (int(row[index]) <= 1996):
                        age=23
                    elif (int(row[index]) > 1986) and (int(row[index]) <= 1991):
                        age=28
                    elif (int(row[index]) > 1981) and (int(row[index]) <= 1986):
                        age=33
                    elif (int(row[index]) > 1976) and (int(row[index]) <= 1981):
                        age=38
                    elif (int(row[index]) > 1971) and (int(row[index]) <= 1976):
                        age=43
                    elif (int(row[index]) > 1966) and (int(row[index]) <= 1971):
                        age=48
                    elif (int(row[index]) > 1961) and (int(row[index]) <= 1966):
                        age=53
                    elif (int(row[index]) > 1956) and (int(row[index]) <= 1961):
                        age=58
                    elif (int(row[index]) > 1951) and (int(row[index]) <= 1956):
                        age=63
                    elif (int(row[index]) > 1946) and (int(row[index]) <= 1951):
                        age=68
                    elif (int(row[index]) > 1941) and (int(row[index]) <= 1946):
                        age=73
                    elif (int(row[index]) > 1936) and (int(row[index]) <= 1941):
                        age=78
                    elif (int(row[index]) > 1931) and (int(row[index]) <= 1936):
                        age=83
                    elif (int(row[index]) > 1926) and (int(row[index]) <= 1931):
                        age=88
                    elif (int(row[index]) > 1921) and (int(row[index]) <= 1926):
                        age=93
                    elif (int(row[index]) > 1916) and (int(row[index]) <= 1921):
                        age=98
                    selectRow.extend([age])
                if index in [14]:
                    selectRow.append(int(row[index]))
            for index in range(len(row)): #through columns                    
                if index in [7]:
                    selectRow.append(int(row[index]))
                
            dataset.append(selectRow)
        i=i+1
    return dataset

def loadCsvClassifiedNaiveStart(filename):
    #lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",", quotechar='\'')
    lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",",quotechar = None,quoting = csv.QUOTE_NONE)
    dataset=[]
    i=0
    for row in lines: #through samples
        if row is None:
            print("NULL detected")
        if i !=0:
            selectRow=[]
            for index in range(len(row)): #through columns
                #print(row[index])                       
                if index in [0]:
                    if int(row[index]) < 60:
                        row[index]=1
                    elif (int(row[index]) >= 60) and (int(row[index]) < 120):
                        row[index]=2
                    elif (int(row[index]) >= 120) and (int(row[index]) < 180):
                        row[index]=3
                    elif (int(row[index]) >= 180) and (int(row[index]) < 240):
                        row[index]=4
                    elif (int(row[index]) >= 240) and (int(row[index]) < 300):
                        row[index]=5
                    elif (int(row[index]) >= 300) and (int(row[index]) < 360):
                        row[index]=6
                    elif (int(row[index]) >= 360) and (int(row[index]) < 420):
                        row[index]=7
                    elif (int(row[index]) >= 420) and (int(row[index]) < 480):
                        row[index]=8
                    elif (int(row[index]) >= 480) and (int(row[index]) < 540):
                        row[index]=9
                    elif (int(row[index]) >= 540) and (int(row[index]) < 600):
                        row[index]=10
                    elif (int(row[index]) >= 600) and (int(row[index]) < 660):
                        row[index]=11
                    elif (int(row[index]) >= 660) and (int(row[index]) < 720):
                        row[index]=12
                    elif (int(row[index]) >= 720) and (int(row[index]) < 780):
                        row[index]=13
                    elif (int(row[index]) >= 780) and (int(row[index]) < 840):
                        row[index]=14
                    elif (int(row[index]) >= 840) and (int(row[index]) < 900):
                        row[index]=15
                    elif (int(row[index]) >= 900) and (int(row[index]) < 960):
                        row[index]=16
                    elif (int(row[index]) >= 960) and (int(row[index]) < 1020):
                        row[index]=17
                    elif (int(row[index]) >= 1020) and (int(row[index]) < 1080):
                        row[index]=18
                    elif (int(row[index]) >= 1080) and (int(row[index]) < 1140):
                        row[index]=19
                    elif (int(row[index]) >= 1140) and (int(row[index]) < 1200):
                        row[index]=20
                    elif (int(row[index]) >= 1200) and (int(row[index]) < 1260):
                        row[index]=21
                    elif (int(row[index]) >= 1260) and (int(row[index]) < 1320):
                        row[index]=22
                    elif (int(row[index]) >= 1320) and (int(row[index]) < 1380):
                        row[index]=23
                    elif (int(row[index]) >= 1380) and (int(row[index]) < 1440):
                        row[index]=24
                    elif (int(row[index]) >= 1440) and (int(row[index]) < 1500):
                        row[index]=25
                    elif (int(row[index]) >= 1500) and (int(row[index]) < 1560):
                        row[index]=26
                    elif (int(row[index]) >= 1560) and (int(row[index]) < 1620):
                        row[index]=27
                    elif (int(row[index]) >= 1620) and (int(row[index]) < 1680):
                        row[index]=28
                    elif (int(row[index]) >= 1680) and (int(row[index]) < 1740):
                        row[index]=29
                    elif (int(row[index]) >= 1740) and (int(row[index]) < 1800):
                        row[index]=30
                    elif (int(row[index]) >= 1800) and (int(row[index]) < 1860):
                        row[index]=31
                    elif (int(row[index]) >= 1860) and (int(row[index]) < 1920):
                        row[index]=32
                    elif (int(row[index]) >= 1920) and (int(row[index]) < 1980):
                        row[index]=33
                    elif (int(row[index]) >= 1980) and (int(row[index]) < 2040):
                        row[index]=34
                    elif (int(row[index]) >= 2040) and (int(row[index]) < 2100):
                        row[index]=35
                    elif (int(row[index]) >= 2100) and (int(row[index]) < 2160):
                        row[index]=36
                    elif (int(row[index]) >= 2160) and (int(row[index]) < 2220):
                        row[index]=37
                    elif (int(row[index]) >= 2220) and (int(row[index]) < 2280):
                        row[index]=38
                    elif (int(row[index]) >= 2280) and (int(row[index]) < 2340):
                        row[index]=39
                    elif (int(row[index]) >= 2340) and (int(row[index]) < 2400):
                        row[index]=40
                    elif (int(row[index]) >= 2400) and (int(row[index]) < 2460):
                        row[index]=41
                    else:
                        row[index]=42
                    selectRow.append(int(row[index]))
                if index in [1]:#time.strptime("2016-12-01 07:35:17","%Y-%m-%d %H:%M:%S")
                    #print(row[index])
                    theTime=time.strptime(row[index],"%Y-%m-%d %H:%M:%S")
                    #print(theTime.tm_hour)
                    if theTime.tm_hour < 2:
                        row[index]=1
                    elif theTime.tm_hour >= 2 and theTime.tm_hour < 4:
                        row[index]=3
                    elif theTime.tm_hour >= 4 and theTime.tm_hour < 6:
                        row[index]=5
                    elif theTime.tm_hour >= 6 and theTime.tm_hour < 8:
                        row[index]=7
                    elif theTime.tm_hour >= 8 and theTime.tm_hour < 10:
                        row[index]=9
                    elif theTime.tm_hour >= 10 and theTime.tm_hour < 12:
                        row[index]=11
                    elif theTime.tm_hour >= 12 and theTime.tm_hour < 14:
                        row[index]=13
                    elif theTime.tm_hour >= 14 and theTime.tm_hour < 16:
                        row[index]=15
                    elif theTime.tm_hour >= 16 and theTime.tm_hour < 18:
                        row[index]=17
                    elif theTime.tm_hour >= 18 and theTime.tm_hour < 20:
                        row[index]=19
                    elif theTime.tm_hour >= 20 and theTime.tm_hour < 22:
                        row[index]=21
                    elif theTime.tm_hour >= 22 and theTime.tm_hour < 24:
                        row[index]=23
                    #if time(row[index]) < time(07):
                    #    print("time success") 
                    selectRow.append(int(row[index]))
                if index in [7]:
                    selectRow.append(int(row[index]))
                if index in [12]:
                    if row[index] in ['Subscriber']:
                        #print(row[index])
                        row[index]=1
                    elif row[index] in ['Customer']:
                        #print(row[index])
                        row[index]=0
                    else:
                        row[index]=2            
                    selectRow.append(int(row[index]))
                if index in [13]:
                    if row[index] in ['']:
                        row[index]=0
                        age=0
                    elif int(row[index]) > 2011:
                        age=3
                    elif (int(row[index]) > 2006) and (int(row[index]) <= 2011):
                        age=8
                    elif (int(row[index]) > 2001) and (int(row[index]) <= 2006):
                        age=13
                    elif (int(row[index]) > 1996) and (int(row[index]) <= 2001):
                        age=18
                    elif (int(row[index]) > 1991) and (int(row[index]) <= 1996):
                        age=23
                    elif (int(row[index]) > 1986) and (int(row[index]) <= 1991):
                        age=28
                    elif (int(row[index]) > 1981) and (int(row[index]) <= 1986):
                        age=33
                    elif (int(row[index]) > 1976) and (int(row[index]) <= 1981):
                        age=38
                    elif (int(row[index]) > 1971) and (int(row[index]) <= 1976):
                        age=43
                    elif (int(row[index]) > 1966) and (int(row[index]) <= 1971):
                        age=48
                    elif (int(row[index]) > 1961) and (int(row[index]) <= 1966):
                        age=53
                    elif (int(row[index]) > 1956) and (int(row[index]) <= 1961):
                        age=58
                    elif (int(row[index]) > 1951) and (int(row[index]) <= 1956):
                        age=63
                    elif (int(row[index]) > 1946) and (int(row[index]) <= 1951):
                        age=68
                    elif (int(row[index]) > 1941) and (int(row[index]) <= 1946):
                        age=73
                    elif (int(row[index]) > 1936) and (int(row[index]) <= 1941):
                        age=78
                    elif (int(row[index]) > 1931) and (int(row[index]) <= 1936):
                        age=83
                    elif (int(row[index]) > 1926) and (int(row[index]) <= 1931):
                        age=88
                    elif (int(row[index]) > 1921) and (int(row[index]) <= 1926):
                        age=93
                    elif (int(row[index]) > 1916) and (int(row[index]) <= 1921):
                        age=98
                    selectRow.extend([age])
                if index in [14]:
                    selectRow.append(int(row[index]))
            for index in range(len(row)): #through columns                    
                if index in [3]:
                    selectRow.append(int(row[index]))
                
            dataset.append(selectRow)
        i=i+1
    return dataset

def loadCsvClassifiedNoHour(filename):
    #lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",", quotechar='\'')
    lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",",quotechar = None,quoting = csv.QUOTE_NONE)
    dataset=[]
    i=0
    for row in lines: #through samples
        if row is None:
            print("NULL detected")
        if i !=0:
            selectRow=[]
            for index in range(len(row)): #through columns
                #print(row[index])                       
                if index in [0]:
                    if int(row[index]) < 60:
                        row[index]=1
                    elif (int(row[index]) >= 60) and (int(row[index]) < 120):
                        row[index]=2
                    elif (int(row[index]) >= 120) and (int(row[index]) < 180):
                        row[index]=3
                    elif (int(row[index]) >= 180) and (int(row[index]) < 240):
                        row[index]=4
                    elif (int(row[index]) >= 240) and (int(row[index]) < 300):
                        row[index]=5
                    elif (int(row[index]) >= 300) and (int(row[index]) < 360):
                        row[index]=6
                    elif (int(row[index]) >= 360) and (int(row[index]) < 420):
                        row[index]=7
                    elif (int(row[index]) >= 420) and (int(row[index]) < 480):
                        row[index]=8
                    elif (int(row[index]) >= 480) and (int(row[index]) < 540):
                        row[index]=9
                    elif (int(row[index]) >= 540) and (int(row[index]) < 600):
                        row[index]=10
                    elif (int(row[index]) >= 600) and (int(row[index]) < 660):
                        row[index]=11
                    elif (int(row[index]) >= 660) and (int(row[index]) < 720):
                        row[index]=12
                    elif (int(row[index]) >= 720) and (int(row[index]) < 780):
                        row[index]=13
                    elif (int(row[index]) >= 780) and (int(row[index]) < 840):
                        row[index]=14
                    elif (int(row[index]) >= 840) and (int(row[index]) < 900):
                        row[index]=15
                    elif (int(row[index]) >= 900) and (int(row[index]) < 960):
                        row[index]=16
                    elif (int(row[index]) >= 960) and (int(row[index]) < 1020):
                        row[index]=17
                    elif (int(row[index]) >= 1020) and (int(row[index]) < 1080):
                        row[index]=18
                    elif (int(row[index]) >= 1080) and (int(row[index]) < 1140):
                        row[index]=19
                    elif (int(row[index]) >= 1140) and (int(row[index]) < 1200):
                        row[index]=20
                    elif (int(row[index]) >= 1200) and (int(row[index]) < 1260):
                        row[index]=21
                    elif (int(row[index]) >= 1260) and (int(row[index]) < 1320):
                        row[index]=22
                    elif (int(row[index]) >= 1320) and (int(row[index]) < 1380):
                        row[index]=23
                    elif (int(row[index]) >= 1380) and (int(row[index]) < 1440):
                        row[index]=24
                    elif (int(row[index]) >= 1440) and (int(row[index]) < 1500):
                        row[index]=25
                    elif (int(row[index]) >= 1500) and (int(row[index]) < 1560):
                        row[index]=26
                    elif (int(row[index]) >= 1560) and (int(row[index]) < 1620):
                        row[index]=27
                    elif (int(row[index]) >= 1620) and (int(row[index]) < 1680):
                        row[index]=28
                    elif (int(row[index]) >= 1680) and (int(row[index]) < 1740):
                        row[index]=29
                    elif (int(row[index]) >= 1740) and (int(row[index]) < 1800):
                        row[index]=30
                    elif (int(row[index]) >= 1800) and (int(row[index]) < 1860):
                        row[index]=31
                    elif (int(row[index]) >= 1860) and (int(row[index]) < 1920):
                        row[index]=32
                    elif (int(row[index]) >= 1920) and (int(row[index]) < 1980):
                        row[index]=33
                    elif (int(row[index]) >= 1980) and (int(row[index]) < 2040):
                        row[index]=34
                    elif (int(row[index]) >= 2040) and (int(row[index]) < 2100):
                        row[index]=35
                    elif (int(row[index]) >= 2100) and (int(row[index]) < 2160):
                        row[index]=36
                    elif (int(row[index]) >= 2160) and (int(row[index]) < 2220):
                        row[index]=37
                    elif (int(row[index]) >= 2220) and (int(row[index]) < 2280):
                        row[index]=38
                    elif (int(row[index]) >= 2280) and (int(row[index]) < 2340):
                        row[index]=39
                    elif (int(row[index]) >= 2340) and (int(row[index]) < 2400):
                        row[index]=40
                    elif (int(row[index]) >= 2400) and (int(row[index]) < 2460):
                        row[index]=41
                    else:
                        row[index]=42
                    selectRow.append(int(row[index]))
                if index in [3]:
                    selectRow.append(int(row[index]))
                if index in [7]:
                    selectRow.append(int(row[index]))
                if index in [12]:
                    if row[index] in ['Subscriber']:
                        #print(row[index])
                        row[index]=1
                    elif row[index] in ['Customer']:
                        #print(row[index])
                        row[index]=0
                    else:
                        row[index]=2            
                    selectRow.append(int(row[index]))
                if index in [13]:
                    if row[index] in ['']:
                        row[index]=0
                        age=0
                    elif int(row[index]) > 2011:
                        age=3
                    elif (int(row[index]) > 2006) and (int(row[index]) <= 2011):
                        age=8
                    elif (int(row[index]) > 2001) and (int(row[index]) <= 2006):
                        age=13
                    elif (int(row[index]) > 1996) and (int(row[index]) <= 2001):
                        age=18
                    elif (int(row[index]) > 1991) and (int(row[index]) <= 1996):
                        age=23
                    elif (int(row[index]) > 1986) and (int(row[index]) <= 1991):
                        age=28
                    elif (int(row[index]) > 1981) and (int(row[index]) <= 1986):
                        age=33
                    elif (int(row[index]) > 1976) and (int(row[index]) <= 1981):
                        age=38
                    elif (int(row[index]) > 1971) and (int(row[index]) <= 1976):
                        age=43
                    elif (int(row[index]) > 1966) and (int(row[index]) <= 1971):
                        age=48
                    elif (int(row[index]) > 1961) and (int(row[index]) <= 1966):
                        age=53
                    elif (int(row[index]) > 1956) and (int(row[index]) <= 1961):
                        age=58
                    elif (int(row[index]) > 1951) and (int(row[index]) <= 1956):
                        age=63
                    elif (int(row[index]) > 1946) and (int(row[index]) <= 1951):
                        age=68
                    elif (int(row[index]) > 1941) and (int(row[index]) <= 1946):
                        age=73
                    elif (int(row[index]) > 1936) and (int(row[index]) <= 1941):
                        age=78
                    elif (int(row[index]) > 1931) and (int(row[index]) <= 1936):
                        age=83
                    elif (int(row[index]) > 1926) and (int(row[index]) <= 1931):
                        age=88
                    elif (int(row[index]) > 1921) and (int(row[index]) <= 1926):
                        age=93
                    elif (int(row[index]) > 1916) and (int(row[index]) <= 1921):
                        age=98
                    selectRow.extend([age])
                if index in [14]:
                    selectRow.append(int(row[index]))

            dataset.append(selectRow)
        i=i+1
    return dataset

def loadCsvClassifiedNoGender(filename):
    #lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",", quotechar='\'')
    lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",",quotechar = None,quoting = csv.QUOTE_NONE)
    dataset=[]
    i=0
    for row in lines: #through samples
        if row is None:
            print("NULL detected")
        if i !=0:
            selectRow=[]
            for index in range(len(row)): #through columns
                #print(row[index])                       
                if index in [0]:
                    if int(row[index]) < 60:
                        row[index]=1
                    elif (int(row[index]) >= 60) and (int(row[index]) < 120):
                        row[index]=2
                    elif (int(row[index]) >= 120) and (int(row[index]) < 180):
                        row[index]=3
                    elif (int(row[index]) >= 180) and (int(row[index]) < 240):
                        row[index]=4
                    elif (int(row[index]) >= 240) and (int(row[index]) < 300):
                        row[index]=5
                    elif (int(row[index]) >= 300) and (int(row[index]) < 360):
                        row[index]=6
                    elif (int(row[index]) >= 360) and (int(row[index]) < 420):
                        row[index]=7
                    elif (int(row[index]) >= 420) and (int(row[index]) < 480):
                        row[index]=8
                    elif (int(row[index]) >= 480) and (int(row[index]) < 540):
                        row[index]=9
                    elif (int(row[index]) >= 540) and (int(row[index]) < 600):
                        row[index]=10
                    elif (int(row[index]) >= 600) and (int(row[index]) < 660):
                        row[index]=11
                    elif (int(row[index]) >= 660) and (int(row[index]) < 720):
                        row[index]=12
                    elif (int(row[index]) >= 720) and (int(row[index]) < 780):
                        row[index]=13
                    elif (int(row[index]) >= 780) and (int(row[index]) < 840):
                        row[index]=14
                    elif (int(row[index]) >= 840) and (int(row[index]) < 900):
                        row[index]=15
                    elif (int(row[index]) >= 900) and (int(row[index]) < 960):
                        row[index]=16
                    elif (int(row[index]) >= 960) and (int(row[index]) < 1020):
                        row[index]=17
                    elif (int(row[index]) >= 1020) and (int(row[index]) < 1080):
                        row[index]=18
                    elif (int(row[index]) >= 1080) and (int(row[index]) < 1140):
                        row[index]=19
                    elif (int(row[index]) >= 1140) and (int(row[index]) < 1200):
                        row[index]=20
                    elif (int(row[index]) >= 1200) and (int(row[index]) < 1260):
                        row[index]=21
                    elif (int(row[index]) >= 1260) and (int(row[index]) < 1320):
                        row[index]=22
                    elif (int(row[index]) >= 1320) and (int(row[index]) < 1380):
                        row[index]=23
                    elif (int(row[index]) >= 1380) and (int(row[index]) < 1440):
                        row[index]=24
                    elif (int(row[index]) >= 1440) and (int(row[index]) < 1500):
                        row[index]=25
                    elif (int(row[index]) >= 1500) and (int(row[index]) < 1560):
                        row[index]=26
                    elif (int(row[index]) >= 1560) and (int(row[index]) < 1620):
                        row[index]=27
                    elif (int(row[index]) >= 1620) and (int(row[index]) < 1680):
                        row[index]=28
                    elif (int(row[index]) >= 1680) and (int(row[index]) < 1740):
                        row[index]=29
                    elif (int(row[index]) >= 1740) and (int(row[index]) < 1800):
                        row[index]=30
                    elif (int(row[index]) >= 1800) and (int(row[index]) < 1860):
                        row[index]=31
                    elif (int(row[index]) >= 1860) and (int(row[index]) < 1920):
                        row[index]=32
                    elif (int(row[index]) >= 1920) and (int(row[index]) < 1980):
                        row[index]=33
                    elif (int(row[index]) >= 1980) and (int(row[index]) < 2040):
                        row[index]=34
                    elif (int(row[index]) >= 2040) and (int(row[index]) < 2100):
                        row[index]=35
                    elif (int(row[index]) >= 2100) and (int(row[index]) < 2160):
                        row[index]=36
                    elif (int(row[index]) >= 2160) and (int(row[index]) < 2220):
                        row[index]=37
                    elif (int(row[index]) >= 2220) and (int(row[index]) < 2280):
                        row[index]=38
                    elif (int(row[index]) >= 2280) and (int(row[index]) < 2340):
                        row[index]=39
                    elif (int(row[index]) >= 2340) and (int(row[index]) < 2400):
                        row[index]=40
                    elif (int(row[index]) >= 2400) and (int(row[index]) < 2460):
                        row[index]=41
                    else:
                        row[index]=42
                    selectRow.append(int(row[index]))
                if index in [1]:#time.strptime("2016-12-01 07:35:17","%Y-%m-%d %H:%M:%S")
                    #print(row[index])
                    theTime=time.strptime(row[index],"%Y-%m-%d %H:%M:%S")
                    #print(theTime.tm_hour)
                    if theTime.tm_hour < 2:
                        row[index]=1
                    elif theTime.tm_hour >= 2 and theTime.tm_hour < 4:
                        row[index]=3
                    elif theTime.tm_hour >= 4 and theTime.tm_hour < 6:
                        row[index]=5
                    elif theTime.tm_hour >= 6 and theTime.tm_hour < 8:
                        row[index]=7
                    elif theTime.tm_hour >= 8 and theTime.tm_hour < 10:
                        row[index]=9
                    elif theTime.tm_hour >= 10 and theTime.tm_hour < 12:
                        row[index]=11
                    elif theTime.tm_hour >= 12 and theTime.tm_hour < 14:
                        row[index]=13
                    elif theTime.tm_hour >= 14 and theTime.tm_hour < 16:
                        row[index]=15
                    elif theTime.tm_hour >= 16 and theTime.tm_hour < 18:
                        row[index]=17
                    elif theTime.tm_hour >= 18 and theTime.tm_hour < 20:
                        row[index]=19
                    elif theTime.tm_hour >= 20 and theTime.tm_hour < 22:
                        row[index]=21
                    elif theTime.tm_hour >= 22 and theTime.tm_hour < 24:
                        row[index]=23
                    #if time(row[index]) < time(07):
                    #    print("time success") 
                    selectRow.append(int(row[index]))
                if index in [3]:
                    selectRow.append(int(row[index]))
                if index in [7]:
                    selectRow.append(int(row[index]))
                if index in [12]:
                    if row[index] in ['Subscriber']:
                        #print(row[index])
                        row[index]=1
                    elif row[index] in ['Customer']:
                        #print(row[index])
                        row[index]=0
                    else:
                        row[index]=2            
                    selectRow.append(int(row[index]))
                if index in [13]:
                    if row[index] in ['']:
                        row[index]=0
                        age=0
                    elif int(row[index]) > 2011:
                        age=3
                    elif (int(row[index]) > 2006) and (int(row[index]) <= 2011):
                        age=8
                    elif (int(row[index]) > 2001) and (int(row[index]) <= 2006):
                        age=13
                    elif (int(row[index]) > 1996) and (int(row[index]) <= 2001):
                        age=18
                    elif (int(row[index]) > 1991) and (int(row[index]) <= 1996):
                        age=23
                    elif (int(row[index]) > 1986) and (int(row[index]) <= 1991):
                        age=28
                    elif (int(row[index]) > 1981) and (int(row[index]) <= 1986):
                        age=33
                    elif (int(row[index]) > 1976) and (int(row[index]) <= 1981):
                        age=38
                    elif (int(row[index]) > 1971) and (int(row[index]) <= 1976):
                        age=43
                    elif (int(row[index]) > 1966) and (int(row[index]) <= 1971):
                        age=48
                    elif (int(row[index]) > 1961) and (int(row[index]) <= 1966):
                        age=53
                    elif (int(row[index]) > 1956) and (int(row[index]) <= 1961):
                        age=58
                    elif (int(row[index]) > 1951) and (int(row[index]) <= 1956):
                        age=63
                    elif (int(row[index]) > 1946) and (int(row[index]) <= 1951):
                        age=68
                    elif (int(row[index]) > 1941) and (int(row[index]) <= 1946):
                        age=73
                    elif (int(row[index]) > 1936) and (int(row[index]) <= 1941):
                        age=78
                    elif (int(row[index]) > 1931) and (int(row[index]) <= 1936):
                        age=83
                    elif (int(row[index]) > 1926) and (int(row[index]) <= 1931):
                        age=88
                    elif (int(row[index]) > 1921) and (int(row[index]) <= 1926):
                        age=93
                    elif (int(row[index]) > 1916) and (int(row[index]) <= 1921):
                        age=98
                    selectRow.extend([age])

            dataset.append(selectRow)
        i=i+1
    #print(dataset[-1])
    #del dataset[-1]
    #print(len(dataset))
    #print(dataset)
    #print(len(dataset))
    #print(i)
    return dataset


"""OLD version
def loadCsvClassifiedNaive(filename):
    #lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",", quotechar='\'')
    lines = csv.reader(open(filename,encoding="cp1250"), delimiter=",",quotechar = None,quoting = csv.QUOTE_NONE)
    dataset=[]
    i=0
    for row in lines: #through samples
        if row is None:
            print("NULL detected")
        if i !=0:
            selectRow=[]
            #print(row[14])
            for index in range(len(row)): #through columns
                #print(row[index])                       
                if index in [0]:
                    if int(row[index]) < 120:
                        row[index]=1
                    elif (int(row[index]) >= 120) and (int(row[index]) < 240):
                        row[index]=3
                    elif (int(row[index]) >= 240) and (int(row[index]) < 360):
                        row[index]=5
                    elif (int(row[index]) >= 360) and (int(row[index]) < 480):
                        row[index]=7
                    elif (int(row[index]) >= 480) and (int(row[index]) < 600):
                        row[index]=9
                    elif (int(row[index]) >= 600) and (int(row[index]) < 720):
                        row[index]=11
                    elif (int(row[index]) >= 720) and (int(row[index]) < 840):
                        row[index]=13
                    elif (int(row[index]) >= 840) and (int(row[index]) < 960):
                        row[index]=15
                    elif (int(row[index]) >= 960) and (int(row[index]) < 1080):
                        row[index]=17
                    else:
                        row[index]=19
                    selectRow.append(int(row[index]))
                if index in [1]:#time.strptime("2016-12-01 07:35:17","%Y-%m-%d %H:%M:%S")
                    #print(row[index])
                    theTime=time.strptime(row[index],"%Y-%m-%d %H:%M:%S")
                    #print(theTime.tm_hour)
                    if theTime.tm_hour < 2:
                        row[index]=1
                    elif theTime.tm_hour >= 2 and theTime.tm_hour < 4:
                        row[index]=3
                    elif theTime.tm_hour >= 4 and theTime.tm_hour < 6:
                        row[index]=5
                    elif theTime.tm_hour >= 6 and theTime.tm_hour < 8:
                        row[index]=7
                    elif theTime.tm_hour >= 8 and theTime.tm_hour < 10:
                        row[index]=9
                    elif theTime.tm_hour >= 10 and theTime.tm_hour < 12:
                        row[index]=11
                    elif theTime.tm_hour >= 12 and theTime.tm_hour < 14:
                        row[index]=13
                    elif theTime.tm_hour >= 14 and theTime.tm_hour < 16:
                        row[index]=15
                    elif theTime.tm_hour >= 16 and theTime.tm_hour < 18:
                        row[index]=17
                    elif theTime.tm_hour >= 18 and theTime.tm_hour < 20:
                        row[index]=19
                    elif theTime.tm_hour >= 20 and theTime.tm_hour < 22:
                        row[index]=21
                    elif theTime.tm_hour >= 22 and theTime.tm_hour < 24:
                        row[index]=23
                    #if time(row[index]) < time(07):
                    #    print("time success") 
                    selectRow.append(int(row[index]))
                if index in [3]:
                    selectRow.append(int(row[index]))
                if index in [12]:
                    if row[index] in ['Subscriber']:
                        #print(row[index])
                        row[index]=1
                    elif row[index] in ['Customer']:
                        #print(row[index])
                        row[index]=0
                    else:
                        row[index]=2            
                    selectRow.append(int(row[index]))
                if index in [13]:
                    if row[index] in ['']:
                        row[index]=0
                        age=0
                    elif int(row[index]) > 2001:
                        age=10
                    elif (int(row[index]) > 1991) and (int(row[index]) <= 2001):
                        age=20
                    elif (int(row[index]) > 1981) and (int(row[index]) <= 1991):
                        age=30
                    elif (int(row[index]) > 1971) and (int(row[index]) <= 1981):
                        age=40
                    elif (int(row[index]) > 1961) and (int(row[index]) <= 1971):
                        age=50
                    elif (int(row[index]) > 1951) and (int(row[index]) <= 1961):
                        age=60
                    elif (int(row[index]) > 1941) and (int(row[index]) <= 1951):
                        age=70
                    elif (int(row[index]) > 1931) and (int(row[index]) <= 1941):
                        age=80
                    elif (int(row[index]) > 1921) and (int(row[index]) <= 1931):
                        age=90
                    elif (int(row[index]) > 1911) and (int(row[index]) <= 1921):
                        age=100
                    selectRow.extend([age])
                if index in [14]:
                    selectRow.append(int(row[index]))
            for index in range(len(row)): #through columns  
                if index in [7]:
                    selectRow.append(int(row[index]))
            
            dataset.append(selectRow)
        i=i+1
    #print(dataset[-1])
    #del dataset[-1]
    #print(len(dataset))
    #print(dataset)
    #print(len(dataset))
    #print(i)
    return dataset
"""
############# Naive Bayes Prediction #############

def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        #print(vector)
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

def summarize(dataset):
    summaries = [(Counter(attribute).keys(),Counter(attribute).values(),sum(Counter(attribute).values())) for attribute in zip(*dataset)]
    #sumofcounts=[sum(Counter(attribute).values()) for attribute in zip(*dataset)]
    #print(summaries)
    del summaries[-1]
    return summaries

def summarizeByClass(dataset):
    separated = separateByClass(dataset)
    #print(separated)
    summaries = {}
    for classValue, instances in separated.items():
        summaries[classValue] = summarize(instances)
    #print(summaries)
    return summaries

def countsByClass(dataset):#Prepare counts of the outcome, in order to calculate the P(Outcome)
    x=[]
    for i in range(len(dataset)):
        x.append([dataset[i][-1]])
    #print(x)
    countsByClass = [(Counter(attribute).keys(),Counter(attribute).values(),sum(Counter(attribute).values())) for attribute in zip(*x)]
    #sumofcounts=[sum(Counter(attribute).values()) for attribute in zip(*dataset)]
    #print(summaries)
    #del summaries[-1]
    return countsByClass

def calculateClassFrequncyProb(countsByClass):
    FrequncyProb = {}
    #probByClass={}
    for classKey, classValue, total in countsByClass:  
        #print(classKey)
        temp_key=list(classKey)
        temp_counts=list(classValue)
        for i in range(len(temp_key)):
            FrequncyProb[temp_key[i]]=temp_counts[i]/total
    #print(temp_key)
    #print(temp_counts)
    return FrequncyProb

def calculateClassProbabilities(FrequncyProb,summaries, inputVector):
    probabilities = {}
    probByClass={}
    for classValue, classSummaries in summaries.items():      
        probPerColumns=[]
        for keys, counts, total in classSummaries:
                temp_counts=list(counts)
                temp_keys=list(keys)
                probPerState={}
                for i in range(len(temp_keys)):
                    probPerState[temp_keys[i]]=temp_counts[i]/total
                probPerColumns.append(probPerState)
        probabilities[classValue]=probPerColumns
        probProduct=1
        for i in range(len(probabilities[classValue])):
            z=inputVector[i]
            if z in probabilities[classValue][i].keys():
                #print(probabilities[classValue][i][z])
                probProduct*=probabilities[classValue][i][z]
            else:
                #print("false")
                probProduct*=1/296
        probByClass[classValue]=probProduct*FrequncyProb[classValue]
        #print (probabilities[18][i])
    #print(probByClass)
    return probByClass

def predict(FrequncyProb,summaries, inputVector):
	probabilities = calculateClassProbabilities(FrequncyProb,summaries, inputVector)
	bestLabel, bestProb = None, -1
	for classValue, probability in probabilities.items():
		if bestLabel is None or probability > bestProb:
			bestProb = probability
			bestLabel = classValue
	return bestLabel

def getPredictions(FrequncyProb,summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        #print(i)
        result = predict(FrequncyProb,summaries, testSet[i])
        predictions.append(result)
    print(predictions)
    return predictions

def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    #print(len(testSet))
    return (correct/(len(testSet))) * 100

def naiveBayes(dataset,testset):
    summaries = summarizeByClass(dataset)
    countsbyclass = countsByClass(dataset)
    FrequncyProb=calculateClassFrequncyProb(countsbyclass)
    predictions = getPredictions(FrequncyProb,summaries, testset)
    #print(predictions)
    accuracy = getAccuracy(testset, predictions)
    #print(accuracy)
    print(('Accuracy: {0}%').format(accuracy))
    return accuracy

############# Minimum Spanning Tree #############
#MST from https://www.ics.uci.edu/~eppstein/161/python/prim.py
def weight(A, u, v):
    return A[u][v]

#A = adjacency matrix, u = vertex u
def adjacent(A, u):
    L = []
    for x in range(len(A)):
        if A[u][x] > 0 and x != u:
            L.insert(0,x)
    return L

#Q = min queue
def extractMin(Q):
    q = Q[0]
    Q.remove(Q[0])
    return q

#Q = min queue, V = vertex list
def decreaseKey(Q, K):
    for i in range(len(Q)):
        for j in range(len(Q)):
            if K[Q[i]] < K[Q[j]]:
                s = Q[i]
                Q[i] = Q[j]
                Q[j] = s

#V = vertex list, A = adjacency list, r = root
def prim(V, A, r):
    u = 0
    v = 0

    # initialize and set each value of the array P (pi) to none
    # pi holds the parent of u, so P(v)=u means u is the parent of v
    P=[None]*len(V)

    # initialize and set each value of the array K (key) to some large number (simulate infinity)
    K = [999999]*len(V)

    # initialize the min queue and fill it with all vertices in V
    Q=[0]*len(V)
    for u in range(len(Q)):
        Q[u] = V[u]

    # set the key of the root to 0
    K[r] = 0
    decreaseKey(Q, K)    # maintain the min queue

    # loop while the min queue is not empty
    while len(Q) > 0:
        u = extractMin(Q)    # pop the first vertex off the min queue

        # loop through the vertices adjacent to u
        Adj = adjacent(A, u)
        for v in Adj:
            w = weight(A, u, v)    # get the weight of the edge uv

            # proceed if v is in Q and the weight of uv is less than v's key
            if Q.count(v)>0 and w < K[v]:
                # set v's parent to u
                P[v] = u
                # v's key to the weight of uv
                K[v] = w
                decreaseKey(Q, K)    # maintain the min queue
    return P

############# Chow-Liu Tree #############

def countsByOneVar(dataset,order):
    x=[]
    for i in range(len(dataset)):
        x.append([dataset[i][order]])
    #print(x)
    countByOneVariable= [(Counter(attribute).keys(),Counter(attribute).values(),sum(Counter(attribute).values())) for attribute in zip(*x)]
    return countByOneVariable

def calculateVarFreqProb(countByOneVariable):
    FrequncyProb = {}
    #probByClass={}
    for classKey, classValue, total in countByOneVariable:  
        #print(classKey)
        temp_key=list(classKey)
        temp_counts=list(classValue)
        for i in range(len(temp_key)):
            FrequncyProb[temp_key[i]]=temp_counts[i]/total
    #print(temp_key)
    #print(temp_counts)
    return FrequncyProb

def probAmongTwoVar (dataset,OrA,OrB):
    prob={}
    x=[]
    for i in range(len(dataset)):
        y=[]
        y.append(dataset[i][OrA])
        y.append(dataset[i][OrB])
        x.append(tuple(y))
    b = defaultdict(int)
    for item in x:
        b[item] += 1
    total=0
    for item in x:
        total +=1
    #print(total)
    for key, value in b.items():
        prob[key]=value/total
    #print(prob)
    #for i in range
    #print(prob[(4, 4)])        
    #countAmongTwoVariable= [(Counter(attribute).keys(),Counter(attribute).values(),sum(Counter(attribute).values())) for attribute in zip(*x)]
    #print(countAmongTwoVariable)
    return prob#countAmongTwoVariable

def mutualInfo(dataset,order1,order2):
    x1=[]# all possible state in x1 variable
    for i in range(len(dataset)):
        if dataset[i][order1] not in x1:
            #print(dataset[i][order1])
            x1.append(dataset[i][order1])
    #print(x1)
    x2=[]# all possible state in x2 variable
    for i in range(len(dataset)):
        if dataset[i][order2] not in x2:
            #print(dataset[i][order2])
            x2.append(dataset[i][order2])
    #print(x2)

    countByVariableONE=countsByOneVar(dataset,order1)
    #print(countByVariableONE)
    p1=calculateVarFreqProb(countByVariableONE)
    #print(p1)
    countByVariableTWO=countsByOneVar(dataset,order2)
    #print(countByVariableTWO)
    p2=calculateVarFreqProb(countByVariableTWO)
    #print(p2)
    p1and2=probAmongTwoVar(dataset,order1,order2)
    #print(p1and2)

    Isum=0
    for i in x1:
        for j in x2:
            #print(i)
            #print(j)
            xp1=0
            xp2=0
            xp12=0
            for key, prob in p1.items():
                #print(key)
               
                if key == i:
                    xp1=prob
                    #print(key)
                    #print(xp1)
            for key, prob in p2.items():
                
                if key == j:
                    xp2=prob
                    #print(key)
                    #print(xp2)                    
            for pair,prob in p1and2.items():
                
                if pair == (i, j):
                    #print(pair)
                    xp12=p1and2[pair]
                    #print(xp12)
            if xp1==0:
                xp1=1/296
            if xp2==0:
                xp2=1/296
            if xp12==0:
                xp12=1/296
                
            #print(xp1)
            #print(xp2)
            #print(xp12)
            #print(math.log((xp12/(xp1*xp2)),2))
            #print()
            I=xp12*math.log((xp12/(xp1*xp2)),2)
            #print(I)
            Isum=Isum+I
    return Isum

def mutualInfoMatrix(dataset):
    matrix=[]
    for i in range(len(dataset[1])):
        row=[]
        for j in range(len(dataset[1])):
            if i == j:
                row.append(0)
            else:    
                row.append(mutualInfo(dataset,i,j))
        #print(row)
        matrix.append(row)
    return matrix
  
def fromMatrixToTree(matrix):
    #V = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    #V = [ 0, 1, 2, 3, 4, 5, 6]
    V = [ 0, 1, 2, 3, 4, 5, 6]
    connection = prim(V, matrix, 0)
    print (connection)
    return connection

def fromMatrixToTree5Var(matrix):
    #V = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    #V = [ 0, 1, 2, 3, 4, 5, 6]
    V = [ 0, 1, 2, 3, 4, 5]
    connection = prim(V, matrix, 0)
    print (connection)
    return connection


def ChowLiuTree(dataset):
    matrix=mutualInfoMatrix(dataset)
    print(matrix)
    connection=fromMatrixToTree(matrix)
    return connection

def ChowLiuTree5Var(dataset):
    matrix=mutualInfoMatrix(dataset)
    print(matrix)
    connection=fromMatrixToTree5Var(matrix)
    return connection


def ChowLiuTreeForJC20161sthalf():
    trainSetFile1  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201601-citibike-tripdata.csv'
    trainSetFile2  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201602-citibike-tripdata.csv'
    trainSetFile3  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201603-citibike-tripdata.csv'
    trainSetFile4  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201604-citibike-tripdata.csv'
    trainSetFile5  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201605-citibike-tripdata.csv'
    trainSetFile6  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201606-citibike-tripdata.csv' 
    dataset1 = loadCsvClassified(trainSetFile1)
    print(len(dataset1))
    dataset2=appendToDataset(dataset1,trainSetFile2)
    print(len(dataset2))
    dataset3=appendToDataset(dataset2,trainSetFile3)
    print(len(dataset3))
    dataset4=appendToDataset(dataset3,trainSetFile4)
    print(len(dataset4))
    dataset5=appendToDataset(dataset4,trainSetFile5)
    print(len(dataset5))
    dataset6=appendToDataset(dataset5,trainSetFile6)
    print(len(dataset6))
    ChowLiuTree(dataset6)
    return

def ChowLiuTreeForJC20162ndhalf():
    trainSetFile7  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201607-citibike-tripdata.csv'
    trainSetFile8  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201608-citibike-tripdata.csv'
    trainSetFile9  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201609-citibike-tripdata.csv'
    trainSetFile10 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201610-citibike-tripdata.csv'
    trainSetFile11 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201611-citibike-tripdata.csv'
    trainSetFile12 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201612-citibike-tripdata.csv'
    dataset7 = loadCsvClassified(trainSetFile7)
    print(len(dataset7))
    dataset8=appendToDataset(dataset7,trainSetFile8)
    print(len(dataset8))
    dataset9=appendToDataset(dataset8,trainSetFile9)
    print(len(dataset9))
    dataset10=appendToDataset(dataset9,trainSetFile10)
    print(len(dataset10))
    dataset11=appendToDataset(dataset10,trainSetFile11)
    print(len(dataset11))
    dataset12=appendToDataset(dataset11,trainSetFile12)
    print(len(dataset12))
    ChowLiuTree(dataset12)
    return

def ChowLiuTreeForJC2016():
    trainSetFile1  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201601-citibike-tripdata.csv'
    trainSetFile2  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201602-citibike-tripdata.csv'
    trainSetFile3  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201603-citibike-tripdata.csv'
    trainSetFile4  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201604-citibike-tripdata.csv'
    trainSetFile5  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201605-citibike-tripdata.csv'
    trainSetFile6  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201606-citibike-tripdata.csv'
    trainSetFile7  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201607-citibike-tripdata.csv'
    trainSetFile8  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201608-citibike-tripdata.csv'
    trainSetFile9  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201609-citibike-tripdata.csv'
    trainSetFile10 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201610-citibike-tripdata.csv'
    trainSetFile11 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201611-citibike-tripdata.csv'
    trainSetFile12 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201612-citibike-tripdata.csv'
    dataset1 = loadCsvClassified(trainSetFile1)
    print(len(dataset1))
    dataset2=appendToDataset(dataset1,trainSetFile2)
    print(len(dataset2))
    dataset3=appendToDataset(dataset2,trainSetFile3)
    print(len(dataset3))
    dataset4=appendToDataset(dataset3,trainSetFile4)
    print(len(dataset4))
    dataset5=appendToDataset(dataset4,trainSetFile5)
    print(len(dataset5))
    dataset6=appendToDataset(dataset5,trainSetFile6)
    print(len(dataset6))
    dataset7=appendToDataset(dataset6,trainSetFile7)
    print(len(dataset7))
    dataset8=appendToDataset(dataset7,trainSetFile8)
    print(len(dataset8))
    dataset9=appendToDataset(dataset8,trainSetFile9)
    print(len(dataset9))
    dataset10=appendToDataset(dataset9,trainSetFile10)
    print(len(dataset10))
    dataset11=appendToDataset(dataset10,trainSetFile11)
    print(len(dataset11))
    dataset12=appendToDataset(dataset11,trainSetFile12)
    print(len(dataset12))
    ChowLiuTree(dataset12)
    return

def ChowLiuTreeForJC2016NoHour():
    trainSetFile1  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201601-citibike-tripdata.csv'
    trainSetFile2  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201602-citibike-tripdata.csv'
    trainSetFile3  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201603-citibike-tripdata.csv'
    trainSetFile4  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201604-citibike-tripdata.csv'
    trainSetFile5  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201605-citibike-tripdata.csv'
    trainSetFile6  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201606-citibike-tripdata.csv'
    trainSetFile7  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201607-citibike-tripdata.csv'
    trainSetFile8  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201608-citibike-tripdata.csv'
    trainSetFile9  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201609-citibike-tripdata.csv'
    trainSetFile10 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201610-citibike-tripdata.csv'
    trainSetFile11 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201611-citibike-tripdata.csv'
    trainSetFile12 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201612-citibike-tripdata.csv'
    dataset1 = loadCsvClassifiedNoHour(trainSetFile1)
    print(len(dataset1))
    dataset2=appendToDatasetNoHour(dataset1,trainSetFile2)
    print(len(dataset2))
    dataset3=appendToDatasetNoHour(dataset2,trainSetFile3)
    print(len(dataset3))
    dataset4=appendToDatasetNoHour(dataset3,trainSetFile4)
    print(len(dataset4))
    dataset5=appendToDatasetNoHour(dataset4,trainSetFile5)
    print(len(dataset5))
    dataset6=appendToDatasetNoHour(dataset5,trainSetFile6)
    print(len(dataset6))
    dataset7=appendToDatasetNoHour(dataset6,trainSetFile7)
    print(len(dataset7))
    dataset8=appendToDatasetNoHour(dataset7,trainSetFile8)
    print(len(dataset8))
    dataset9=appendToDatasetNoHour(dataset8,trainSetFile9)
    print(len(dataset9))
    dataset10=appendToDatasetNoHour(dataset9,trainSetFile10)
    print(len(dataset10))
    dataset11=appendToDatasetNoHour(dataset10,trainSetFile11)
    print(len(dataset11))
    dataset12=appendToDatasetNoHour(dataset11,trainSetFile12)
    print(len(dataset12))
    ChowLiuTree5Var(dataset12)
    return

def ChowLiuTreeForJC2016NoGender():
    trainSetFile1  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201601-citibike-tripdata.csv'
    trainSetFile2  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201602-citibike-tripdata.csv'
    trainSetFile3  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201603-citibike-tripdata.csv'
    trainSetFile4  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201604-citibike-tripdata.csv'
    trainSetFile5  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201605-citibike-tripdata.csv'
    trainSetFile6  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201606-citibike-tripdata.csv'
    trainSetFile7  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201607-citibike-tripdata.csv'
    trainSetFile8  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201608-citibike-tripdata.csv'
    trainSetFile9  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201609-citibike-tripdata.csv'
    trainSetFile10 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201610-citibike-tripdata.csv'
    trainSetFile11 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201611-citibike-tripdata.csv'
    trainSetFile12 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201612-citibike-tripdata.csv'
    dataset1 = loadCsvClassifiedNoGender(trainSetFile1)
    print(len(dataset1))
    dataset2=appendToDatasetNoGender(dataset1,trainSetFile2)
    print(len(dataset2))
    dataset3=appendToDatasetNoGender(dataset2,trainSetFile3)
    print(len(dataset3))
    dataset4=appendToDatasetNoGender(dataset3,trainSetFile4)
    print(len(dataset4))
    dataset5=appendToDatasetNoGender(dataset4,trainSetFile5)
    print(len(dataset5))
    dataset6=appendToDatasetNoGender(dataset5,trainSetFile6)
    print(len(dataset6))
    dataset7=appendToDatasetNoGender(dataset6,trainSetFile7)
    print(len(dataset7))
    dataset8=appendToDatasetNoGender(dataset7,trainSetFile8)
    print(len(dataset8))
    dataset9=appendToDatasetNoGender(dataset8,trainSetFile9)
    print(len(dataset9))
    dataset10=appendToDatasetNoGender(dataset9,trainSetFile10)
    print(len(dataset10))
    dataset11=appendToDatasetNoGender(dataset10,trainSetFile11)
    print(len(dataset11))
    dataset12=appendToDatasetNoGender(dataset11,trainSetFile12)
    print(len(dataset12))
    ChowLiuTree5Var(dataset12)
    return

def naiveBayesGender():
    trainSetFile1  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201601-citibike-tripdata.csv'
    trainSetFile2  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201602-citibike-tripdata.csv'
    trainSetFile3  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201603-citibike-tripdata.csv'
    trainSetFile4  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201604-citibike-tripdata.csv'
    trainSetFile5  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201605-citibike-tripdata.csv'
    trainSetFile6  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201606-citibike-tripdata.csv'
    trainSetFile7  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201607-citibike-tripdata.csv'
    trainSetFile8  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201608-citibike-tripdata.csv'
    trainSetFile9  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201609-citibike-tripdata.csv'
    trainSetFile10 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201610-citibike-tripdata.csv'
    trainSetFile11 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201611-citibike-tripdata.csv'
    trainSetFile12 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201612-citibike-tripdata.csv'
    dataset1 = loadCsvClassified(trainSetFile1)
    print(len(dataset1))
    dataset2=appendToDataset(dataset1,trainSetFile2)
    print(len(dataset2))
    dataset3=appendToDataset(dataset2,trainSetFile3)
    print(len(dataset3))
    dataset4=appendToDataset(dataset3,trainSetFile4)
    print(len(dataset4))
    dataset5=appendToDataset(dataset4,trainSetFile5)
    print(len(dataset5))
    dataset6=appendToDataset(dataset5,trainSetFile6)
    print(len(dataset6))
    dataset7=appendToDataset(dataset6,trainSetFile7)
    print(len(dataset7))
    dataset8=appendToDataset(dataset7,trainSetFile8)
    print(len(dataset8))
    dataset9=appendToDataset(dataset8,trainSetFile9)
    print(len(dataset9))
    dataset10=appendToDataset(dataset9,trainSetFile10)
    print(len(dataset10))
    dataset11=appendToDataset(dataset10,trainSetFile11)
    print(len(dataset11))
    dataset12=appendToDataset(dataset11,trainSetFile12)
    print(len(dataset12))
    testSetFile = '/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201703-citibike-tripdata.csv'
    testset = loadCsvClassified(testSetFile)
    print(len(testset))
    naiveBayes(dataset12,testset)
    return

def naiveBayesAge():
    trainSetFile1  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201601-citibike-tripdata.csv'
    trainSetFile2  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201602-citibike-tripdata.csv'
    trainSetFile3  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201603-citibike-tripdata.csv'
    trainSetFile4  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201604-citibike-tripdata.csv'
    trainSetFile5  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201605-citibike-tripdata.csv'
    trainSetFile6  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201606-citibike-tripdata.csv'
    trainSetFile7  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201607-citibike-tripdata.csv'
    trainSetFile8  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201608-citibike-tripdata.csv'
    trainSetFile9  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201609-citibike-tripdata.csv'
    trainSetFile10 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201610-citibike-tripdata.csv'
    trainSetFile11 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201611-citibike-tripdata.csv'
    trainSetFile12 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201612-citibike-tripdata.csv'
    dataset1 = loadCsvClassifiedNaiveAge(trainSetFile1)
    print(len(dataset1))
    dataset2=appendToDatasetNaiveAge(dataset1,trainSetFile2)
    print(len(dataset2))
    dataset3=appendToDatasetNaiveAge(dataset2,trainSetFile3)
    print(len(dataset3))
    dataset4=appendToDatasetNaiveAge(dataset3,trainSetFile4)
    print(len(dataset4))
    dataset5=appendToDatasetNaiveAge(dataset4,trainSetFile5)
    print(len(dataset5))
    dataset6=appendToDatasetNaiveAge(dataset5,trainSetFile6)
    print(len(dataset6))
    dataset7=appendToDatasetNaiveAge(dataset6,trainSetFile7)
    print(len(dataset7))
    dataset8=appendToDatasetNaiveAge(dataset7,trainSetFile8)
    print(len(dataset8))
    dataset9=appendToDatasetNaiveAge(dataset8,trainSetFile9)
    print(len(dataset9))
    dataset10=appendToDatasetNaiveAge(dataset9,trainSetFile10)
    print(len(dataset10))
    dataset11=appendToDatasetNaiveAge(dataset10,trainSetFile11)
    print(len(dataset11))
    dataset12=appendToDatasetNaiveAge(dataset11,trainSetFile12)
    print(len(dataset12))
    testSetFile = '/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201703-citibike-tripdata.csv'
    testset = loadCsvClassifiedNaiveAge(testSetFile)
    print(len(testset))
    naiveBayes(dataset12,testset)
    return

def naiveBayesEnd():
    trainSetFile1  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201601-citibike-tripdata.csv'
    trainSetFile2  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201602-citibike-tripdata.csv'
    trainSetFile3  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201603-citibike-tripdata.csv'
    trainSetFile4  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201604-citibike-tripdata.csv'
    trainSetFile5  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201605-citibike-tripdata.csv'
    trainSetFile6  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201606-citibike-tripdata.csv'
    trainSetFile7  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201607-citibike-tripdata.csv'
    trainSetFile8  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201608-citibike-tripdata.csv'
    trainSetFile9  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201609-citibike-tripdata.csv'
    trainSetFile10 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201610-citibike-tripdata.csv'
    trainSetFile11 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201611-citibike-tripdata.csv'
    trainSetFile12 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201612-citibike-tripdata.csv'
    dataset1 = loadCsvClassifiedNaiveEnd(trainSetFile1)
    print(len(dataset1))
    dataset2=appendToDatasetNaiveEnd(dataset1,trainSetFile2)
    print(len(dataset2))
    dataset3=appendToDatasetNaiveEnd(dataset2,trainSetFile3)
    print(len(dataset3))
    dataset4=appendToDatasetNaiveEnd(dataset3,trainSetFile4)
    print(len(dataset4))
    dataset5=appendToDatasetNaiveEnd(dataset4,trainSetFile5)
    print(len(dataset5))
    dataset6=appendToDatasetNaiveEnd(dataset5,trainSetFile6)
    print(len(dataset6))
    dataset7=appendToDatasetNaiveEnd(dataset6,trainSetFile7)
    print(len(dataset7))
    dataset8=appendToDatasetNaiveEnd(dataset7,trainSetFile8)
    print(len(dataset8))
    dataset9=appendToDatasetNaiveEnd(dataset8,trainSetFile9)
    print(len(dataset9))
    dataset10=appendToDatasetNaiveEnd(dataset9,trainSetFile10)
    print(len(dataset10))
    dataset11=appendToDatasetNaiveEnd(dataset10,trainSetFile11)
    print(len(dataset11))
    dataset12=appendToDatasetNaiveEnd(dataset11,trainSetFile12)
    print(len(dataset12))
    testSetFile = '/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201703-citibike-tripdata.csv'
    testset = loadCsvClassifiedNaiveEnd(testSetFile)
    print(len(testset))
    naiveBayes(dataset12,testset)
    return

def naiveBayesStart():
    trainSetFile1  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201601-citibike-tripdata.csv'
    trainSetFile2  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201602-citibike-tripdata.csv'
    trainSetFile3  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201603-citibike-tripdata.csv'
    trainSetFile4  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201604-citibike-tripdata.csv'
    trainSetFile5  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201605-citibike-tripdata.csv'
    trainSetFile6  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201606-citibike-tripdata.csv'
    trainSetFile7  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201607-citibike-tripdata.csv'
    trainSetFile8  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201608-citibike-tripdata.csv'
    trainSetFile9  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201609-citibike-tripdata.csv'
    trainSetFile10 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201610-citibike-tripdata.csv'
    trainSetFile11 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201611-citibike-tripdata.csv'
    trainSetFile12 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201612-citibike-tripdata.csv'
    dataset1 = loadCsvClassifiedNaiveStart(trainSetFile1)
    print(len(dataset1))
    dataset2=appendToDatasetNaiveStart(dataset1,trainSetFile2)
    print(len(dataset2))
    dataset3=appendToDatasetNaiveStart(dataset2,trainSetFile3)
    print(len(dataset3))
    dataset4=appendToDatasetNaiveStart(dataset3,trainSetFile4)
    print(len(dataset4))
    dataset5=appendToDatasetNaiveStart(dataset4,trainSetFile5)
    print(len(dataset5))
    dataset6=appendToDatasetNaiveStart(dataset5,trainSetFile6)
    print(len(dataset6))
    dataset7=appendToDatasetNaiveStart(dataset6,trainSetFile7)
    print(len(dataset7))
    dataset8=appendToDatasetNaiveStart(dataset7,trainSetFile8)
    print(len(dataset8))
    dataset9=appendToDatasetNaiveStart(dataset8,trainSetFile9)
    print(len(dataset9))
    dataset10=appendToDatasetNaiveStart(dataset9,trainSetFile10)
    print(len(dataset10))
    dataset11=appendToDatasetNaiveStart(dataset10,trainSetFile11)
    print(len(dataset11))
    dataset12=appendToDatasetNaiveStart(dataset11,trainSetFile12)
    print(len(dataset12))
    testSetFile = '/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201703-citibike-tripdata.csv'
    testset = loadCsvClassifiedNaiveStart(testSetFile)
    print(len(testset))
    naiveBayes(dataset12,testset)
    return
     

def main():
    """
    outputFile='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/CS6347_Hw5/student_test_processed.data'
    inputFile='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/CS6347_Hw5/student_test.data'
    preProcessData(inputFile,outputFile)
    
    outputFile='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/CS6347_Hw5/student_train_processed.data'
    inputFile='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/CS6347_Hw5/student_train.data'
    preProcessData(inputFile,outputFile)
    """

    #trainSetFile = '/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/201612CitiTrain.csv'
    #dataset = loadCsv(trainSetFile)
    #testSetFile = '/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/201612CitiTest.csv'
    #testset = loadCsv(testSetFile)
    #naiveBayes(dataset,testset)

    
    #trainSetFile = '/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/201612CitiTrain.csv'
    #trainSetFile = '/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/JC-201701-citibike-tripdata.csv'
    #classifiedDataset = loadCsvClassified(trainSetFile)
    #print(classifiedDataset)
    #print(len(classifiedDataset))
    #combimedDataset=loadMultipleCsv(trainSetFile,trainSetFile)
    #print(len(combimedDataset))
    #appendedDataset=appendToDataset(combimedDataset,trainSetFile)
    #print(len(appendedDataset))
    """ #NYU dataset
    trainSetFile1 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/201606-citibike-tripdata.csv'
    trainSetFile2 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/201602-citibike-tripdata.csv'
    trainSetFile3 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/201603-citibike-tripdata.csv'
    trainSetFile4 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/201604-citibike-tripdata.csv'
    trainSetFile5 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/201605-citibike-tripdata.csv'
    trainSetFile6 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/201606-citibike-tripdata.csv'
    """
    #JC dataset
    trainSetFile1  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201601-citibike-tripdata.csv'
    trainSetFile2  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201602-citibike-tripdata.csv'
    trainSetFile3  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201603-citibike-tripdata.csv'
    trainSetFile4  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201604-citibike-tripdata.csv'
    trainSetFile5  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201605-citibike-tripdata.csv'
    trainSetFile6  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201606-citibike-tripdata.csv'
    trainSetFile7  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201607-citibike-tripdata.csv'
    trainSetFile8  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201608-citibike-tripdata.csv'
    trainSetFile9  ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201609-citibike-tripdata.csv'
    trainSetFile10 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201610-citibike-tripdata.csv'
    trainSetFile11 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201611-citibike-tripdata.csv'
    trainSetFile12 ='/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201612-citibike-tripdata.csv'
    
    
    dataset1 = loadCsvClassified(trainSetFile1)
    print(dataset1)
    print(len(dataset1))
    
    """
    dataset2=appendToDataset(dataset1,trainSetFile2)
    print(len(dataset2))
    dataset3=appendToDataset(dataset2,trainSetFile3)
    print(len(dataset3))
    dataset4=appendToDataset(dataset3,trainSetFile4)
    print(len(dataset4))
    dataset5=appendToDataset(dataset4,trainSetFile5)
    print(len(dataset5))
    dataset6=appendToDataset(dataset5,trainSetFile6)
    print(len(dataset6))
    dataset7=appendToDataset(dataset6,trainSetFile7)
    print(len(dataset7))
    dataset8=appendToDataset(dataset7,trainSetFile8)
    print(len(dataset8))
    dataset9=appendToDataset(dataset8,trainSetFile9)
    print(len(dataset9))
    dataset10=appendToDataset(dataset9,trainSetFile10)
    print(len(dataset10))
    dataset11=appendToDataset(dataset10,trainSetFile11)
    print(len(dataset11))
    dataset12=appendToDataset(dataset11,trainSetFile12)
    print(len(dataset12))
    """
    #ChowLiuTree(dataset6)
    
    #print(len(dataset1))    
    testSetFile = '/Users/JC/Documents/UTD CS/CS6347_Statistical Methods in AI and Machine Learning/citibike rawdata/JC-201703-citibike-tripdata.csv'
    testset = loadCsvClassified(testSetFile)
    #testset = loadCsvClassifiedNaiveAge(testSetFile)
    #testset = loadCsvClassifiedNaiveEnd(testSetFile)
    #testset = loadCsvClassifiedNaiveStart(testSetFile)
    #print(testset)
    #print(len(testset))
    #ChowLiuTree(testset)
    #print(dataset1) 
    naiveBayes(dataset1,testset)
    #print(len(testset))
    #print(dataset1)
    
    
    
    ####### TERM PROJECT RESULT ####### 
    
    #ChowLiuTreeForJC20161sthalf()
    #ChowLiuTreeForJC20162ndhalf()
    #ChowLiuTreeForJC2016()
    #ChowLiuTreeForJC2016NoHour()
    #ChowLiuTreeForJC2016NoGender()
    
    #naiveBayesGender()
    #naiveBayesAge()
    #naiveBayesEnd()
    #naiveBayesStart()


    
    
main()