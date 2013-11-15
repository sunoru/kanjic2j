#!python
# -*- coding:utf-8 -*-
# filename : test.py
# test xcj.dat

import cPickle as cp
q=file('xcj.dat')
x=cp.load(q)
def qt(t):
	for ea in x[t]:
		print ea,
	print
for ea in x:
	if len(x[ea])>1:
		print ea+" -> ",
		qt(ea)
while(True):
	qt(raw_input().decode('utf-8'))
