# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

# check50.include("testmylib.c")

@check50.check()
def exists():
    """mylib.c and mylib.h exist"""
    check50.exists("mylib.c")
    check50.exists("mylib.h")

@check50.check(exists)
def mylib():
    """mylib contains mergesort"""
    check50.include("testmylib.c", "testmerge.c")
    check50.run("clang -c mylib.c").exit(0)
    check50.run("clang testmylib.c -lcs50 mylib.o -o testmylib").exit(0)
    check50.run("clang testmerge.c -lcs50 mylib.o -o testmerge").exit(0)
    check50.run("./testmylib").stdout("okay","okay\n").exit(0)

@check50.check(mylib)
def selsort():
    """mergesort sorts 3,1,8,4,7,3,1,5,0,13,-1 into -1,0,1,1,3,3,4,5,7,8,13,"""
    check50.run("./testmerge").stdout("-1,0,1,1,3,3,4,5,7,8,13,").exit(0)
