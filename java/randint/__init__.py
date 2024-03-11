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
    """Custom.java exists"""
    check50.exists("Custom.java")

@check50.check(exists)
def compiles():
    """Custom.java compiles"""
    out = check50.run("javac -d ./ Custom.java").stdout(timeout = 60)
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
    """Custom.java has a randInt method that works alright"""
    check50.include("TestRandInt.java")
    checker = {"lower":0, 24:0, 25:0, 26:0, 27:0, 28:0, 29:0, 30:0, "bigger":0}
    put = check50.run("javac -d ./ TestRandInt.java").stdout(timeout = 60)
    check50.log(put)
    for trial in range(100):
        out = check50.run("java TestRandInt 2>&1").stdin("25", prompt = False, timeout = 20).stdin("30", prompt = False, timeout = 20).stdout(timeout = 60)
        try:
            out = int(out)
        except Exception as e:
            raise check50.Failure(f"Call to Custom.randInt(25, 30) returned {out}")
        if out < 24:
          checker["lower"] += 1
        elif out > 30:
          checker["higher"] += 1
        else:
          checker[out] += 1
    printer = "A call to randInt(25, 30) should produce numbers of 25, 26, 27, 28, or 29 only."
    if checker["lower"] > 0:
      raise check50.Failure(f"Out of 100 runs of your code, a number lower than 25 was generated {checker['lower']} times.", help=printer)
    if checker["higher"] > 0:
      raise check50.Failure(f"Out of 100 runs of your code, a number higher than 30 was generated {checker['lower']} times.", help=printer)  
    if checker[30] > 0:
      raise check50.Failure(f"The upper bound of 30 must be excluded from your range.", help=printer)  
    neednums = [num for num in checker if type(num) == int and checker[num] == 0]
    if len(neednums) > 0:
      raise check50.Failure(f"After running your randInt(start,upperBound) 100 times, we expected to get the numbers 25 - 29 at least once each. But we never got: {neednums}")
