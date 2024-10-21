# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50


@check50.check()
def exists():
    """UPC.java exists"""
    check50.exists("UPC.java")

@check50.check(exists)
def compiles():
    """UPC.java compiles"""
    out = check50.run("javac -d ./ Custom.java 2>&1").stdout(timeout = 60)
    out = check50.run("javac -d ./ UPC.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """UPC.java finds a valid UPC"""
    check50.run("java UPC").stdin("616960").stdin("44819").stdin("0").stdout("[vV]alid[\.]*", "valid", timeout = 60, regex = True)

@check50.check(compiles)
def runs():
    """UPC.java finds another valid UPC"""
    check50.run("java UPC").stdin("076783").stdin("00450").stdin("4").stdout("[vV]alid[\.]*", "valid", timeout = 60, regex = True)

@check50.check(compiles)
def runs60():
    """UPC.java finds an invalid UPC"""
    check50.run("java UPC").stdin("076783").stdin("00450").stdin("6").stdout("[Ii]nvalid[\.]*", "invalid", timeout = 60, regex = True)