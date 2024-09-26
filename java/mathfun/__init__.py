# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c

classname = 'MathFun'

@check50.check()
def exists():
    """Program file exists"""
    check50.exists(f"{classname}.java")

@check50.check(exists)
def compiles():
    """Program compiles"""
    out = check50.run(f"javac -d ./ {classname}.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """MathFun runs on 5"""
    output = "Your number is: 5\nHere are some facts about your number:\n\t- The cube of your number is: 125.0\n\t- The square root of your number is: 2.23606797749979\n\t- The square root of your number rounded to nearest 10th is: 2.2"
    check50.run(f"java {classname}").stdin("5").stdout(output, timeout = 60)


@check50.check(runs)
def runs2():
    """MathFun runs on -3"""
    output = "Your number is: 1\nHere are some facts about your number:\n\t- The cube of your number is: 1.0\n\t- The square root of your number is: 1.0\n\t- The square root of your number rounded to nearest 10th is: 1.0"
    check50.run(f"java {classname}").stdin("-3").stdout(output, timeout = 60)


@check50.check(runs)
def runs2():
    """MathFun runs on 10"""
    output = "Your number is: 10\nHere are some facts about your number:\n\t- The cube of your number is: 1000.0\n\t- The square root of your number is: 3.1622776601683795\n\t- The square root of your number rounded to nearest 10th is: 3.2"
    check50.run(f"java {classname}").stdin("10").stdout(output, timeout = 60)



@check50.check(runs)
def runs3():
    """MathFun runs on 13"""
    output = "Your number is: 10\nHere are some facts about your number:\n\t- The cube of your number is: 1000.0\n\t- The square root of your number is: 3.1622776601683795\n\t- The square root of your number rounded to nearest 10th is: 3.2"
    outputre = r"Your number is: ([0-9]+)\nHere are some facts about your number:\n\t- The cube of your number is: ([0-9\.]+)\n\t- The square root of your number is: ([0-9\.]+)\n\t- The square root of your number rounded to nearest 10th is: ([0-9\.]+)[\s\S]*"

    check50.run(f"java {classname}").stdin("13").stdout(outputre, output + "\nExpected something LIKE the example, doesn't have to use 10 necessarily", timeout = 60, regex=True)


@check50.check(runs3)
def runs4():
    """MathFun runs on 11"""
    output = check50.run(f"java {classname}").stdin("11").stdout()
    if 'Your number is: 0' in output:
        raise check50.Failure("uh oh, the number can only be 1 - 10, not 0!")