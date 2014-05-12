#!python
# -*- coding: utf-8 -*-
# filename: kanjic2j/web_lyrics.py
# special for web lyrics

from .lyrics import *


class WebLyrics(Lyrics):
    __hightlight = "<span class='hred'>%s</span>"

    def worksent(self, mstr):
        xtmp = []
        for l in xrange(0, len(mstr)):
            qtmp = Lyrics.workdanji(mstr[l])
            if len(qtmp) > 1:
                xtmp.append(__hightlight % qtmp[0])
            else:
                xtmp.append(qtmp[0])
        return u''.join(xtmp)

