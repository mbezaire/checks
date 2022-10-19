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
    """TenSwap.java exists"""
    check50.exists("TenSwap.java")

@check50.check(exists)
def compiles():
    """TenSwap.java compiles"""
    out = check50.run("javac -d ./ TenSwap.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """TenSwap.java swaps 3 to 30"""
    check50.run("java TenSwap").stdin("  3  ").stdout("30", timeout = 60)
    # if len(out2) < 60 or 'border' not in out2:
    #     raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    # else:
    #     check50.log(out2)


@check50.check(compiles)
def runs60():
    """TenSwap.java swaps 30 to 3"""
    check50.run("java TenSwap").stdin(" 30   ").stdout("3", timeout = 60)        

@check50.check(compiles)
def runs59():
    """TenSwap.java swaps 212 to 221"""
    check50.run("java TenSwap").stdin("    212  ").stdout("221", timeout = 60)        
 
@check50.check(compiles)
def runs89():
    """TenSwap.java swaps 1001 to 1010"""
    check50.run("java TenSwap").stdin("    1001  ").stdout("1010", timeout = 60)        
 
@check50.check(compiles)
def runs90():
    """TenSwap.java swaps 890 to 809"""
    check50.run("java TenSwap").stdin("890   ").stdout("809", timeout = 60)
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