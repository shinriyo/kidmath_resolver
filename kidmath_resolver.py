#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


argvs = sys.argv
argc = len(argvs)

if not argc == 2:
    print('put argument')

# I have no idea that 4 is 0/1
mapper = {'0':1, '1':0, '2':0, '3':0, '4':0, '5':0, '6':1, '7':0, '8':2, '9':1}
res = 0
for x in str(argvs[1]):
#    print x
    res += int(mapper[x])

print(res)

