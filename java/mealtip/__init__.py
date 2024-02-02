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
    """MealTip.java compiles"""
    out = check50.run("javac -d ./ MealTip.java").stdout(timeout = 60)
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
    """MealTip.java calculates the correct cost"""
    dollars = random.randint(5,500)
    cents = random.randint(0,99)/100
    tip = random.randint(15,45)
    mealcost = dollars + cents
    check50.run("java MealTip 2>&1").stdin(str(mealcost)).stdin(str(tip)).stdout(timeout = 30).exit(0)
    out = check50.run("java MealTip 2>&1").stdin(str(mealcost)).stdin(str(tip)).stdout(timeout = 30)
    check50.log(out)
    findtemp = re.findall(r'([0-9]+.[0-9]+)', out)  # replace search with findall to find last
    if "Exception" in out:
        raise check50.Failure("There was an error with your code. Check that you are scanning in the meal cost as a double and the tip as an int.", help=out)
    if findtemp == None or len(findtemp) == 0:
        raise check50.Failure("Failed to find a decimal number in your printed output: " + out, help="Make sure to print out the total meal cost as a decimal number")
    result = findtemp # findtemp.groups()
    ans = mealcost*(1 + tip/100)
    if abs(float(result[-1]) - ans) > 0.0001:
        raise check50.Mismatch(ans, out.strip())
