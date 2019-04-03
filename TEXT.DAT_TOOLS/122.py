#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

rootdir = os.getcwd()
dirlist = os.listdir(rootdir+"\\JP_OUT")
for inpdir in dirlist:
    inp = open('JP_OUT\\'+inpdir,'r',encoding='gbk', errors='replace')
    out = open('DUBLE\\TEXT_duble_line.txt','w',encoding='gbk',errors='replace')
    try:
        label = 0
        while True:
            line = inp.readline()
            if line=='':
                break
            
            if line=='\n':
                label+=1
                continue
            
            line = line.replace('\n','')
            i = 1
            out.writelines('★'+"{:0>5d}".format(label)+'★'+line+'\n')
            out.writelines(line+'\n\n')
            label+=1
            
    finally:
        inp.close()
        out.close()
print('SUCCESS')
