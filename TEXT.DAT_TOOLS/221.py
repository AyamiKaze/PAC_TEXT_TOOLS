#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import re

rootdir = os.getcwd()
dirlist = os.listdir(rootdir+"\\DUBLE")
for inpdir in dirlist:
    try:
        inp = open('DUBLE\\TEXT_duble_line.txt','r',encoding='gbk', errors='replace')
        label = 0
        out = open('CN_OUT\\'+'TEXT_CHS'+'.txt','w',encoding='gbk', errors='replace')
        while 1:
            line = inp.readline()
            if line=='':
                break
            if line=='\n':
                label+=1
                continue
            line = line.replace('\n','')
            line_check = re.match('★',line)
            if line_check:
                del line
            else:
                out.write(line+'\n')
    finally:
        inp.close()
        out.close()

print('success')
