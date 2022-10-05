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
    """Grade.java exists"""
    check50.exists("Grade.java")

@check50.check(exists)
def compiles():
    """Grade.java compiles"""
    out = check50.run("javac -d ./ Grade.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """Grade.java gives an A for a grade of 94"""
    check50.run("java Grade").stdin("94").stdout("A", timeout = 60)
    # if len(out2) < 60 or 'border' not in out2:
    #     raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    # else:
    #     check50.log(out2)


@check50.check(compiles)
def runs60():
    """Grade.java gives a D for a grade of 60"""
    check50.run("java Grade").stdin("60").stdout("D", timeout = 60)        

@check50.check(compiles)
def runs59():
    """Grade.java gives an F for a grade of 59"""
    check50.run("java Grade").stdin("59").stdout("F", timeout = 60)        
 
@check50.check(compiles)
def runs89():
    """Grade.java gives a B for a grade of 89"""
    check50.run("java Grade").stdin("89").stdout("B", timeout = 60)        
 
@check50.check(compiles)
def runs90():
    """Grade.java gives a C for a grade of 70"""
    check50.run("java Grade").stdin("70").stdout("C", timeout = 60)
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