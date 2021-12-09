# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """day39.c was submitted"""
    check50.exists("day39.c")

@check50.check(exists)
def compiles():
    """day39.c compiles"""
    check50.c.compile("day39.c", lcs50=True)
