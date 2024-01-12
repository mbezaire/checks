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
    """ClassDay.java exists"""
    check50.exists("ClassDay.java")

@check50.check(exists)
def compiles():
    """ClassDay.java compiles"""
    out = check50.run("javac -d ./ ClassDay.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """ClassDay.java gives no class for B on Day 1"""
    out = check50.run("java ClassDay").stdin("1").stdin("B").stdout(timeout = 60)
    if "n't" not in out and "not" not in out and "no " not in out:
        raise check50.Mismatch("B doesn't meet today (or similar)", out)


@check50.check(compiles)
def runs2():
    """ClassDay.java gives period 3 for F on Day 5"""
    out = check50.run("java ClassDay").stdin("5").stdin("F").stdout(timeout = 60)
    if "3" not in out and "third" not in out:
        raise check50.Mismatch("F meets 3rd period today (or similar)", out)


@check50.check(compiles)
def runs3():
    """ClassDay.java gives period 5 for G on Day 7"""
    out = check50.run("java ClassDay").stdin("7").stdin("G").stdout(timeout = 60)
    if "5" not in out and "fifth" not in out:
        raise check50.Mismatch("G meets 5th period today (or similar)", out)



@check50.check(compiles)
def runs4():
    """ClassDay.java gives no class for block A on Day 2"""
    out = check50.run("java ClassDay").stdin("2").stdin("A").stdout(timeout = 60)
    if "n't" not in out and "not" not in out and "no " not in out:
        raise check50.Mismatch("A doesn't meet today (or similar)", out)
