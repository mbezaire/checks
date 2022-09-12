# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c


@check50.check()
def exists():
    """hello.py exists"""
    check50.exists("hello.py")
    
@check50.check(exists)
def runs():
    """hello.py runs"""
    check50.run"python hello.py")
