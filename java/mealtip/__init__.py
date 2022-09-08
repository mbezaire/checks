# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

# check50.include("Client.java", "M1Client.java")

@check50.check()
def exists():
    """MealTip.java exists"""
    check50.exists("MealTip.java")

@check50.check(exists)
def compiles():
    """MealTip.java compiles"""
    check50.run("javac MealTip.java")

@check50.check(compiles)
def runs():
    """MealTip.java runs"""
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
    out = check50.run("java MealTip").stdout()
    check50.log(out)
