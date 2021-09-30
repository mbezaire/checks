# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50

@check50.check()
def exists():
    """largest_digit.c exists"""
    check50.require("largest_digit.c")

@check50.check(exists)
def compiles():
    """largest_digit.c compiles"""
    check50.c.compile("largest_digit.c", lcs50=True)

@check50.check(compiles)
def largest_digit_pos():
    """The largest digit of a positive number is returned"""
    check50.run("./largest_digit").stdin("28451").stdout("8\n").exit(0)

@check50.check(compiles)
def largest_digit_neg():
    """The largest digit of a negative number is returned"""
    check50.run("./largest_digit").stdin("-28451").stdout("8\n").exit(0)

@check50.check(compiles)
def largest_digit_tie():
    """One digit is returned in a tie"""
    check50.run("./largest_digit").stdin("4444").stdout("4\n").exit(0)

@check50.check("compiles")
def largest_digit_zero():
    """Zero returns zero"""
    check50.run("./largest_digit").stdin("0").stdout("0\n").exit(0)