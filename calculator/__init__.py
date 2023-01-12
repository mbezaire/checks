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
    """+ - 3 4 5 yields"""
    out = check50.run("./calculator + - 3 4 5").stdout()
    if abs(float(out) - 4.000000) > 0.00001:
        raise check50.Mismatch(out, 4.000000, help='Answer should be within 0.00001 of the expected value')

@check50.check(compiles)
def calc_ex2():
    """x - 3.4 5.6 7.9 yields"""
    out = check50.run("./calculator x - 3.4 5.6 7.9").stdout()
    if abs(float(out) - -17.379999) > 0.00001:
        raise check50.Mismatch(out, -17.379999, help='Answer should be within 0.00001 of the expected value')


@check50.check(compiles)
def calc_ex3():
    """+ - / 4 2 24 x 8 9 yields"""
    out = check50.run("./calculator + - / 4 2 24 x 8 9").stdout()
    if abs(float(out) - 50.000000) > 0.00001:
        raise check50.Mismatch(out, 50.000000, help='Answer should be within 0.00001 of the expected value')

