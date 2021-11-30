# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """decode.c exists"""
    check50.exists("decode.c")

@check50.check(exists)
def compiles():
    """decode.c compiles"""
    check50.c.compile("decode.c", lcs50=True)

@check50.check(compiles)
def spacey_word():
    """A phrase is decoded"""
    check50.run("./decode").stdin("caae sswc Auel Ppsa ieos srms").stdout("csAPisasuperawesomeclass", "csAPisasuperawesomeclass\n").exit(0)

@check50.check(compiles)
def short_phrase():
    """Another phrase is decoded"""
    check50.run("./decode").stdin("tid osa dtz ao zn").stdout("todazistondaz", "todayismonday\n").exit(0)