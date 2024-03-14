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
    check50.run("java TwoGrade").stdin("91").stdin("95").stdout("Student has an A", timeout = 60)

@check50.check(compiles)
def runs60():
    """TwoGrade.java gives a fail for two low grades"""
    check50.run("java TwoGrade").stdin("50").stdin("55").stdout("[Ss]tudent [Ff]ailed", timeout = 60, regex = True)        

@check50.check(compiles)
def runs59():
    """TwoGrade.java gives a fail if at least one grade is below 20"""
    check50.run("java TwoGrade").stdin("19").stdin("110").stdout("[Ss]tudent [Ff]ailed", timeout = 60, regex = True)        
 
@check50.check(compiles)
def runs89():
    """TwoGrade.java gives a double average for other grades"""
    check50.run("java TwoGrade").stdin("50").stdin("90").stdout("[Ss]tudent has a 70[\.0]* average", timeout = 60, regex = True)        
