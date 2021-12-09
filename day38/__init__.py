# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """day38.c was submitted"""
    check50.exists("day38.c")

@check50.check(exists)
def compiles():
    """day38.c compiles"""
    check50.c.compile("day38.c", lcs50=True)
