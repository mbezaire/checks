# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """struct_address.c and time_program.c were submitted"""
    check50.exists("struct_address.c")
    check50.exists("time_program.c")

@check50.check(exists)
def compiles():
    """struct_address.c and time_program.c compile"""
    check50.c.compile("struct_address.c", lcs50=True)
    check50.c.compile("time_program.c", lcs50=True)