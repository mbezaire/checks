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
    """Hello.java exists"""
    check50.exists("Hello.java")

@check50.check(exists)
def compiles():
    """Hello.java compiles"""
    out = check50.run("javac -d ./ Hello.java").stdout(timeout = 60)
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
    """Hello program greets the user"""
    check50.run("java Hello").stdin("Mrs. Taylor").stdout("[Hh]ello[,]{0,1} Mrs. Taylor", "Hello, Mrs. Taylor\n", timeout=30, regex=True).exit(0)


@check50.check(compiles)
def runs2():
    """Hello program greets another user"""
    check50.run("java Hello").stdin("Dr. Bezaire").stdout("[Hh]ello[,]{0,1} Dr. Bezaire", "Hello, Dr. Bezaire\n", timeout=30, regex=True).exit(0)
