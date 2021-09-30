# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50

@check50.check()
def exists():
    """real_abs.c exists"""
    check50.require("real_abs.c")

@check50.check("exists")
def compiles():
    """real_abs.c compiles"""
    check50.spawn("clang -o real_abs real_abs.c -lcs50 -lm").exit(0)

@check50.check("compiles")
def real_abs_pos():
    """A positive number stays positive"""
    check50.spawn("./real_abs").stdin("5").stdout("5\n").exit(0)

@check50.check("compiles")
def real_abs_neg():
    """A negative number goes positive"""
    check50.spawn("./real_abs").stdin("-5").stdout("5\n").exit(0)