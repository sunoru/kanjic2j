#!python
# filename : kanjic2j/core.py
# core of kanjic2j

import codecs
xcj=xjc={}
import sys,os

def init():
	global xcj,xjc
	print 'Initializing..'
	import cPickle as cp
	print 'Loading xcj..',
	f1=file(os.path.join(os.path.dirname(__file__),'xcj.dat'))
	xcj=cp.load(f1)
	f1.close()
	print 'Done!'
	print 'Loading xjc..',
	f1=file(os.path.join(os.path.dirname(__file__),'xjc.dat'))
	xjc=cp.load(f1)
	f1.close()
	print 'Done!'
try:
	init()
except:
	print 'Error!'

class Kjfile:
	global xcj
	mxcj=xcj
	def __init__(self,ain):
		if (type(ain)==str)or(type(ain)==file):
			self.file_open(ain)
		elif type(ain)==unicode:
			self.data=ain
		else:
			self.data=unicode('unknown input','utf-8')
		if self.data.find('\r\n'):
			self.linebreak='\r\n'
		elif self.data.find('\r'):
			self.linebreak='\r'
		else:
			self.linebreak='\n'
	def file_open(self,ain):
		if type(ain)==str:
			try:
				ain=codecs.open(ain,'r','utf-8')
				self.data=ain.read()
			except:
				ain=file(ain)
				self.data=unicode(ain.read(),'utf-8')
			finally:
				ain.close()
		else:
			self.data=unicode(ain.read(),'utf-8')
	def file_save(self,aout,linebreak=self.linebreak):
		if type(aout)==str:
			aout=codecs.open(aout,'w','utf-8')
			aout.write(self.data.replace(self.linebreak,linebreak))
			aout.close()
	@staticmethod
	def workdanji(ach):
		if Kjfile.mxcj.has_key(ach):
			return Kjfile.mxcj[ach]
		else:
			return ach
	def work(self):
		'''
		need to be override
		'''
		re=[]
		for i in xrange(0,len(self.data)):
			re.append(Kjfile.workdanji(self.data[i])[0])
			print self.data[i],re[i]
		return Kjfile(''.join(re))
def file_open(afile):
	return Kjfile(afile)

