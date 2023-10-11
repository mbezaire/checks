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
    """TwoGrade.java exists"""
    check50.exists("TwoGrade.java")

@check50.check(exists)
def compiles():
    """TwoGrade.java compiles"""
    out = check50.run("javac -d ./ TwoGrade.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """TwoGrade.java gives an A for two strong grades"""
    check50.run("java TwoGrade").stdin("91 95").stdout("Student has an A", timeout = 60)
    # if len(out2) < 60 or 'border' not in out2:
    #     raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    # else:
    #     check50.log(out2)


@check50.check(compiles)
def runs60():
    """TwoGrade.java gives a fail for two low grades"""
    check50.run("java TwoGrade").stdin("50 55").stdout("Student failed", timeout = 60)        

@check50.check(compiles)
def runs59():
    """TwoGrade.java gives a fail if at least one grade is below 20"""
    check50.run("java TwoGrade").stdin("19 100").stdout("Student failed", timeout = 60)        
 
@check50.check(compiles)
def runs89():
    """TwoGrade.java gives a double average for other grades"""
    check50.run("java TwoGrade").stdin("50 90").stdout("Student has a 70.0 average", timeout = 60)        
