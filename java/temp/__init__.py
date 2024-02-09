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
    """Temperature.java exists"""
    check50.exists("Temperature.java")

@check50.check(exists)
def compiles():
    """Temperature.java compiles"""
    out = check50.run("javac -d ./ Temperature.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

@check50.check(compiles)
def runs():
    """Temperature.java converts 41 degrees Fahrenheit correctly"""
    check50.run("java Temperature").stdin("41").stdout('5.0[0-9]*[ ]+[cC]elsius','5.0 Celsius\n',regex = True, timeout = 10);

@check50.check(compiles)
def runs2():
    """Temperature.java converts 212 degrees Fahrenheit correctly"""
    check50.run("java Temperature").stdin("212").stdout('100.0[0-9]*[ ]+[cC]elsius','100.0 Celsius\n',regex = True, timeout = 10);


@check50.check(compiles)
def runs3():
    """Temperature.java converts 70 degrees Fahrenheit correctly"""
    check50.run("java Temperature").stdin("70").stdout('21.11[0-9]*[ ]+[cC]elsius', '21.11111111 Celsius\n',regex = True, timeout = 10);
