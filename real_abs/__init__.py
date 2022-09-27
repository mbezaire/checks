# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """real_abs.c exists"""
    check50.exists("real_abs.c")

@check50.check(exists)
def compiles():
    """real_abs.c compiles"""
    check50.c.compile("real_abs.c", lcs50=True)

@check50.check(compiles)
def real_abs_pos():
    """A positive number stays positive"""
    check50.run("./real_abs").stdin("5").stdout("5.000000\n").exit(0)

@check50.check(compiles)
def real_abs_neg():
    """A negative number goes positive"""
    check50.run("./real_abs").stdin("-5").stdout("5.000000\n").exit(0)