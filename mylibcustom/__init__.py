# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

# check50.include("testmylib.c") #, "testmylibvowel.c", "testmylibconsonant.c" ])

@check50.check()
def exists():
    """files were submitted - will be graded manually"""
    check50.exists("mylib.c")
    check50.exists("mylib.h")
    check50.exists("MyLibrary.md")

@check50.check(exists)
def mylib():
    """mylib compiles"""
    check50.include("testmylib.c")
    check50.run("clang -c mylib.c").exit(0)
    check50.run("clang testmylib.c -lcs50 mylib.o -o testmylib").exit(0)
