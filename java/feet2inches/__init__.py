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
    """FeetToInches.java exists"""
    check50.exists("FeetToInches.java")

@check50.check(exists)
def compiles():
    """FeetToInches.java compiles"""
    out = check50.run("javac -d ./ FeetToInches.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """FeetToInches.java: 0 feet and 11 inches = 11 inches"""
    check50.run("java FeetToInches").stdin("0").stdin("11").stdout("11", timeout = 60)

@check50.check(compiles)
def runs5():
    """FeetToInches.java: 0 feet and 25 inches = 25 inches"""
    check50.run("java FeetToInches").stdin("0").stdin("25").stdout("25", timeout = 60)


@check50.check(compiles)
def runs60():
    """FeetToInches.java: 6 feet and 6 inches = 78 inches"""
    check50.run("java FeetToInches").stdin("6").stdin("6").stdout("78", timeout = 60)
 
@check50.check(compiles)
def runs89():
    """FeetToInches.java: 4 feet and 0 inches = 48 inches"""
    check50.run("java FeetToInches").stdin("4").stdin("0").stdout("48", timeout = 60)
 
@check50.check(compiles)
def runs90():
    """FeetToInches.java: 8 feet and 11 inches = 107 inches"""
    check50.run("java FeetToInches").stdin("8").stdin("11").stdout("107", timeout = 60)
    # if len(out2) < 60 or 'border' not in out2:
    #     raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    # else:
    #     check50.log(out2)
       
# @check50.check(compiles)
# def getvalue():
#     """Fraction value can be computed"""
#     out = check50.run("javac -d ./ F0Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
#     check50.run("java F0Client").stdin("1", prompt=False).stdin("4", prompt=False).stdout("0.25\n").exit(0)