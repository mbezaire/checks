# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50

@check50.check()
def exists():
    """restaurant.c exists"""
    check50.require("restaurant.c")

@check50.check("exists")
def compiles():
    """restaurant.c compiles"""
    check50.spawn("clang -o restaurant restaurant.c -lcs50 -lm").exit(0)

@check50.check("compiles")
def restaurant_style_you():
    """A stylish date and me"""
    check50.spawn("./restaurant").stdin("8").stdin("5").stdout("2\n").exit(0)

@check50.check("compiles")
def restaurant_style_me():
    """A  date and stylish me"""
    check50.spawn("./restaurant").stdin("3").stdin("8").stdout("2\n").exit(0)

@check50.check("compiles")
def restaurant_you_me():
    """A  date and  me"""
    check50.spawn("./restaurant").stdin("3").stdin("5").stdout("1\n").exit(0)

@check50.check("compiles")
def restaurant_noyou_me():
    """A non-stylish date and  me"""
    check50.spawn("./restaurant").stdin("8").stdin("1").stdout("0\n").exit(0)

@check50.check("compiles")
def restaurant_you_nome():
    """A  date and non-stylish me"""
    check50.spawn("./restaurant").stdin("1").stdin("8").stdout("0\n").exit(0)
