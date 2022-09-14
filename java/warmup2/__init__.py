# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """Warmup2.java exists"""
    check50.exists("Warmup2.java")

@check50.check(exists)
def compiles():
    """Warmup2.java compiles"""
    check50.run("javac Warmup2.java")

# @check50.check(compiles)
# def runs():
#     """MealTip.java runs"""
#     # check50.log(check50.run("pwd").stdout())
#     # check50.log(check50.run("ls ./").stdout())
#     check50.run("javac MealTip.java")
#     out = check50.run("java MealTip").stdout()
#     check50.log(out)
