#!python
# filename : test.py
# testing

def test1():
	import cPickle as cp
	q=file('kanjic2j/kanjic2j_xcj.dat')
	x=cp.load(q)
	def qt(t):
		for ea in x[t]:
			print ea,
		print
	for ea in x:
		if len(x[ea])>1:
			print ea+" -> ",
			qt(ea)
def test2():
	import kanjic2j as kj
	q=kj.file_open('test.txt')
	print q.data
	p=q.work()
	print p.data
	p.file_save('test_out.txt')
def test3():
	import kanjic2j as kj
	print kj.cur_file_dir()
exec('test'+raw_input()+'()')
