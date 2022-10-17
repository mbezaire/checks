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
    """LeapYear.java exists"""
    check50.exists("LeapYear.java")

@check50.check(exists)
def compiles():
    """LeapYear.java compiles"""
    out = check50.run("javac -d ./ LeapYear.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """LeapYear.java should say 1896 was a leap year"""
    check50.run("java LunchTime").stdin("1896").stdout("1896 was a leap year", timeout = 60)
    # if len(out2) < 60 or 'border' not in out2:
    #     raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    # else:
    #     check50.log(out2)


@check50.check(compiles)
def runs2():
    """LeapYear.java should say 1900 was not a leap year"""
    check50.run("java LunchTime").stdin("1900").stdout("1900 was not a leap year", timeout = 60)
    # if len(out2) < 60 or 'border' not in out2:
    #     raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    # else:
    #     check50.log(out2)


@check50.check(compiles)
def runs3():
    """LeapYear.java should say 2005 was not a leap year"""
    check50.run("java LunchTime").stdin("2005").stdout("2005 was not a leap year", timeout = 60)
    # if len(out2) < 60 or 'border' not in out2:
    #     raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    # else:
    #     check50.log(out2)


@check50.check(compiles)
def runs4():
    """LeapYear.java should say 2000 was a leap year"""
    check50.run("java LunchTime").stdin("2000").stdout("2000 was a leap year", timeout = 60)
    # if len(out2) < 60 or 'border' not in out2:
    #     raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    # else:
    #     check50.log(out2)
