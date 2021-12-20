# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """calculator.c was submitted"""
    check50.exists("calculator.c")

@check50.check(exists)
def compiles():
    """calculator.c compiles"""
    check50.c.compile("calculator.c", lcs50=True)

@check50.check(compiles)
def calc_ex1():
    """+ - 3 4 5 yields 4.000000"""
    check50.run("./calculator + - 3 4 5").stdout("4.000000\n", "4.000000\n").exit(0)


@check50.check(compiles)
def calc_ex2():
    """x - 3.4 5.6 7.9 yields"""
    check50.run("./calculator x - 3.4 5.6 7.9").stdout("-17.3799999\n", "-17.3799999\n").exit(0)


@check50.check(compiles)
def calc_ex3():
    """+ - / 4 2 24 x 8 9 yields"""
    check50.run("./calculator + - / 4 2 24 x 8 9").stdout("50.000000\n", "50.000000\n").exit(0)


