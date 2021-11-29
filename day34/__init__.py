# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """warmup1.txt and warmup2.c were submitted"""
    check50.exists("warmup1.txt")
    check50.exists("warmup2.c")

@check50.check(exists)
def compiles():
    """warmup2.c compiles"""
    check50.c.compile("warmup2.c", lcs50=True)
