# -*- coding: utf-8 -*-
"""
Created on Apr 8 2024

@author: marianne.bezaire
"""

import re
import check50
import check50.c
import os
os.environ["CHECK50_WORKERS"] = "1"


@check50.check()
def exists():
    """Warmup.java must exist"""
    check50.exists("Warmup.java")

@check50.check(exists)
def compiles():
    """Warmup.java must compile"""
    check50.include("CheckIt.java")
    out = check50.run("javac -d ./ Warmup.java CheckIt.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)


@check50.check(compiles)
def runs():
    """Warmup.java runs alright"""
    check50.run("java Warmup 2>&1").exit(0)
    out = check50.run("java CheckIt 2>&1").stdout(timeout=60)
    return out

@check50.check(runs)
def asciit(out):
    """The ascii() method returns the right value"""

    #with open("output.txt") as f:
    content = out.split("\n")

    expected = ""
    actual = ""
    for line in content[:3]:
        data = line.split("\t")
        expected += data[0] + "\n"
        actual += data[1] + "\n"

    if expected != actual:
        raise check50.Mismatch(expected, actual, help = "Not sure what went wrong, this was a gimme")

    return content[3:]

@check50.check(asciit)
def uppercheck(content):
    """ The upper() method returns an uppercase char """
    expected = ""
    actual = ""
    for line in content[:3]:
        data = line.split("\t")
        charstr = data[0]
        lowerchar = data[1]
        upperchar = data[2]
        expected += charstr.lower() + " returns: " + charstr.upper() + "\n" + charstr.upper() + " returns: " + charstr.upper() + "\n"
        actual += charstr.lower() + " returns: " + lowerchar + "\n" + charstr.upper() + " returns: " + upperchar + "\n"

    if expected != actual:
        raise check50.Mismatch(expected, actual, help = "Make sure that your program returns the uppercase char whether you pass in the lower or upper case one.")

    return content[3:]


@check50.check(uppercheck)
def lowercheck(content):
    """ The lower() method returns a lowercase char """
    expected = ""
    actual = ""
    for line in content[:3]:
        data = line.split("\t")
        charstr = data[0]
        lowerchar = data[1]
        upperchar = data[2]
        expected += charstr.lower() + " returns: " + charstr.lower() + "\n" + charstr.upper() + " returns: " + charstr.lower() + "\n"
        actual += charstr.lower() + " returns: " + lowerchar + "\n" + charstr.upper() + " returns: " + upperchar + "\n"


    if expected != actual:
        raise check50.Mismatch(expected, actual, help = "Make sure that your program returns the lowercase char whether you pass in the lower or upper case one.")

    return content[3:]


@check50.check(lowercheck)
def explain(content):
    """ This check will be manually graded if you pass """
    if len(content[0]) < 10:
        raise check50.Failure("Your explanation is too short. Fill out your explain() method with a String of what your ascii() method does and why it doesn't error")
    check50.log("This check will be manually graded if you pass")
