# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c

classname = 'PrintOrder'

@check50.check()
def exists():
    """Program file exists"""
    check50.exists(f"{classname}.java")
    check50.exists(f"ClassCopies.java")
    check50.exists(f"Client.java")

@check50.check(exists)
def compiles():
    """Program compiles"""
    out = check50.run(f"javac -d ./ *.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """ClassCopies should run and have reasonable math"""
    check50.include("OrderClient.java")
    out = check50.run("javac -d ./ OrderClient.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to run due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to run", help=finderror)

    check50.run(f"java OrderClient").stdin("24", prompt = False).stdin("5", prompt = False).stdout("PrintOrder: 120 pages for 24 students", timeout = 60)


@check50.check(runs)
def runstatic():
    """PrintOrder should run and have reasonable static math"""
    check50.include("SuperClient.java")
    out = check50.run("javac -d ./ SuperClient.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to run due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to run", help=finderror)

    check50.run(f"java SuperClient").stdin("24", prompt = False).stdin("5", prompt = False).stdin("18", prompt = False).stdout("Total pages: 138", timeout = 60)