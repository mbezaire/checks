# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c
from re import match


check50.include("BClient.java","B1Client.java","B2Client.java")

@check50.check()
def exists():
    """Book.java, Author.java, and Client.java exist"""
    check50.exists("Book.java")
    check50.exists("Author.java")
    check50.exists("Client.java")

    
@check50.check(exists)
def compiles():
    """Files compile"""
    check50.run("javac Book.java Author.java Client.java")

@check50.check(compiles)
def runs():
    """Book.java runs"""
    check50.include("BClient.java","B1Client.java","B2Client.java")
    out = check50.run("javac -d ./ BClient.java").stdout(timeout = 60)
    check50.log(out)
    check50.log(check50.run("pwd").stdout())
    check50.log(check50.run("ls ./").stdout())
    out2 = check50.run("java BClient").stdout()
    check50.log(out2)

@check50.check(runs)
def book1():
    """A book has a price and a toString"""
    out = check50.run("javac -d ./ B1Client.java").stdout(timeout = 60)
    expected = r"[Aa]n [Ii]mmense [Ww]orld[\n\t\s]*[bByY :]+Ed Yong[\n\t\s]*[$0-9\.]+"
    check50.run("java B1Client").stdout(expected, regex=True)

@check50.check(runs)
def book2():
    """Another book has a price and a toString"""
    out = check50.run("javac -d ./ B2Client.java").stdout(timeout = 60)
    expected = r"[Aa]n [Ii]mmense [Ww]orld[\n\t\s]*[bByY :]+Ed Yong[\n\t\s]*[$0-9\.]+"
    check50.run("java B2Client").stdout(expected, regex=True)


