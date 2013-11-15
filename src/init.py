#!python
# filename : init.py
# initialization for kanjic2j

def init():
	import cPickle as cp
	print 'input'
	fin=file('kanjic2j/xjc.dat')
	xjc=cp.load(fin)
	fin.close()
	xcj={}
	for ja,ch in xjc.items():
		if xcj.has_key(ch):
			xcj[ch].append(ja)
		else:
			xcj[ch]=[ja]
	print 'output'
	fout=file('kanjic2j/xcj.dat','wb')
	cp.dump(xcj,fout)
	fout.close()
	print 'Done.'

if __name__=='__main__':
	init()

