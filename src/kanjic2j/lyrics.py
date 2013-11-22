#!python
# -*- coding: utf-8 -*-
# filename: kanjic2j/lyrics.py
# special for lyrics

from core import *
class Lyrics(Kjfile):
	__kanas=[
		u"ん",u"ン",
		u"わ",u"ワ",u"ら",u"ラ",u"や",u"ヤ",u"ま",u"マ",u"は",u"ハ",
		u"な",u"ナ",u"た",u"タ",u"さ",u"サ",u"か",u"カ",u"あ",u"ア",
		u"ゐ",u"ヰ",u"り",u"リ",u"み",u"ミ",u"ひ",u"ヒ",u"に",u"ニ",
		u"ち",u"チ",u"し",u"シ",u"き",u"キ",u"い",u"イ",
		u"る",u"ル",u"ゆ",u"ユ",u"む",u"ム",u"ふ",u"フ",u"ぬ",u"ヌ",
		u"つ",u"ツ",u"す",u"ス",u"く",u"ク",u"う",u"ウ",
		u"ゑ",u"ヱ",u"れ",u"レ",u"め",u"メ",u"へ",u"ヘ",u"ね",u"ネ",
		u"て",u"テ",u"せ",u"セ",u"け",u"ケ",u"え",u"エ",
		u"を",u"ヲ",u"ろ",u"ロ",u"よ",u"ヨ",u"も",u"モ",u"ほ",u"ホ",
		u"の",u"ノ",u"と",u"ト",u"そ",u"ソ",u"こ",u"コ",u"お",u"オ"
		]
	__splitch=[
		'\n','/','.','(',')'
		u'。',u'（',u'）'
		]
	def __init__(self):
		Kjfile.__init__(self)
		self.__split()
	def __prepare(self):
		self.data=self.data.replace(self.linebreak,'\n')
		if self.data[len(self.data)-1]!='\n':
			self.data+='\n'
	def __findnext(self,now):
		t1=oo
		t2=''
		for ea in Lyrics.__splitch:
			xp=self.data.find(ea,now)
			if (xp>0)and(xp<t1):
				t1=xp
				t2=ea
		return t1,t2
	@staticmethod
	def __test(tmpstr):
		for ea in Lyrics.__kanas:
			if tmpstr.find(ea):
				return True
		return False

	def __split(self):
		self.__prepare()
		self.__tmpstr=[]
		self.__sps=['']
		self.__flags=[]
		u=0
		while True:
			v,sp=self.__findnext(u)
			if sp=='':
				break
			self.__tmpstr.append(self.data[u:v])
			self.__sps.append(sp)
			self.__flags.append(Lyrics.__test(self.__tmpstr[len(self.__tmpstr)]))
			u=v+1

	@staticmethod
	def worksent(mstr):
		xtmp=[]
		for l in xrange(0,len(mstr)):
			xtmp.append(Lyrics.workdanji(mstr[l])[0])
		return u''.join(xtmp)
	def work(self):
		ptmp=[]
		for i in xrange(0,len(self.__tmpstr)):
			ptmp.append(self.__sps[i])
			ptmp[i]+=Lyrics.worksent(self.__tmpstr[i]) if self.__flags[i] else self.__tmstr[i]
		return Kjfile(u''.join(ptmp))
		
