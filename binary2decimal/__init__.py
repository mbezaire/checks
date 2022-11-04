# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """binary2decimal.c was submitted"""
    check50.exists("binary2decimal.c")

@check50.check(exists)
def compiles():
    """binary2decimal.c compiles"""
    check50.c.compile("binary2decimal.c", lcs50=True)

@check50.check(compiles)
def calc_ex1():
    """10000000 is 128"""
    check50.run("./binary2decimal").stdin("10000000").stdout("128").exit(0)


@check50.check(compiles)
def calc_ex2():
    """00000001 is 1"""
    check50.run("./binary2decimal").stdin("00000001").stdout("1").exit(0)


@check50.check(compiles)
def calc_ex3():
    """11111111 is 255"""
    check50.run("./binary2decimal").stdin("11111111").stdout("255").exit(0)



@check50.check(compiles)
def calc_ex3():
    """01010101 is 85"""
    check50.run("./binary2decimal").stdin("01010101").stdout("85").exit(0)
