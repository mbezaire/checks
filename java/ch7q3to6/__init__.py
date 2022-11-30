# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c
import re

check50.include("FClient.java", "F0Client.java", "F1Client.java", "F2Client.java", "F3Client.java")

@check50.check()
def exists():
    """Chapter7part1.java exists"""
    check50.exists("Chapter7part1.java")

@check50.check(exists)
def compiles():
    """Chapter7part1.java compiles"""
    out = check50.run("javac -d ./ Chapter7part1.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
    check50.run("javac -d ./ FClient.java").stdout(timeout = 60)
    check50.run("javac -d ./ F0Client.java").stdout(timeout = 60)
    check50.run("javac -d ./ F1Client.java").stdout(timeout = 60)
    check50.run("javac -d ./ F2Client.java").stdout(timeout = 60)
    check50.run("javac -d ./ F3Client.java").stdout(timeout = 60)


@check50.check()
def dexists():
    """HelloNTimes.java exists"""
    check50.exists("HelloNTimes.java")

@check50.check(dexists)
def dcompiles():
    """HelloNTimes.java compiles"""
    out = check50.run("javac -d ./ HelloNTimes.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

@check50.check(compiles)
def run1():
    """calcSum works correctly"""
    out = check50.run("java FClient").stdout()
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if "true" not in out:
        raise check50.Failure("calcSum doesn't give the right answer")


@check50.check(compiles)
def run3():
    """product calculates 6 and 0 as 0"""
    out = check50.run("java F0Client").stdin("6", prompt = False).stdin("0", prompt = False).stdout() #"0").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "0":
        raise check50.Failure("expected 0, actual " + str(out))

@check50.check(compiles)
def run2():
    """product calculates 5 and 9 as 45"""
    out = check50.run("java F0Client").stdin("5", prompt = False).stdin("9", prompt = False).stdout() #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "45":
        raise check50.Failure("expected 45, actual " + str(out))

@check50.check(compiles)
def run4():
    """product calculates 1 and 5 as 5"""
    out = check50.run("java F0Client").stdin("1", prompt = False).stdin("5", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "5":
        raise check50.Failure("expected 5, actual " + str(out))

@check50.check(compiles)
def run5():
    """nextAlgorithm works correctly"""
    out = check50.run("java F1Client").stdout()
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if "true" not in out:
        raise check50.Failure("nextAlgorithm doesn't give the right answer")


@check50.check(compiles)
def run6():
    """division calculates 45/6 correctly"""
    out = check50.run("java F2Client").stdin("45", prompt = False).stdin("6", prompt = False).stdout() #"45/6 gives\nquotient: 7, remainder: 3").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "45/6 gives\nquotient: 7, remainder: 3":
        raise check50.Failure("expected 45/6 gives\nquotient: 7, remainder: 3\nactual " + str(out))

@check50.check(compiles)
def run7():
    """division calculates 13/30 correctly"""
    out = check50.run("java F2Client").stdin("13", prompt = False).stdin("30", prompt = False).stdout() #"13/30 gives\nquotient: 0, remainder: 13").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "13/30 gives\nquotient: 0, remainder: 13":
        raise check50.Failure("expected 13/30 gives\nquotient: 0, remainder: 13\nactual " + str(out))


@check50.check(compiles)
def run8():
    """division calculates 14/7 correctly"""
    out = check50.run("java F2Client").stdin("14", prompt = False).stdin("7", prompt = False).stdout() # "14/7 gives\nquotient: 2, remainder: 0").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "14/7 gives\nquotient: 2, remainder: 0":
        raise check50.Failure("expected 14/7 gives\nquotient: 2, remainder: 0\nactual " + str(out))

@check50.check(compiles)
def run9():
    """populationMexico forecasts 150 correctly"""
    out = check50.run("java F3Client").stdin("150").stdout() #"2053").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if  "2053" not in out:
        raise check50.Failure("expected 2053\nactual " + str(out.replace("Enter a target population:","").strip()))

@check50.check(compiles)
def run10():
    """populationMexico goes back in time"""
    out = check50.run("java F3Client").stdin("120").stdout() #"2014").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if "2014" not in out:
        raise check50.Failure("expected 2014\nactual " + str(out.replace("Enter a target population:","").strip()))

@check50.check(compiles)
def run11():
    """populationMexico forecasts 130 alright"""
    out = check50.run("java F3Client ").stdin("130").stdout() #"2024").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if "2024" not in out:
        raise check50.Failure("expected 2024\nactual " + str(out.replace("Enter a target population:","").strip()))

@check50.check(dcompiles)
def druns1():
    """HelloNTimes.java prints correctly"""
    check50.run("java HelloNTimes.java").stdin("2").stdin("Hello").stdout("Hello\nHello\n").exit(0)

@check50.check(dcompiles)
def druns2():
    """HelloNTimes.java prints Santa's message correctly"""
    check50.run("java HelloNTimes.java").stdin("3").stdin("Ho").stdout("Ho\nHo\nHo\n").exit(0)