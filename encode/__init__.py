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
    out = check50.run("./encode").stdin("csAP  is    a super   awesome  class").stdout()
    if out.strip() != "caae sswc Auel Ppsa ieos srms":
        raise check50.Mismatch("caae sswc Auel Ppsa ieos srms\n", out, help='Can your code skip multiple spaces in a row?')

@check50.check(compiles)
def short_phrase():
    """A phrase is encoded"""
    out = check50.run("./encode").stdin("today is monday").stdout()
    if out.strip() != "tid osa dmy ao yn":
        raise check50.Mismatch("tid osa dmy ao yn\n", out, help='Mondays ARE tough')


@check50.check(compiles)
def other_phrase():
    """Another phrase is encoded"""
    out = check50.run("./encode").stdin("today is friday").stdout()
    if out.strip() != "tid osa dfy ar yi":
        raise check50.Mismatch("tid osa dfy ar yi\n", out, help='Hmm, better try again')
