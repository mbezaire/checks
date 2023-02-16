# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re

check50.include("FClient.java")

@check50.check()
def exists():
    """Repeat.java exists"""
    check50.exists("Repeat.java")

@check50.check(exists)
def compiles():
    """Repeat.java compiles"""
    check50.include("FClient.java")
    out = check50.run("javac -d ./ Repeat.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
    check50.run("javac -d ./ FClient.java").stdout(timeout = 60)


@check50.check(compiles)
def run0():
    """Repeat with no space in middle should be true"""
    check50.include("FClient.java")
    out5 = check50.run("java FClient").stdin("HAHA", prompt = False).stdout()
    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out5 = out5.strip()
    if out5 != "true":
        raise check50.Failure('Given "HAHA", expected true, actual ' + str(out5))

@check50.check(compiles)
def run1():
    """Repeat with space in middle should be true"""
    check50.include("FClient.java")
    out5 = check50.run("java FClient").stdin("orange orange", prompt = False).stdout()
    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out5 = out5.strip()
    if out5 != "true":
        raise check50.Failure('Given "orange orange", expected true, actual ' + str(out5))


@check50.check(compiles)
def run3():
    """Non-repeating should be false"""
    check50.include("FClient.java")
    out5 = check50.run("java FClient").stdin("orange range", prompt = False).stdout()
    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out5 = out5.strip()
    if out5 != "false":
        raise check50.Failure('Given "orange range", expected false, actual ' + str(out5))
