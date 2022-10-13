# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

check50.include("testmylib.c") #, "testmylibvowel.c", "testmylibconsonant.c" ])

@check50.check()
def exists():
    """mylib.c exists"""
    check50.exists("mylib.c")

@check50.check(exists)
def compiles():
    """mylib.c compiles"""
    check50.c.compile("mylib.c", lcs50=True)

@check50.check(compiles)
def mylib():
    """mylib contains isvowel and isconsonant"""
    check50.include("testmylib.c","testmylibvowel.c", "testmylibconsonant.c")
    check50.c.compile("testmylib.c", lcs50=True)
    check50.c.compile("testmylibvowel.c", lcs50=True)
    check50.c.compile("testmylibcons.c", lcs50=True)
    check50.run("./testmylib").stdin("u").stdin("u").stdout("okay", "okay\n").exit(0)

@check50.check(mylib)
def isvowelyes():
    """isvowel returns 1 for vowel chars"""
    check50.run("./testmylibvowel").stdin("u").stdout("1", "1\n").exit(0)

@check50.check(mylib)
def isvowelno():
    """isvowel returns 0 for nonvowel chars"""
    check50.run("./testmylibvowel").stdin("z").stdout("0", "0\n").exit(0)

@check50.check(mylib)
def isconsonantyes():
    """isconsonant returns 1 for consonant chars"""
    check50.run("./testmylibcons").stdin("z").stdout("1", "1\n").exit(0)

@check50.check(mylib)
def isconsonantno():
    """isconsonant returns 0 for nonconsonant chars"""
    check50.run("./testmylibcons").stdin("a").stdout("0", "0\n").exit(0)

@check50.check(mylib)
def isconsonantnope():
    """isconsonant returns 0 for numeric chars"""
    check50.run("./testmylibcons").stdin("5").stdout("0", "0\n").exit(0)
