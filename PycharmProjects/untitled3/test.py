print('2111')
#coding=utf-8

import numpy as np
import os

cwd = os.getcwd()

txtFile1 = cwd + '/first.txt'
txtFile2 = cwd + '/second.txt'
mergeFile2 = cwd + '/mergeTXT.txt'


f = file(mergeFile2, 'a+')
for (index1, line1) in enumerate(open(txtFile1)):
    # print index1, line1
    for (index2, line2) in enumerate(open(txtFile2)):
        if index1 == index2:
            newline = line1 + line2 + '\n'
            f.write(newline)
f.close()