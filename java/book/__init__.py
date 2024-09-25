# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c
import re

@check50.check()
def exists():
    """Book.java, Author.java, and Client.java exist"""
    check50.exists("Book.java")
    check50.exists("Author.java")
    check50.exists("Client.java")

    
@check50.check(exists)
def compiles():
    """Files compile"""
    out = check50.run("javac -d ./ Book.java Author.java Client.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to run due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to run", help=finderror)


@check50.check(compiles)
def runs():
    """Book.java runs"""
    check50.include("BClient.java")
    out = check50.run("javac -d ./ BClient.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to run due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to run", help=finderror)
    check50.log(out)
    out2 = check50.run("java BClient").stdout()
    check50.log(out2)

@check50.check(runs)
def book1():
    """A book has a price and a toString"""
    check50.include("B1Client.java")
    out = check50.run("javac -d ./ B1Client.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to run due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to run", help=finderror)
    check50.log(out)
    expected = r"[Aa]n [Ii]mmense [Ww]orld[\n\t\s]*[bByY :]+Ed Yong[\n\t\s]*[$0-9\.]+"
    check50.run("java B1Client").stdout(expected, "An Immense World\nby Ed Yong\n$85.43", regex=True)

@check50.check(runs)
def book2():
    """Another book has a price and a toString"""
    check50.include("B2Client.java")
    out = check50.run("javac -d ./ B2Client.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to run due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to run", help=finderror)
    check50.log(out)
    expected = r"[Aa]n [Ii]mmense [Ww]orld[\n\t\s]*[bByY :]+Ed Yong[\n\t\s]*[$0-9\.]+"
    check50.run("java B2Client").stdout(expected, "An Immense World\nby Ed Yong\n$85.43", regex=True)


