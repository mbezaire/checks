# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re
import random

@check50.check()
def exists():
    """RandomWord.java exists"""
    check50.exists("RandomWord.java")

@check50.check(exists)
def compiles():
    """RandomWord.java compiles"""
    out = check50.run("javac -d ./ RandomWord.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

@check50.check(compiles)
def runs():
    """RandomWord.java has a getOneRandomWord method that takes a String as an argument and returns a String of one word from its input"""
    check50.include("TestRandomWords.java")
    out = check50.run("javac -d ./ TestRandomWords.java").stdout(timeout = 60)
    wordstr = "HOUSE,TALLY,BUNCH,"
    out = check50.run("java TestRandomWords 2>&1").stdin(wordstr, prompt = False).stdout(timeout = 30)
    if ',' in out:
        raise check50.Failure(f"Your getOneRandomWord returned {out} but should not include a comma")
    elif out.strip() not in wordstr:
        raise check50.Failure(f"Your getOneRandomWord returned {out} but should have returned a word from {wordstr}")

@check50.check(runs)
def varwords():
    """RandomWord.java returns words randomly"""
    out = check50.run("javac -d ./ TestRandomWords.java").stdout(timeout = 60)
    check50.log(out)
    wordstr = "HAPPY,ETHER,BREAK,GOALS,AZURE,PILOT,RAINY,"
    allkeys = wordstr[:-1].split(",")
    wordct = {}
    for key in allkeys:
        wordct[key] = 0
    numtimes = 200
    outer = ""
    for x in range(numtimes):
        out = check50.run("java TestRandomWords 2>&1").stdin(wordstr, prompt = False).stdout(timeout = 30)
        if x < 20:
            outer += out + " "
        if ',' in out:
            raise check50.Failure(f"Your getOneRandomWord returned {out} but should not include a comma")
        elif out.strip() not in wordct:
            raise check50.Failure(f"Your getOneRandomWord returned {out} but should have returned a word from {wordstr}")
        else:
            wordct[out.strip()] += 1
    for key in allkeys:
        if key not in wordct or wordct[key] == 0:
            raise check50.Failure(f"We ran your getOneRandomWord {numtimes} times using {wordstr} and never once got {key}, this seems sus")
    check50.log(outer)
    mystr = ""
    for key in wordct:
        mystr += key + ": " + str(wordct[key]) + ", "
    check50.log(mystr)


@check50.check(varwords)
def noIfs():
    """RandomWord.java contains no if or boolean logic"""
    with open("RandomWord.java") as f:
        filestr = f.read()
    if "if" in filestr or "switch" in filestr or "?" in filestr or "for" in filestr or "while" in filestrt:
        raise check50.Failure(f"Try to rewrite your logic so that you don't need any loops, if statements, or conditionals")

