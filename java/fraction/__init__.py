# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c


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
    check50.include("FClient.java", "F0Client.java", "F1Client.java", "F2Client.java", "F3Client.java", "F4Client.java", "F5Client.java")
    out = check50.run("javac -d ./ FClient.java F2Client.java F3Client.java F4Client.java  F5Client.java F0Client.java").stdout(timeout = 180)
    check50.log(out)
    check50.run("java FClient").stdout("1/4\n")
    
@check50.check(runs)
def divide():
    """Fractions can be divided"""
    check50.run("java F2Client").stdin("1", prompt=False).stdin("3", prompt=False).stdin("1", prompt=False).stdin("4", prompt=False).stdout("4/3\n").exit(0)


@check50.check(runs)
def multiply():
    """Fractions can be multiplied"""
    check50.run("java F3Client").stdin("1", prompt=False).stdin("3", prompt=False).stdin("1", prompt=False).stdin("4", prompt=False).stdout("1/12\n").exit(0)


@check50.check(runs)
def add():
    """Fractions can be added"""
    check50.run("java F4Client").stdin("1", prompt=False).stdin("3", prompt=False).stdin("1", prompt=False).stdin("4", prompt=False).stdout("7/12\n").exit(0)

@check50.check(runs)
def subtract():
    """Fractions can be subtracted"""
    check50.run("java F5Client").stdin("1", prompt=False).stdin("3", prompt=False).stdin("1", prompt=False).stdin("4", prompt=False).stdout("1/12\n").exit(0)


@check50.check(runs)
def getvalue():
    """Fraction value can be computed"""
    check50.run("java F0Client").stdin("1", prompt=False).stdin("4", prompt=False).stdout("0.25\n").exit(0)
