# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c
import random


@check50.check()
def exists():
    """Split.java exists"""
    check50.exists("Split.java")

@check50.check(exists)
def compiles():
    """Split.java compiles"""
    out = check50.run("javac -d ./ Split.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
    check50.include("TestSplit.java")
    out = check50.run("javac -d ./ TestSplit.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        raise check50.Failure("Make sure your Split.java has a split method with this header: public static String[] split(String, char)")


@check50.check(compiles)
def runs40():
    """Find.java uses a your custom split method"""
    with open("Split.java") as f:
        content = f.read()
    content = content.replace(" ","").replace("\n","").replace("\t","")
    if "publicstaticString[]split(String" not in content:
        raise check50.Failure("Looks like you forgot to write your own split method")
    if "publicstaticvoidmain(String" not in content:
        raise check50.Failure("That's bold - no main method to test your code?")
    if "=split(" not in content and "Arrays.toString(split(" not in content:
        raise check50.Failure("Make sure to actually test your split method, print out its results")
    if ".split(" in content:
        raise check50.Failure("Looks like you used the regular String split method - write your own logic")
    
@check50.check(runs40)
def runs():
    """Split.java prints out an array of Strings"""
    phrases = ["Once upon a magical line of code","It was a dark and buggy compilation of code","Who is your favorite fearless coder"]
    delims = [' ',':',',','-']
    phrase = random.choice(phrases)
    delim = random.choice(delims)
    phrases.remove(phrase)
    delims.remove(delim)
    phrase = phrase.replace(" ",delim)
    arr = phrase.split(delim)
    output = '[' + ', '.join(arr) + ']\nLength: ' + str(len(arr))
    out = check50.run("java TestSplit").stdin(phrase,prompt = False).stdin(delim,prompt = False).stdout(timeout = 5)
    if out != output:
        for i in range(min(len(out),len(output))):
            if out[i] != output[i]:
                check50.log(f'difference at character {i} which is {out[i]} or {output[i]}')
        print(f'lengths are: {len(out)}, {len(output)}')

    check50.run("java TestSplit").stdin(phrase,prompt = False).stdin(delim,prompt = False).stdout(output,timeout = 5)



