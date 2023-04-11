# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re
import random

@check50.check()
def exists():
    """Vowels.java exists"""
    check50.exists("Vowels.java")

@check50.check(exists)
def compiles():
    """Vowels.java compiles"""
    out = check50.run("javac -d ./ Vowels.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

@check50.check(compiles)
def runs():
    """Vowels.java calculates the correct number of vowels in awesome"""

    out = check50.run("java Vowels").stdin("awesome").stdout()
    findtemp = re.search(r'([0-9]+)', out)
    if findtemp != None:
        result = findtemp.groups()
    if int(result[0]) != 4:
        raise check50.Mismatch(4, out.strip())


@check50.check(compiles)
def runs2():
    """Vowels.java calculates the correct number of vowels in shhhh"""

    out = check50.run("java Vowels").stdin("shhhh").stdout()
    findtemp = re.search(r'([0-9]+)', out)
    if findtemp != None:
        result = findtemp.groups()
    if int(result[0]) != 0:
        raise check50.Mismatch(0, out.strip())


@check50.check(compiles)
def runs3():
    """Vowels.java calculates the correct number of vowels in aeiou"""

    out = check50.run("java Vowels").stdin("aeiou").stdout()
    findtemp = re.search(r'([0-9]+)', out)
    if findtemp != None:
        result = findtemp.groups()
    if int(result[0]) != 5:
        raise check50.Mismatch(5, out.strip())

