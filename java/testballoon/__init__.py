# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""
# out = 'TestBalloon.java:7: error: incompatible types: String cannot be converted to Color\n        Balloon greenie = new Balloon(50, 100, 30, "green");\n                                                   ^\n\n1 error\n'

import re
import check50
import check50.c
import os


@check50.check()
def exists():
    """TestBalloon.java exists"""
    check50.exists("TestBalloon.java")

@check50.check(exists)
def compiles():
    """TestBalloon.java compiles"""
    check50.include("Color.java","Balloon.java")
    # out2 = check50.run("javac -d ./ *.java 2>&1").stdout(timeout = 60)
    out = check50.run("javac -d ./ TestBalloon.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        result = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output","")).groups()
        raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())

@check50.check(compiles)
def runs():
    """TestBalloon.java runs"""
    out2 = check50.run("java TestBalloon").stdout()
    if len(out2) < 60 or 'border' not in out2:
        raise check50.Failure("Your TestBalloon code seems to be missing some print statements.\nHere's what printed:\n", help=out2.strip())
    else:
        check50.log(out2)
        
        
# @check50.check(compiles)
# def getvalue():
#     """Fraction value can be computed"""
#     out = check50.run("javac -d ./ F0Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
#     check50.run("java F0Client").stdin("1", prompt=False).stdin("4", prompt=False).stdout("0.25\n").exit(0)
