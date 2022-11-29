# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """time_program.c was submitted"""
    check50.exists("time_program.c")

@check50.check(exists)
def compiles():
    """time_program.c compiles"""
    check50.c.compile("time_program.c", lcs50=True)


@check50.check(compiles)
def runs():
    """time_program.c runs"""
    check50.c.run("./time_program").stdin("02:31:15").stdin("12:05:00").stdout("09:33:45").exit(0)


@check50.check()
def dexists():
    """struct_address.c was submitted"""
    check50.exists("struct_address.c")

@check50.check(dexists)
def dcompiles():
    """struct_address.c compiles"""
    check50.c.compile("struct_address.c", lcs50=True)
