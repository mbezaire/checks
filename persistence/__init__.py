# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """persistence.c was submitted"""
    check50.exists("persistence.c")

@check50.check(exists)
def compiles():
    """persistence.c compiles"""
    check50.c.compile("persistence.c", lcs50=True)

@check50.check(compiles)
def persistence0():
    """A single digit returns 0"""
    check50.run("./persistence").stdin("4").stdout("0", "0\n").exit(0)

@check50.check(compiles)
def persistence2():
    """A short digit returns 3"""
    check50.run("./persistence").stdin("39").stdout("3", "3\n").exit(0)

@check50.check(compiles)
def persistence3():
    """A long digit returns 4"""
    check50.run("./persistence").stdin("999").stdout("4", "4\n").exit(0)

@check50.check(compiles)
def persistence6():
    """A long digit returns 1"""
    check50.run("./persistence").stdin("111112").stdout("1", "1\n").exit(0)
