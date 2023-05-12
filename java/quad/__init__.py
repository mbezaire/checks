# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

#check50.include("FClient.java", "F0Client.java", "F1Client.java", "F2Client.java", "F3Client.java", "F4Client.java", "F5Client.java")

@check50.check()
def exists():
    """Quad.java exists"""
    check50.exists("Quad.java")

@check50.check(exists)
def compiles():
    """Quad.java compiles"""
    check50.run("javac Quad.java")

@check50.check(compiles)
def runs():
    """Quad.java runs"""
    check50.run("java Quad").stdin("1").stdin("3").stdin("2").stdout("x = -1 and -2\n")
