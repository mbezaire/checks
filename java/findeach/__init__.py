# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c


@check50.check()
def exists():
    """Find.java exists"""
    check50.exists("Find.java")

@check50.check(exists)
def compiles():
    """Find.java compiles"""
    check50.include("content.txt");
    out = check50.run("javac -d ./ Find.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

@check50.check(compiles)
def runs():
    """Find.java prints out content.txt as a String and as an array of Strings"""
    out = check50.run("java Find 1 > out.txt 2>&1").stdin("hello", prompt = False, timeout = 1).stdout(timeout = 5);
    with open("out.txt") as f:
        out = f.read() + "\n" + out
    check50.log(out)
    if "this hope is our door our portal" not in out:
        raise check50.Failure("Make sure to print out the String of the content from content.txt");
    elif "[this, hope, is, our, door, our, portal]" not in out:
        raise check50.Failure("Make sure to print out the String array of words from content.txt using Arrays.toString()");


@check50.check(compiles)
def runs60():
    """Find.java reports the correct number of words"""
    out = check50.run("java Find").stdin("our").stdout(timeout = 60)
    if 'The word our was found 2 times.' not in out:
        raise check50.Mismatch('The word our was found 2 times.',out)
    out = check50.run("java Find").stdin("portal").stdout(timeout = 60)
    if 'The word portal was found 1 times.' not in out:
        raise check50.Mismatch('The word portal was found 1 times.',out)
    out = check50.run("java Find").stdin("hello").stdout(timeout = 60)
    if 'The word hello was found 0 times.' not in out:
        raise check50.Mismatch('The word hello was found 0 times.',out)

@check50.check(compiles)
def runs40():
    """Find.java uses a for each loop"""
    with open("Find.java") as f:
        content = f.read()
        content = content.replace(" (","(")
    if "for(String" not in content:
        raise check50.Failure("Looks like you didn't use a for each loop")
    elif "for(i" in content:
        raise check50.Failure("Looks like you used a classic for loop (replace with for each loop)")
