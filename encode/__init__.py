# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """encode.c exists"""
    check50.exists("encode.c")

@check50.check(exists)
def compiles():
    """encode.c compiles"""
    check50.c.compile("encode.c", lcs50=True)

@check50.check(compiles)
def spacey_word():
    """A phrase with several spaces is encoded"""
    check50.run("./encode").stdin("csAP  is    a super   awesome  class").stdout("caae sswc Auel Ppsa ieos srms", "caae sswc Auel Ppsa ieos srms\n").exit(0)

@check50.check(compiles)
def short_phrase():
    """A phrase is encoded"""
    check50.run("./encode").stdin("today is monday").stdout("tid osa dmy ao yn\n", "tid osa dmy ao yn").exit(0)
