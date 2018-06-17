# -*- coding: UTF-8 -*-
'''
Created on 2018年6月17日

@author: luke
'''

import argparse
import os

prog='rateldu'
usage='%(prog)s [directory] [options]'
description='Summarize disk usage of each FILE, based on ncdu command, default unit is Byte. Default directory is current directory.'
epilog='SIZE is an integer and optional unit (example: 10M is 10*1024*1024).  Units are K, M, G, T, P, E, Z, Y \
            (powers of 1024) or KB, MB, ... (powers of 1000).'
argument_default=argparse.SUPPRESS

def ncdu(pwd, exclude):
    if exclude == None:
        cmd = "ncdu -o- " + pwd
        ncdudata = os.popen(cmd).read()
        return ncdudata
    else:
        cmd = "ncdu -o- " + pwd + " --exclude=" + exclude
        ncdudata = os.popen(cmd).read()
        return ncdudata

def sortdata(ncdudata, humanr):
    if humanr == None:
        return ncdudata
    else:
        return ncdudata

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=prog, usage=usage, description=description, epilog=epilog,\
                                     argument_default=argument_default)
    parser.add_argument('-s', '--sort-number', type=int, action='store', dest="s", default=0, help='default sort by file size, display the first number files after sorted by size (-s5)')
    parser.add_argument('-u', '--human-readable', action='store_true', dest="u", default=False, help='print sizes in human readable format (e.g., 1K 234M 2G)')
    parser.add_argument("-o", "--output", action='store', dest="o", default=None, help='export scanned directory to FILE')
    parser.add_argument("-x", "--exclude", action='store', dest="e", default=None, help='exclude files that match PATTERN')
    currentpwd = os.getcwd()
    parser.add_argument("d", nargs='?', default=currentpwd, help='test')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
    
    args = parser.parse_args()
    
    pwd = args.d
    sortn = args.s
    humanr = args.u
    outputfile = args.o
    exclude = args.e
    
    print(pwd, sortn, humanr, outputfile, exclude)
    
    ncdudata = ncdu(pwd, exclude)
    print(ncdudata)
    
    sortdata = sortdata(ncdudata, humanr)
    
    if outputfile == None:
        if sortn == 0:
            print(sortdata)
        else:
            print(sortdata[sortn])
    else:
        f = open(outputfile, 'w')
        if sortn == 0:
            f.write(sortdata)
            f.close()
        else:
            f.write(sortdata[sortn])
            f.close()       
        