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
    """Football.java exists"""
    check50.exists("Football.java")

@check50.check(exists)
def compiles():
    """Football.java compiles"""
    out = check50.run("javac -d ./ Football.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """Football.java should "Go for it" when down by 6 with 5 minutes left if the QB has a better completion rate"""
    check50.run("java Football").stdin("21").stdin("27").stdin("305").stdin("35").stdin("50").stdin("55").stdout("Go for it", timeout = 60)

def kicks():
    """Football.java should "Kick" when down by 6 with 5 minutes left if the kicker has a better success rate"""
    check50.run("java Football").stdin("21").stdin("27").stdin("305").stdin("35").stdin("60").stdin("45").stdout("Kick", timeout = 60)