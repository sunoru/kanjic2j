#!python
# -*- coding: utf-8 -*-
# filename: kanjic2j/lyrics.py
# special for lyrics

import core
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
	def __init__(self):
		Kjfile.__init__(self)
		self.__split()
	def __prepare(self):
		self.data=self.data.replace(self.linebreak,'\n')
	def __split(self):
		self.__prepare()
		self.__tmpstr=self.data.split('\n')
		self.__flags=[]
		for i in xrange(0,len(self.__tmpstr)):


	def work(self):
		pass
		
