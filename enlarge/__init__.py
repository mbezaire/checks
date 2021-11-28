# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """enlarge.c exists"""
    check50.exists("enlarge.c")
    check50.exists("bmp.h")

@check50.check(exists)
def compiles():
    """enlarge.c compiles - Further manual checks will happen!"""
    check50.c.compile("enlarge.c", lcs50=True)
