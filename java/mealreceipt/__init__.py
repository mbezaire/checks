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
    """MealReceipt.java exists"""
    check50.exists("MealReceipt.java")

@check50.check(exists)
def compiles():
    """MealReceipt.java compiles"""
    out = check50.run("javac -d ./ MealReceipt.java").stdout(timeout = 60)
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
    """MealReceipt.java calculates the correct tip amounts"""
    dollars = random.randint(5,500)
    cents = random.randint(0,99)/100
    mealcost = dollars + cents
    out = check50.run("java MealReceipt").stdin(str(mealcost)).stdout()
    checkers = ['tip','receipt','total','15%','20%', '25%', '$'+str(0.15*mealcost), '$'+str(0.2*mealcost), '$'+str(0.25*mealcost), '$'+str(mealcost)]
    for num in checkers:
        if num not in out.lower():
            raise check50.Mismatch("Expected tips calculated for 15%, 20%, and 25%", out.strip(), help="Make sure to include percentage labels for each tip, dollar signs in front of the prices, the words 'Tip', 'Total', and 'Receipt' in your print outs")
