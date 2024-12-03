# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re
import os
os.environ["CHECK50_WORKERS"] = "1"

theirfile = ["ReadAFile", "WriteAFile", "CountAndPrint", "LoopCount"]

## New plan:

# Check that files exist
# If they do, then run the autograder
# next, load in the json(s) that are produced
# And use the json scores to determine which checks are passed

# Must still hard code defs and docstrings here
# and then look for specific json checks to figure out if passing
# and print out the expected and actual

# printme goes to check50.log
# then expected and actual for mismatch
# then help if you want


### DON'T CHANGE THIS SECTION USUALLY #############
f_results = {'tests':[]}


def runcheck(theirfile=theirfile, actualin = "Hello", expected = "Hello"):
    out5 = check50.run(f"java {theirfile}").stdin(actualin, prompt = False).stdout()
    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out5 = out5.strip()
    if out5 != expected:
        raise check50.Failure(f'Given "{input}", expected: {expected}, your program gave: ' + str(out5))

@check50.check()
def exists():
    """Your programs exist"""
    for file in theirfile:
        check50.exists(f"{file}.java")

@check50.check(exists)
def compiles():
    """Your programs compile"""
    global f_results

    out = check50.run(f"javac -d ./ {'.java '.join(theirfile)}.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

def findCheck(f_results, id = "constructors"):
    for i, test in enumerate(f_results['tests']):
        if test['checkId'] == id:
            return i
    raise check50.Failure("Something went wrong with the autograder for this check")

def processCheck(f_results, id = "constructors"):
    checkId = findCheck(f_results, id)
    if 'printme' in f_results['tests'][checkId] and len(f_results['tests'][checkId]['printme']) > 0:
        prme = f_results['tests'][checkId]['printme'].replace("\\\\","\\")
        for line in prme.split("\n"):
            check50.log(line)
    if not f_results['tests'][checkId]['pass']:
        if f_results['tests'][checkId]['failStatus'] == 1:
            raise check50.Failure(f_results['tests'][checkId]['rationale'].replace("\\\\","\\"), help=f_results['tests'][checkId]['help'].replace("\\\\","\\"))
        else: # if failStatus is 0, choose mismatch
            raise check50.Mismatch(f_results['tests'][checkId]['expected'].replace("\\\\","\\"), f_results['tests'][checkId]['actual'].replace("\\\\","\\"), f_results['tests'][checkId]['help'].replace("\\\\","\\"))

################################################
# BELOW HERE IS FINE TO CHANGE
import random

@check50.check(compiles)
def reads():
    """Checking that ReadAFile works"""
    funname = random.choice(["Henrietta","Fiona","Arnold","Reginald","Alvin"])
    funyear = random.randint(9,12)
    fungpa = 3 + random.randint(1,100)/100
    with open("info.txt","w") as f:
        f.write(f"{funname}\n{funyear}\n{fungpa}")

    check50.run('java ReadAFile').stdout(f"{funname}\n{funyear}\n{fungpa}").exit(0)

@check50.check(compiles)
def writes():
    """Checking that WriteAFile works"""
    funname = random.choice(["Henrietta","Fiona","Arnold","Reginald","Alvin"])
    funyear = random.randint(9,12)
    fungpa = 3 + random.randint(1,100)/100
    check50.run('java WriteAFile').stdin(funname, timeout=60).stdin(str(funyear) + " ", timeout=60).stdin(str(fungpa) + " ", timeout=60).exit(0)
    with open("info.txt","r") as f:
        content = f.read()
    
    if content.strip() != f"{funname}\n{funyear}\n{fungpa}":
        raise check50.Mismatch(content.strip(), f"{funname}\n{funyear}\n{fungpa}")

@check50.check(compiles)
def counts():
    """Check that CountAndPrint works"""
    x = 6
    y = random.randint(5,9)
    check50.include("count.txt")

    for z in range(y):
        check50.run('java CountAndPrint').exit(0)

    with open("count.txt","r") as f:
        num = f.read()
    num = num.strip()
    num = int(num)

    if num != x + y:
        raise check50.Mismatch(str(x + y), str(num), help=f"The number in the count.txt file was different than expected, starting from count.txt contains {x} and running CountAndPrint {y} more times")
    
@check50.check(compiles)
def loops():
    """Check that LoopCount works"""
    x = random.randint(1,3)
    with open("countloop.txt","w") as f:
        f.write(str(x))

    check50.run('java LoopCount').stdin('5', timeout=60)
    check50.run('java LoopCount').stdin('6', timeout=60)

    with open("countloop.txt","r") as f:
        num = f.read()

    num = int(num.strip())
    
    if num != x + 11:
        raise check50.Mismatch(str(x + 11), str(num), help=f"The number in the countloop.txt file was different than expected, starting from count.txt contains {x} and running CountAndPrint 2 more times with 5 and 6 loop iterations")

    return f_results
