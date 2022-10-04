# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """TestBalloon.java exists"""
    check50.exists("TestBalloon.java")

@check50.check(exists)
def compiles():
    """TestBalloon.java compiles"""
    out = check50.run("javac -d ./ TestBalloon.java 2>&1").stdout(timeout = 60).replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output","")
    if "error" in out:
        
        raise check50.Failure("Failed to compile", help="|"+out+"|")

@check50.check(compiles)
def runs():
    """TestBalloon.java runs"""
    out = check50.run("javac -d ./ TestBalloon.java").stdout(timeout = 60)
    check50.log(out)
    out2 = check50.run("java TestBalloon").stdout()
    check50.log(out2)

# @check50.check(compiles)
# def getvalue():
#     """Fraction value can be computed"""
#     out = check50.run("javac -d ./ F0Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
#     check50.run("java F0Client").stdin("1", prompt=False).stdin("4", prompt=False).stdout("0.25\n").exit(0)
