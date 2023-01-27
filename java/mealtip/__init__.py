# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re

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
    """MealTip.java runs"""
    out = check50.run("java MealTip").stdin("25.50").stdin("20").stdout()
    if abs(float(out) - 25.50*1.2) > 0.0001:
        raise check50.Mismatch(25.50*1.2, out)


