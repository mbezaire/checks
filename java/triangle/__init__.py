# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50


@check50.check()
def exists():
    """Triangle.java exists"""
    check50.exists("Triangle.java")

@check50.check(exists)
def compiles():
    """Triangle.java compiles"""
    out = check50.run("javac -d ./ Custom.java 2>&1").stdout(timeout = 60)
    out = check50.run("javac -d ./ Triangle.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """Triangle.java finds a shape is not a triangle"""
    check50.run("java Triangle").stdin("8").stdin("2").stdin("1").stdout("[nN]ot [aA] [tT]riangle[\.]*", "not a triangle", timeout = 60, regex = True)

@check50.check(compiles)
def runs60():
    """Triangle.java finds a shape is a triangle"""
    check50.run("java Triangle").stdin("8").stdin("9").stdin("2").stdout("[tT]riangle[\.]*", "triangle", timeout = 60, regex = True)

@check50.check(compiles)
def runs59():
    """Triangle.java finds a shape is a right triangle"""
    check50.run("java Triangle").stdin("6").stdin("8").stdin("10").stdout("[rR]ight [tT]riangle[\.]*", "triangle", timeout = 60, regex = True)