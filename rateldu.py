# -*- coding: UTF-8 -*-
'''
Created on 2018年6月17日

@author: luke
'''

import argparse
import os
import math
import json
import sys


#call ncdu command
def ncdu(pwd, exclude):
    try:
        if exclude == None:
            cmd = "ncdu -o- " + pwd
            ncdudata = os.popen(cmd).read()
            return json.loads(ncdudata)
        else:
            cmd = "ncdu -o- " + pwd + " --exclude=" + exclude
            ncdudata = os.popen(cmd).read()
            return json.loads(ncdudata)
    except Exception as e:
        return None
        print(e)

def dictdata(data, rootd, rdata):
    try:
        if rootd == data['name'] or 'asize' not in data.keys() or data['name'] == "kcore":
            pass
        else:
            s = {'asize': data['asize'], 'name': rootd + "/" + data['name']}
            rdata.append(s)            
    except Exception as e:
        print(e)     
        
def listdata(data, rootd, rdata):
    try:
        for i in range(len(data)):
            if type(data[i]) == list:
                listdata(data[i], rootd, rdata)
            elif type(data[i]) == dict:
                if i == 0 and "excluded" not in data[i]:
                    if rootd == "/":
                        rootd = rootd + data[i]['name']
                    else:
                        rootd = rootd + "/" + data[i]['name']
                else:       
                    dictdata(data[i], rootd, rdata)
    except Exception as e:
        print(e)     

#sort data without convert file size unit
def sortdata(ncdudata):
    try:
        data = list(ncdudata)[3]
        rootd = data[0]['name']
        rdata = []
        
        for i in range(len(data)):
            if type(data[i]) == list:
                listdata(data[i], rootd, rdata)
            else: 
                if "excluded" in data[i]:
                    pass
                else:
                    dictdata(data[i], rootd, rdata)
        
        rdata.sort(key=lambda k: (k.get('asize', 0)), reverse=True)
        
        return rdata
    except Exception as e:
        return None
        print(e) 

def isncdu():
    try:
        cmd = "ncdu -v"
        ret = os.popen(cmd).read()
        if ret == "":
            #cmd = "yum install -y ncdu"
            print("Please install ncdu command first, you can use 'yum install -y ncdu' or https://dev.yorhel.nl/ncdu")
            return False
        else:
            #print("ncdu command is installed.")
            return True
    except Exception as e:
        print(e)    

#initialize argparse
def argparseconn():
    #argparse.ArgumentParser parameter
    prog='rateldu'
    usage='%(prog)s [directory] [options]'
    description='Summarize disk usage of each FILE, based on ncdu command, default unit is Byte. Default directory is current directory.'
    epilog='SIZE is an integer and optional unit (example: 10M is 10*1024*1024).  Units are K, M, G, T, P, E, Z, Y \
                (powers of 1024) or KB, MB, ... (powers of 1000).'
    argument_default=argparse.SUPPRESS
    
    try:
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
        return args
    except Exception as e:
        print(e)         

#conver file size unit
def convertBytes(byte, sizetype):
    i = int(math.floor(math.log(byte, 1024)))

    if i >= len(sizetype):
        i = len(sizetype) - 1
    return ('%.2f' + " " + sizetype[i]) % (byte / math.pow(1024, i)) 

def main():
    #check ncdu command
    if not isncdu():
        sys.exit(1)
    
    #get parameters from command line
    args = argparseconn()
    print(args)
    pwd = args.d
    sortn = args.s
    humanr = args.u
    outputfile = args.o
    exclude = args.e
    
    #print(pwd, sortn, humanr, outputfile, exclude)
    
    #get ncdu data, dealing with exclude, delete file name is /proc/kcore from ncdudata
    ncdudata = ncdu(pwd, exclude)
    if not ncdudata:
        sys.exit(2)

    #sort data
    sortncdata = sortdata(ncdudata)
    if not sortncdata:
        sys.exit(3)

    #humanreadable
    sizetype = ['B', 'KB', 'MB', 'GB', 'TB']
    for i in sortncdata:
        if humanr == False:
            pass
        else:
            i['asize'] = convertBytes(i['asize'], sizetype=sizetype)

    #output, stdout or file, all or the forst N row
    if outputfile == None:
        if sortn == 0:
            for i in sortncdata:
                print("%-9s %s" % (i['asize'], i['name']))
        else:
            for i in sortncdata[0:sortn]:
                print("%-9s %s" % (i['asize'], i['name']))
    else:
        f = open(outputfile, 'w')
        if sortn == 0:
            for i in sortncdata:
                f.write(str("%-9s %s\n" % (i['asize'], i['name'])))
            f.close()
        else:
            for i in sortncdata[0:sortn]:
                f.write(str("%-9s %s\n" % (i['asize'], i['name'])))
            f.close()      
    
    print("\nToal file: %s" % (len(sortncdata)))
    
if __name__ == "__main__":
     main()