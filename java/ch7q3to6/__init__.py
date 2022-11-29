# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

check50.include("FClient.java", "F0Client.java", "F1Client.java", "F2Client.java", "F3Client.java", "F4Client.java", "F5Client.java")

@check50.check()
def exists():
    """Chapter7part1.java exists"""
    check50.exists("Chapter7part1.java")

@check50.check(exists)
def compiles():
    """Chapter7part1.java compiles"""
    check50.run("javac Chapter7part1.java")


@check50.check()
def dexists():
    """HelloNTimes.java exists"""
    check50.exists("HelloNTimes.java")

@check50.check(dexists)
def dcompiles():
    """HelloNTimes.java compiles"""
    check50.run("javac HelloNTimes.java")

@check50.check(compiles)
def run1():
    """calcSum works correctly"""
    check50.include("FClient.java")
    out = check50.run("java FClient").stdout()
    if out != "true":
        raise check50.Failure("calcSum doesn't give the right answer")

@check50.check(compiles)
def run2():
    """product calculates 5 and 9 as 45"""
    check50.include("F0Client.java")
    check50.run("java F0Client").stdin("5", prompt = False).stdin("9", prompt = False).stdout("45")

@check50.check(compiles)
def run3():
    """product calculates 6 and 0 as 0"""
    check50.include("F0Client.java")
    check50.run("java F0Client").stdin("6", prompt = False).stdin("0", prompt = False).stdout("0")

@check50.check(compiles)
def run4():
    """product calculates 1 and 5 as 5"""
    check50.include("F0Client.java")
    check50.run("java F0Client").stdin("1", prompt = False).stdin("5", prompt = False).stdout("5")

@check50.check(compiles)
def run5():
    """nextAlgorithm works correctly"""
    check50.include("F1Client.java")
    out = check50.run("java F1Client").stdout()
    if out != "true":
        raise check50.Failure("nextAlgorithm doesn't give the right answer")


@check50.check(compiles)
def run6():
    """division calculates 45/6 correctly"""
    check50.include("F2Client.java")
    check50.run("java F2Client").stdin("45", prompt = False).stdin("6", prompt = False).stdout("45/6 gives\nquotient: 7, remainder: 3")
        

@check50.check(compiles)
def run7():
    """division calculates 13/30 correctly"""
    check50.include("F2Client.java")
    check50.run("java F2Client").stdin("13", prompt = False).stdin("30", prompt = False).stdout("13/30 gives\nquotient: 0, remainder: 13")
        

@check50.check(compiles)
def run8():
    """division calculates 14/7 correctly"""
    check50.include("F2Client.java")
    check50.run("java F2Client").stdin("14", prompt = False).stdin("7", prompt = False).stdout("14/7 gives\nquotient: 2, remainder: 0")
 
@check50.check(compiles)
def run9():
    """populationMexico forecasts 150 correctly"""
    check50.include("F3Client.java")
    check50.run("java F3Client").stdin("150").stdout("2053")
        
@check50.check(compiles)
def run10():
    """populationMexico goes back in time"""
    check50.include("F3Client.java")
    check50.run("java F3Client").stdin("120").stdout("2014")
        
@check50.check(compiles)
def run11():
    """populationMexico forecasts 130 alright"""
    check50.include("F3Client.java")
    check50.run("java F3Client").stdin("130").stdout("2024")
        
@check50.check(dcompiles)
def druns1():
    """HelloNTimes.java prints correctly"""
    check50.run("java HelloNTimes.java").stdin("2").stdin("Hello").stdout("Hello\nHello\n").exit(0)
                
@check50.check(dcompiles)
def druns2():
    """HelloNTimes.java prints correctly"""
    check50.run("java HelloNTimes.java").stdin("3").stdin("Ho").stdout("Ho\nHo\nHo\n").exit(0)