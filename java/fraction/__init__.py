# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

check50.include("FClient.java", "F1Client.java", "F2Client.java", "F3Client.java", "F4Client.java", "F5Client.java")

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
def divide():
    """Fractions can be divided"""
    out = check50.run("javac -d ./ F2Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
    check50.run("java F2Client").stdin("1", prompt=False).stdin("3", prompt=False).stdin("1", prompt=False).stdin("4", prompt=False).stdout("4/3\n").exit(0)


@check50.check(compiles)
def multiply():
    """Fractions can be multiplied"""
    out = check50.run("javac -d ./ F3Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
    check50.run("java F3Client").stdin("1", prompt=False).stdin("3", prompt=False).stdin("1", prompt=False).stdin("4", prompt=False).stdout("1/12\n").exit(0)


@check50.check(compiles)
def add():
    """Fractions can be added"""
    out = check50.run("javac -d ./ F4Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
    check50.run("java F4Client").stdin("1", prompt=False).stdin("3", prompt=False).stdin("1", prompt=False).stdin("4", prompt=False).stdout("7/12\n").exit(0)

@check50.check(compiles)
def subtract():
    """Fractions can be subtracted"""
    out = check50.run("javac -d ./ F5Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
    check50.run("java F5Client").stdin("1", prompt=False).stdin("3", prompt=False).stdin("1", prompt=False).stdin("4", prompt=False).stdout("1/12\n").exit(0)


@check50.check(compiles)
def getvalue():
    """Fraction value can be computed"""
    out = check50.run("javac -d ./ F0Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
    check50.run("java F0Client").stdin("1", prompt=False).stdin("4", prompt=False).stdout("0.25\n").exit(0)
