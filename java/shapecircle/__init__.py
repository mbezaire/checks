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
    """Circle.java, Shape.java, Rectangle.java, and ShapeClient.java exist"""
    check50.exists("Shape.java")
    check50.exists("Rectangle.java")
    check50.exists("ShapeClient.java")
    check50.exists("Circle.java")

@check50.check(exists)
def compiles():
    """All files compile"""
    out = check50.run("javac -d ./ Shape.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

    out = check50.run("javac -d ./ Rectangle.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

    out = check50.run("javac -d ./ ShapeClient.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

    out = check50.run("javac -d ./ Circle.java").stdout(timeout = 60)
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
    """ShapeClient.java creates a Shape, a Rectangle, and a Circle and prints out their toStrings"""
    out = check50.run("java ShapeClient 2>&1").stdout(timeout = 30)
    if len(out) == 0:
        raise check50.Failure("There was an issue with your code.", help="Check that you are printing your shapes")
    if "@" in out or "ect" not in out or len(out) < 15:
        raise check50.Mismatch("Nicely worded toString output", out.strip())
    if "irc" not in out or len(out) < 20:
        raise check50.Mismatch("Not enough stuff printed...", out.strip(), help="Make sure you print out your Circle and perhaps also some other methods. Show off your code!")


@check50.check(runs)
def readme():
    """README.md for code"""
    check50.exists("README.md")
    with open("README.md") as f:
        text = f.read()

    if len(text) < 100:
        raise check50.Failure("Add more content to your README.", help="Include notes about class content and inheritance syntax")
    elif '#' not in text:
        raise check50.Failure("Include a header in your README.", help="Use a # symbol, then a space, then your heading")
    elif text.count('```') < 2:
        raise check50.Failure("Include a code snippet in your README.", help="Use ``` (3 backtick symbols) in a line above and a line below your code snippet")
    elif text.count('`') < 8:
        raise check50.Failure("Include in-line code in your README.", help="Use ` (the backtick symbol) before and after your in-line code.")
    elif text.lower().count('circle') < 1:
        raise check50.Failure("Include information about your Circle code in your README.", help="Describe something, anything about your Circle code.")