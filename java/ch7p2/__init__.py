# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re

check50.include("FClient.java", "F0Client.java", "F1Client.java", "F2Client.java", "F3Client.java", "F4Client.java", "F5Client.java", "scores.dat", "scores2.dat")

@check50.check()
def exists():
    """Chapter7Part2.java exists"""
    check50.exists("Chapter7Part2.java")

@check50.check(exists)
def compiles():
    """Chapter7Part2.java compiles"""
    out = check50.run("javac -d ./ Chapter7Part2.java").stdout(timeout = 60)
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
    check50.run("javac -d ./ F4Client.java").stdout(timeout = 60)
    check50.run("javac -d ./ F5Client.java").stdout(timeout = 60)


@check50.check()
def dexists():
    """AverageScore.java exists"""
    check50.exists("AverageScore.java")

@check50.check(dexists)
def dcompiles():
    """AverageScore.java compiles"""
    out = check50.run("javac -d ./ AverageScore.java").stdout(timeout = 60)
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
    """addOdds works correctly"""
    out5 = check50.run("java F0Client").stdin("5", prompt = False).stdout()
    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out5 = out5.strip()
    if out5 != "9":
        raise check50.Failure("Given addOdds(5), expected 9, actual " + str(out5))
    out5 = check50.run("java F0Client").stdin("8", prompt = False).stdout()
    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out5 = out5.strip()
    if out5 != "16":
        raise check50.Failure("Given addOdds(8), expected 16, actual " + str(out5))

@check50.check(compiles)
def run3():
    """addUpTo() sums and prints correctly"""
    out = check50.run("java F1Client").stdin("6", prompt = True, timeout = 60).stdout() #"0").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if "1 + 2 + 3 + 4 + 5 + 6 = 21" not in out:
        raise check50.Failure("expected 1 + 2 + 3 + 4 + 5 + 6 = 21, actual " + str(out))
    out = check50.run("java F1Client").stdin("1", prompt = True).stdout() #"0").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "1 = 1":
        raise check50.Failure("expected 1 = 1, actual " + str(out))

@check50.check(compiles)
def run2():
    """isPerfectSquare evaluates correctly"""
    out = check50.run("java F2Client").stdin("1", prompt = False).stdout() #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))

    out = check50.run("java F2Client").stdin("3", prompt = False).stdout() #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "false":
        raise check50.Failure("expected false, actual " + str(out))

    out = check50.run("java F2Client").stdin("81", prompt = False).stdout() #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))

    out = check50.run("java F2Client").stdin("36", prompt = False).stdout() #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))

@check50.check(compiles)
def run4():
    """isPrime correctly reports prime numbers"""
    out = check50.run("java F3Client").stdin("2", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))
    out = check50.run("java F3Client").stdin("3", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))
    out = check50.run("java F3Client").stdin("4", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "false":
        raise check50.Failure("expected false, actual " + str(out))
    out = check50.run("java F3Client").stdin("11", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))
    out = check50.run("java F3Client").stdin("22", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "false":
        raise check50.Failure("expected true, false " + str(out))
    out = check50.run("java F3Client").stdin("81", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "false":
        raise check50.Failure("expected false, actual " + str(out))


@check50.check(compiles)
def run4():
    """isRelPrime correctly reports prime numbers"""
    out = check50.run("java F3Client").stdin("2", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))
    out = check50.run("java F3Client").stdin("3", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))
    out = check50.run("java F3Client").stdin("4", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "false":
        raise check50.Failure("expected false, actual " + str(out))
    out = check50.run("java F3Client").stdin("11", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))
    out = check50.run("java F3Client").stdin("5", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "true":
        raise check50.Failure("expected true, actual " + str(out))

    out = check50.run("java F3Client").stdin("6", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "false":
        raise check50.Failure("expected true, false " + str(out))
    out = check50.run("java F3Client").stdin("25", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "false":
        raise check50.Failure("expected false, actual " + str(out))
    out = check50.run("java F3Client").stdin("65", prompt = False).stdout() #"5").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "false":
        raise check50.Failure("expected false, actual " + str(out))


@check50.check(compiles)
def run5():
    """sumDigits evaluates correctly"""
    out = check50.run("java F4Client").stdin("123", prompt = False).stdout() #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "6":
        raise check50.Failure("expected 6, actual " + str(out))
    out = check50.run("java F4Client").stdin("304", prompt = False).stdout() #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "7":
        raise check50.Failure("expected 7, actual " + str(out))

    out = check50.run("java F4Client").stdin("590", prompt = False).stdout() #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "14":
        raise check50.Failure("expected 14, actual " + str(out))

    out = check50.run("java F4Client").stdin("1062938", prompt = False).stdout() #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if out != "29":
        raise check50.Failure("expected 29, actual " + str(out))


@check50.check(compiles)
def run5():
    """printPairs prints correct pairs"""
    out = check50.run("java F5Client").stdout(timeout = 60) #"45").exit(0)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    pairs = [(5, 3),\
(7, 5),\
(13, 11),\
(19, 17),\
(31, 29),\
(43, 41),\
(61, 59),\
(73, 71),\
(103, 101),\
(109, 107),\
(139, 137),\
(151, 149),\
(181, 179),\
(193, 191),\
(199, 197),\
(229, 227),\
(241, 239),\
(271, 269),\
(283, 281),\
(313, 311)]
    for pair in pairs:
        if f"{pair[0]} and {pair[1]}" not in out and f"{pair[1]} and {pair[0]}" not in out:
            raise check50.Failure(f"expected {pair[1]} and {pair[0]} but not found in:\n{out}")



@check50.check(dcompiles)
def druns1():
    """AverageScore.java calculates correctly"""
    out = check50.run("java AverageScore.java").stdin("scores.dat", prompt = True, timeout = 60).stdout()
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if abs(float(out) - 92.42857143) > 0.0001:
        raise check50.Failure("expected 92.42857143, actual " + str(out))
    out = check50.run("java AverageScore.java").stdin("scores2.dat", prompt = True, timeout = 60).stdout()
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    out = out.strip()
    if abs(float(out) - 68) > 0.0001:
        raise check50.Failure("expected 68, actual " + str(out))
