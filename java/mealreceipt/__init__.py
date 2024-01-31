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
    """MealReceipt.java prints the meal cost"""
    dollars = random.randint(5,500)
    cents = random.randint(0,99)/100
    mealcost = dollars + cents
    out = check50.run("java MealReceipt").stdin(str(mealcost)).stdout(timeout = 60)
    check50.log(out)
    if 'meal' not in out.lower() or '$' + str(mealcost) not in out:
        raise check50.Mismatch("Meal: $" + str(mealcost), out, help="Include the cost of the meal (without tax or tip) on the receipt, with a dollar sign in front, and a label that includes the word 'meal')
    return mealcost, out

@check50.check(runs)
def tax(mealcost, out):
    """MealReceipt.java calculates and prints the tax (tax rate should be 7%)"""
    tax = mealcost * 0.07
    if 'tax' not in out.lower() or '$' + str(tax) not in out:
        raise check50.Mismatch("Tax: $" + str(tax), out, help="Include the cost of the tax (calculated as the cost of the meal * 0.07) on the receipt, with a dollar sign in front, and a label that includes the word 'tax')
    return mealcost, out

@check50.check(runs)
def tip(mealcost, out):
    """MealReceipt.java calculates and prints the tip values for tip rates of 15%, 20%, 25%"""
    tiprates = [15, 20, 25]
    if 'tip' not in out.lower():
        raise check50.Mismatch("Tip:\n15% ...", out, help="Include the word 'Tip' on your receipt)
    for tiprate in tiprates:
        tip = tiprate/100 * mealcost
        if str(tiprate) + '%' not in out or '$' + str(tip) not in out:
            raise check50.Mismatch(f"{tiprate}% ${tip}", out, help=f"Include a labelled calculation for the tip with a tip rate of {tiprate}%")
