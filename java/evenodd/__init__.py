# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c

classname = 'EvenOdd'

@check50.check()
def exists():
    """Program file exists"""
    check50.exists(f"{classname}.java")

@check50.check(exists)
def compiles():
    """Program compiles"""
    out = check50.run(f"javac -d ./ {classname}.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """Program should say more evens"""
    output = check50.run(f"java {classname}").stdin("8").stdin("6", prompt = False).stdin("4", prompt = False).stdin("5", prompt = False).stdout()
    if "ven" not in output:
        raise check50.Mismatch("More evens", output)
    
@check50.check(compiles)
def runs60():
    """Program should say same number"""
    output = check50.run(f"java {classname}").stdin("0").stdin("2", prompt = False).stdin("1", prompt = False).stdin("3", prompt = False).stdout()
    if "ame" not in output:
        raise check50.Mismatch("Same number of evens and odds", output)

@check50.check(compiles)
def runs59():
    """Program should say more odds"""
    output = check50.run(f"java {classname}").stdin("1").stdin("3", prompt = False).stdin("1", prompt = False).stdin("3", prompt = False).stdout()
    if "dd" not in output:
        raise check50.Mismatch("More odds", output)
