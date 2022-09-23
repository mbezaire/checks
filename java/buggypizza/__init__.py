# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c


@check50.check()
def exists():
    """PizzaOrder.java exists"""
    check50.exists("PizzaOrder.java")


    
@check50.check(exists)
def compiles():
    """PizzaOrder.java compiles"""
    check50.run("javac PizzaOrder.java").stdout("")
