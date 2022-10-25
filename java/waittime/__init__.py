# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c

classname = 'WaitTime'

@check50.check()
def exists():
    """Program file exists"""
    check50.exists(f"{classname}.java")

@check50.check(exists)
def compiles():
    """Program compiles"""
    out = check50.run(f"javac -d ./ {classname}.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """Program should say wait time is 2 hours and 30 minutes"""
    check50.run(f"java {classname}").stdin("6").stdin("30").stdin("9").stdin("00").stdout("2 hours and 30 minutes", timeout = 60)

@check50.check(compiles)
def runs60():
    """Program should say wait time is 3 hours and 59 minutes"""
    check50.run(f"java {classname}").stdin("6").stdin("30").stdin("10").stdin("29").stdout("3 hours and 59 minutes", timeout = 60)

@check50.check(compiles)
def runs59():
    """Program should say wait time is 0 hours and 44 minutes"""
    check50.run(f"java {classname}").stdin("2").stdin("51").stdin("3").stdin("37").stdout("0 hours and 44 minutes", timeout = 60)
 
@check50.check(compiles)
def runs89():
    """Program should say wait time is 0 hours and 0 minutes"""
    check50.run(f"java {classname}").stdin("3").stdin("11").stdin("3").stdin("11").stdout("0 hours and 0 minutes", timeout = 60)

