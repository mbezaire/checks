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
    """LetterGrade.java exists"""
    check50.exists("LetterGrade.java")

@check50.check(exists)
def compiles():
    """LetterGrade.java compiles"""
    try: #     - !include Custom.java
        check50.run("javac -d ./ Custom.java")
    except:
        pass
    out = check50.run("javac -d ./ LetterGrade.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """LetterGrade.java gives an A for a grade of 94"""
    check50.run("java LetterGrade").stdin("94").stdout("A", timeout = 60)


@check50.check(compiles)
def runs60():
    """LetterGrade.java gives a D for a grade of 60"""
    check50.run("java LetterGrade").stdin("60").stdout("D", timeout = 60)        

@check50.check(compiles)
def runs59():
    """LetterGrade.java gives an F for a grade of 59"""
    check50.run("java LetterGrade").stdin("59").stdout("F", timeout = 60)        
 
@check50.check(compiles)
def runs89():
    """LetterGrade.java gives a B for a grade of 89"""
    check50.run("java LetterGrade").stdin("89").stdout("B", timeout = 60)        
 
@check50.check(compiles)
def runs90():
    """LetterGrade.java gives a C for a grade of 70"""
    check50.run("java LetterGrade").stdin("70").stdout("C", timeout = 60)
