# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re

helperfile = "FClient"
theirfile = "Repeat5"

### DON'T CHANGE THIS SECTION USUALLY #############
if len(helperfile) > 0:
    check50.include(f"{helperfile}.java")

def runcheck(helperfile=helperfile, theirfile=theirfile, input = "Hello", expected = "Hello"):
    if len(helperfile) > 0:
        check50.include(f"{helperfile}.java")
        out5 = check50.run(f"java {helperfile}").stdin(input, prompt = False).stdout()
    else:
        out5 = check50.run(f"java {theirfile}").stdin(input, prompt = False).stdout()
    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out5 = out5.strip()
    if out5 != expected:
        raise check50.Failure(f'Given "{input}", expected: {expected}, your program gave: ' + str(out5))

@check50.check()
def exists():
    """Your program exists """
    check50.exists(f"{theirfile}.java")

@check50.check(exists)
def compiles():
    """Your program compiles"""
    if len(helperfile) > 0:
        check50.include(f"{helperfile}.java")
    out = check50.run(f"javac -d ./ {theirfile}.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
    if len(helperfile) > 0:
        check50.run(f"javac -d ./ {helperfile}.java").stdout(timeout = 60)

################################################
# BELOW HERE IS FINE TO CHANGE

@check50.check(compiles)
def run0():
    """First 5 and last 5 should match"""
    input = "bonus points are bonus"
    expected = "true"
    runcheck(input = input, expected = expected)


@check50.check(compiles)
def run1():
    """First 5 and last 5 don't match"""
    input = "bonus points are extra credit"
    expected = "false"
    runcheck(input = input, expected = expected)
