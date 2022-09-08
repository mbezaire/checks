# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

check50.include("BClient.java")

# not working in sandbox
# less = check50.import_checks("https://github.com/mbezaire/checks/main/java/fraction")
# from less import *


@check50.check()
def exists():
    """Book.java exists"""
    check50.exists("Book.java")

@check50.check(exists)
def compiles():
    """Book.java compiles"""
    check50.run("javac Book.java")

@check50.check(compiles)
def runs():
    """Book.java runs"""
    out = check50.run("javac -d ./ BClient.java").stdout(timeout = 60)
    check50.log(out)
    check50.log(check50.run("pwd").stdout())
    check50.log(check50.run("ls ./").stdout())
    out2 = check50.run("java BClient").stdout()
    check50.log(out2)


# @check50.check(compiles)
# def reduce():
#     """A book has a price and a toString"""
#     out = check50.run("javac -d ./ B1Client.java").stdout(timeout = 60)

    
#     from re import match

#     expected = "[Aa]n {Ii]mmense [Ww]orld[\n\t\s]*[bByY :]+Ed Yong[\n\t\s]*[$0-9\.]+"
#     actual = check50.run("java B1Client").stdout()
#     if not match(expected, actual):
#         help = None
#         raise check50.Mismatch("An Immense World\nBy Ed Yong\n$85.43", actual, help=help)

