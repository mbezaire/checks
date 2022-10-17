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
    """LunchTime.java exists"""
    check50.exists("LunchTime.java")

@check50.check(exists)
def compiles():
    """LunchTime.java compiles"""
    out = check50.run("javac -d ./ LunchTime.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """LunchTime.java computes 9:45 as 195 minutes until lunch"""
    check50.run("java LunchTime").stdin("09:45").stdout("195", timeout = 60)
    # if len(out2) < 60 or 'border' not in out2:
    #     raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    # else:
    #     check50.log(out2)


@check50.check(compiles)
def runscloser():
    """LunchTime.java computes 11:00 as 120 minutes until lunch"""
    check50.run("java LunchTime").stdin("11:00").stdout("120", timeout = 60)


@check50.check(compiles)
def runsclosest():
    """LunchTime.java computes 12:14 as 46 minutes until lunch"""
    check50.run("java LunchTime").stdin("12:14").stdout("46", timeout = 60)


@check50.check(compiles)
def runtime():
    """LunchTime.java computes 12:59 as 1 minute until lunch"""
    check50.run("java LunchTime").stdin("12:59").stdout("1", timeout = 60)

@check50.check(compiles)
def myclient():
    """minutesUntilLunch method works as expected"""
    check50.include("OtherClient.java")
    out = check50.run("javac -d ./ OtherClient.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
    else:
        check50.run("java OtherClient").stdout("331", timeout = 60)
