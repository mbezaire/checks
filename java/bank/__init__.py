# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re

helperfile = "CheckBank"
theirfile = ["BankAccount", "Bank", "BankClient"]

## New plan:
    
# Check that files exist
# If they do, then run the gradescope autograder
# next, load in the json(s) that are produced
# And use the json scores to determine which checks are passed

# Must still hard code defs and docstrings here
# and then look for specific json checks to figure out if passing
# and print out the expected and actual

# printme goes to check50.log
# then expected and actual for mismatch
# then help if you want


### DON'T CHANGE THIS SECTION USUALLY #############
if len(helperfile) > 0:
    check50.include(f"{helperfile}.java")

def runcheck(helperfile=helperfile, theirfile=theirfile, actualin = "Hello", expected = "Hello"):
    if len(helperfile) > 0:
        check50.include(f"{helperfile}.java")
        out5 = check50.run(f"java {helperfile}").stdin(actualin, prompt = False).stdout()
    else:
        out5 = check50.run(f"java {theirfile}").stdin(actualin, prompt = False).stdout()
    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out5 = out5.strip()
    if out5 != expected:
        raise check50.Failure(f'Given "{input}", expected: {expected}, your program gave: ' + str(out5))

@check50.check()
def exists():
    """Your program exists"""
    for file in theirfile:
        check50.exists(f"{file}.java")

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
    """Repeat with no space in middle should be true"""
    input = "HAHA"
    expected = "true"
    runcheck(input = input, expected = expected)


@check50.check(compiles)
def run1():
    """Repeat with space in middle should be true"""
    input = "orange orange"
    expected = "true"
    runcheck(input = input, expected = expected)



@check50.check(compiles)
def run3():
    """Non-repeating should be false"""
    input = "orange range"
    expected = "false"
    runcheck(input = input, expected = expected)

