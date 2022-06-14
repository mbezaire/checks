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
    """encode.c exists"""
    check50.exists("Fraction.java")

@check50.check(exists)
def compiles():
    """Fraction.java compiles"""
    check50.run("javac Fraction.java")

@check50.check(compiles)
def runs():
    """Fraction.java runs"""
    check50.run("javac FClient.java")
    check50.run("java FClient")
    
@check50.check(compiles)
def makequarter():
    """A 1/4 fraction is instantiated and prints"""
    out = check50.run("/opt/jdk-18.0.1.1/bin/javac -d ./ FClient.java").stdout()
    check50.log("compile in current dir: " + out)

    out = check50.run("/opt/jdk-18.0.1.1/bin/java FClient").stdout()
    
    check50.log(check50.run("ls").stdout())
    if out != "1/4\n":
        raise check50.Failure("Instead it printed:\n" + ".", help=out)
    
    #check50.run("/opt/jdk-18.0.1.1/bin/javac ./FClient.java")
    #check50._api.run("/opt/jdk-18.0.1.1/bin/java ./FClient").stdout("1/4\n").exit(0)
    #check50._api.run("/opt/jdk-18.0.1.1/bin/java ./FClient.class").stdout("1/4\n").exit(0)
    
# @check50.check(compiles)
# def divide():
#     """Fractions can be divided"""
#     check50.run("javac F2Client.java")
#     check50._api.run("java F2Client").stdin("1 4 1 3").stdout("12/1\n").exit(0)


# @check50.check(compiles)
# def multiply():
#     """Fractions can be multiplied"""
#     check50.run("javac F3Client.java")
#     check50._api.run("java F3Client").stdin("1 4 1 3").stdout("1/12\n").exit(0)


# @check50.check(compiles)
# def add():
#     """Fractions can be added"""
#     check50.run("javac F4Client.java")
#     check50._api.run("java F4Client").stdin("1 4 1 3").stdout("7/12\n").exit(0)

# @check50.check(compiles)
# def subtract():
#     """Fractions can be subtracted"""
#     check50.run("javac F5Client.java")
#     check50._api.run("java F5Client").stdin("1 3 1 4").stdout("1/12\n").exit(0)