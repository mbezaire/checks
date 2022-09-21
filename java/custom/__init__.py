# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

check50.include("Bookstore.class")

# not working in sandbox
# less = check50.import_checks("https://github.com/mbezaire/checks/main/java/fraction")
# from less import *


@check50.check()
def exists():
    """Book.java exists"""
    check50.exists("Book.java")

@check50.check()
def authexists():
    """Author.java exists"""
    check50.exists("Author.java")

@check50.check()
def customexists():
    """CustomBookstore.java exists"""
    check50.exists("CustomBookstore.java")

@check50.check()
def demoexists():
    """DemoClient.java exists"""
    check50.exists("DemoClient.java")
    
@check50.check(exists)
def compiles():
    """Book.java compiles"""
    check50.run("javac Book.java").stdout("")
    
@check50.check(authexists)
def authcompiles():
    """Author.java compiles"""
    check50.run("javac Author.java").stdout("")
    
@check50.check(authexists)
def customcompiles():
    """CustomBookstore.java compiles"""
    check50.run("javac CustomBookstore.java").stdout("")
    
@check50.check(authexists)
def democompiles():
    """DemoClient.java compiles"""
    check50.run("javac DemoClient.java").stdout("")

