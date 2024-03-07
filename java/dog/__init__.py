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
    """MealTip.java exists"""
    check50.exists("MealTip.java")

@check50.check(exists)
def compiles():
    """Dog.java compiles"""
    out = check50.run("javac -d ./ Dog.java").stdout(timeout = 60)
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
    """Dog.java has a dogYears method that works alright"""
    check50.include("TestDogYears.java","TestPrintDog.java")
    out = check50.run("javac -d ./ TestDogYears.java").stdout(timeout = 60)
    age = 4
    check50.run("java TestDogYears 2>&1").stdin(str(age)).stdout(str(age*7),timeout = 30)

@check50.check(runs)
def printdog():
    """Dog.java has a printDog method that works alright"""
    out = check50.run("javac -d ./ TestPrintDog.java").stdout(timeout = 60)
    check50.log(out)
    age = 9
    out = check50.run("java TestPrintDog 2>&1").stdin("Rocket").stdin("123.2").stdin(str(age)).stdin("Standard Poodle").stdout(timeout = 30)

    if not ("Rocket" in out and "123.2" in out and str(age*7) in out and "Standard Poodle" in out):
        raise check50.Mismatch(f"Rocket (a Standard Poodle) weighs 123.2 lbs, is {age*7} in dog years, and is a good doggy", out.strip())
