# -*- coding:utf-8 -*-
#  def triangles():
#     b = [1]
#
#     while len(b) <= n:
#         yield b
#         b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
#
#
# n = 0
# for t in triangles():
#     print t
#     n += 1
#     if n == 10:
#         break
# b=[1,1]
# for i in range(len(b) - 1):
#     a=b[i]
#     c=b[i+1]
#     print (a+c)
_author_='fortest'
import sys
import os
from datetime import datetime

def myDirList():
    currpath=os.path.abspath('')
    print ("---%s----" % currpath)
    for f in os.listdir(currpath):
        fsize=os.path.getsize(f)
        mtime=datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
        if os.path.isdir(f):
            print('%10d %s <dir> %s' % (fsize,mtime,f))

if(__name__=="__main__"):
    if 0==len(sys.argv):
        print("")
    elif 1<=len(sys.argv):
        if '-l'==sys.argv[1].lower():
            myDirList()
        elif '-?' == sys.argv[1].lower() or '-h' == sys.argv[1].lower():
            print("            -l            显示目录列表")
            print("            -?/-h         显示帮助信息")
        else:
            print("无效的参数，请输入-？或-h参数来获取帮助信息！")