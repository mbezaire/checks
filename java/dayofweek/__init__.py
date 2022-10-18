# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c

classname = 'DayOfWeek'

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
    """Program should say Jan 5, 2022 is Wednesday (3)"""
    check50.run(f"java {classname}").stdin("6").stdin("5").stdout("3", timeout = 60)

@check50.check(compiles)
def runs60():
    """Program should say Jan 30, 2023 is Monday (1)"""
    check50.run(f"java {classname}").stdin("0").stdin("30").stdout("1", timeout = 60)

@check50.check(compiles)
def runs59():
    """Program should say Jan 22, 2023 is Sunday (0)"""
    check50.run(f"java {classname}").stdin("0").stdin("22").stdout("0", timeout = 60)
 
@check50.check(compiles)
def runs89():
    """Program should say Jan 13, 2024 is Saturday (6)"""
    check50.run(f"java {classname}").stdin("1").stdin("13").stdout("6", timeout = 60)

