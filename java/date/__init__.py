# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c


@check50.check()
def exists():
    """ConvertDate.java exists"""
    check50.exists("ConvertDate.java")

@check50.check(exists)
def compiles():
    """ConvertDate.java compiles"""
    out = check50.run("javac -d ./ ConvertDate.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)    

@check50.check(compiles)
def runs():
    """ConvertDate.java converts a 2 digit month and 2 digit day correctly"""
    check50.run("java ConvertDate").stdin("11/30/2023").stdout("30-11-2023", timeout = 60)

@check50.check(compiles)
def runs60():
    """ConvertDate.java converts a 2 digit month and 1 digit day correctly"""
    check50.run("java ConvertDate").stdin("12/1/2023").stdout("1-12-2023", timeout = 60)    

@check50.check(compiles)
def runs40():
    """ConvertDate.java converts a 1 digit month and 2 digit day correctly"""
    check50.run("java ConvertDate").stdin("9/18/2023").stdout("18-9-2023", timeout = 60)  

@check50.check(compiles)
def runs20():
    """ConvertDate.java preserves leading 0s"""
    check50.run("java ConvertDate").stdin("01/02/2024").stdout("02-01-2024", timeout = 60)           
