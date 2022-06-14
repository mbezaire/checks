# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

check50.include("FClient.java", "F6Client.java", "F7Client.java")

# not working in sandbox
# less = check50.import_checks("https://github.com/mbezaire/checks/main/java/fraction")
# from less import *


@check50.check()
def exists():
    """Fraction.java exists"""
    check50.exists("Fraction.java")

@check50.check(exists)
def compiles():
    """Fraction.java compiles"""
    check50.run("javac Fraction.java")

@check50.check(compiles)
def runs():
    """Fraction.java runs"""
    out = check50.run("javac -d ./ FClient.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
    check50.run("java FClient").stdout("1/4\n")


@check50.check(compiles)
def makedouble():
    """Fractions can be constructed from a double"""
    out = check50.run("javac -d ./ F7Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
    check50.run("java F7Client").stdin("1.25", prompt=False).stdout("5/4\n").exit(0)

@check50.check(compiles)
def reduce():
    """Fractions can be reduced"""
    out = check50.run("javac -d ./ F6Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
    check50.run("java F6Client").stdin("13", prompt=False).stdin("52", prompt=False).stdout("1/4\n").exit(0)

