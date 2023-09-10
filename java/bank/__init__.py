# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re
import os
os.environ["CHECK50_WORKERS"] = "1"
import json

helperfile = "Tester"
theirfile = ["BankAccount", "Bank", "BankClient"]

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
    """Your program compiles and the tester files compile with it"""
    global f_results
    if len(helperfile) > 0:
        check50.include(f"{helperfile}.java")
    out = check50.run(f"javac -d ./ {'.java '.join(theirfile)}.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
    if len(helperfile) > 0:
        out = check50.run(f"javac -d ./ {helperfile}.java").stdout(timeout = 60)
        if "error" in out:
            finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
            if finderror != None:
                result = finderror.groups()
                raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
            else:
                raise check50.Failure("Failed to compile", help=finderror)
        for line in out.split("\n"):
            check50.log(line)
        out = check50.run(f"java {helperfile}").stdout(timeout = 360)

        if "{" in out:
            f_results = json.loads(out[out.index("{"):])
        return f_results

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

@check50.check(compiles)
def construct(f_results):
    """Checking that constructor(s) work"""
    processCheck(f_results, "constructors")
    return f_results

@check50.check(construct)
def run0(f_results):
    """Checking that appropriate getters exist"""
    processCheck(f_results, "getters")
    return f_results

@check50.check(run0)
def run1(f_results):
    """Constructors and getters manage field values correctly"""
    processCheck(f_results, "correctval")
    return f_results

@check50.check(run1)
def run2(f_results):
    """The deposit method works correctly"""
    processCheck(f_results, "deposit")
    return f_results


@check50.check(run2)
def run3(f_results):
    """The withdraw method works correctly"""
    processCheck(f_results, "withdraw")
    return f_results

@check50.check(run3)
def run4(f_results):
    """The toString method returns a String with all field data"""
    processCheck(f_results, "tostring")
    return f_results

@check50.check(run4)
def run5(f_results):
    """The pin number is 4 digits and randomly assigned"""
    processCheck(f_results, "pinnumber")
    check50.log("You are ready to develop Bank now!")
    return f_results


@check50.check(run5)
def run6(f_results):
    """Checks whether Bank is ready to test"""
    with open("Bank.java") as f:
        lines = f.readlines()
    if len(lines) < 18:
        raise check50.Failure("Add more code to Bank.java to run additional tests on Bank")
    return f_results

@check50.check(run6)
def run7(f_results):
    """Checks constructor of Bank"""
    check50.include("Tester2.java")
    out = check50.run(f"javac -d ./ Tester2.java").stdout(timeout = 60)
    check50.log(out)
    out = check50.run(f"java Tester2").stdout(timeout = 360)

    if "{" in out:
        f_results = json.loads(out[out.index("{"):])
    processCheck(f_results, "bankstruct")
    return f_results

@check50.check(run7)
def run8(f_results):
    """Bank contains separate BankAccount fields"""

    with open("Bank.java", "r") as f:
        textlines = f.read()

    if "Array" in textlines or (textlines.count("[") > textlines.count("main(String[")) or "List" in textlines:
        raise check50.Failure("Looks like your Bank code may be using Arrays or other List-type structures")

    processCheck(f_results, "account3")
    return f_results


@check50.check(run8)
def run9(f_results):
    """ Accounts can be viewed when the correct information is provided and not otherwise """
    processCheck(f_results, "accountview")
    return f_results


@check50.check(run9)
def run10(f_results):
    """ Withdraw and deposit logic works alright at the Bank level """
    processCheck(f_results, "depdraw")
    return f_results

@check50.check(run10)
def run11(f_results):
    """ Bank has a descriptive toString """
    processCheck(f_results, "bankstring")
    check50.log("You are ready to develop BankClient now!")
    return f_results


@check50.check(run11)
def run12(f_results):
    """ Checks whether BankClient is ready to test"""
    with open("BankClient.java") as f:
        lines = f.readlines()
    if len(lines) < 14:
        raise check50.Failure("Add more code to BankClient.java to run additional tests on BankClient")
    return f_results


@check50.check(run12)
def run13(f_results):
    """ Checks whether BankClient runs without errors """
    out = check50.run(f"javac -d ./ BankClient.java").stdout(timeout = 60)
    check50.log(out)
    out = check50.run(f"java BankClient").stdin("4", timeout = 60).stdin("Missy", timeout = 60).stdin("1245", timeout = 60).stdin("5", timeout = 60).stdout(timeout = 360)
    check50.log(out)

    # if len(lines) < 13:
    #    raise check50.Failure("Add more code to BankClient.java to run additional tests on BankClient")
    # return f_results
