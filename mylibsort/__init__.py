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
    """mylib.c and mylib.h exist"""
    check50.exists("mylib.c")
    check50.exists("mylib.h")

@check50.check(exists)
def mylib():
    """mylib contains selectionsort and bubblesort"""
    check50.include("testmylib.c","testselection.c", "testbubble.c")
    check50.run("clang -c mylib.c").exit(0)
    check50.run("clang testmylib.c -lcs50 mylib.o -o testmylib").exit(0)
    check50.run("clang testselection.c -lcs50 mylib.o -o testselection").exit(0)
    check50.run("clang testbubble.c -lcs50 mylib.o -o testbubble").exit(0)
    check50.run("./testmylib").stdin("u").stdout("okay","okay\n").exit(0)

@check50.check(mylib)
def isvowelyes():
    """selectionsort sorts 9,4,7,3,1 into 1,3,4,7,9"""
    check50.run("./testselection").stdout("1,3,4,7,9,").exit(0)

@check50.check(mylib)
def isvowelno():
    """bubblesort sorts 3,1,8,4,7,3,1 into 1,1,3,3,4,7,8"""
    check50.run("./testbubble").stdout("1,1,3,3,4,7,8,").exit(0)

@check50.check(mylib)
def isconsonantyes():
    """isconsonant returns 1 for consonant chars"""
    check50.run("./testmylibcons").stdin("Z").stdout("1").exit(0)

@check50.check(mylib)
def isconsonantno():
    """isconsonant returns 0 for nonconsonant chars"""
    check50.run("./testmylibcons").stdin("a").stdout("0").exit(0)

@check50.check(mylib)
def isconsonantnope():
    """isconsonant returns 0 for numeric chars"""
    check50.run("./testmylibcons").stdin("5").stdout("0").exit(0)
