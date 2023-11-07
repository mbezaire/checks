# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """custom.c exists"""
    check50.exists("custom.c")

@check50.check(exists)
def compiles():
    """custom.c compiles"""
    check50.c.compile("custom.c", lcs50=True)

