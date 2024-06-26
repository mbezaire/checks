# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

def fix(out):
    return out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true\n", "").strip()

def checkit(out, answer):
    if fix(out) != answer:
        if fix(out) not in answer:
            raise check50.Mismatch(answer, fix(out))


@check50.check()
def compiles():
    """Duration.java exists and compiles"""
    check50.exists("Duration.java")
    check50.run("javac Duration.java")
    check50.include("Client.java","CBlient.java","CClient.java")
    out = check50.run("javac -d ./ Client.java CBlient.java CClient.java").stdout(timeout = 180)
    check50.log(out)

@check50.check(compiles)
def runs1():
    """Duration.java's getSeconds method returns the right seconds for 3777 seconds"""
    out = check50.run("java Client").stdin("3777", prompt = False).stdin("seconds", prompt = False).stdout(timeout = 120)
    checkit(out, "3777")

@check50.check(compiles)
def runs2():
    """Duration.java's getSeconds method returns the right seconds for 2 minutes"""
    out = check50.run("java Client").stdin("2", prompt = False).stdin("minutes", prompt = False).stdout(timeout = 120)
    checkit(out, "120")

@check50.check(compiles)
def runs3():
    """Duration.java's getSeconds method returns the right seconds for 33 hours"""
    out = check50.run("java Client").stdin("33", prompt = False).stdin("hours", prompt = False).stdout(timeout = 120)
    checkit(out, "118800")

@check50.check(runs2)
def tostring1():
    """Duration.java's toString method produces the correct String for 3777 seconds"""
    out = check50.run("java Duration").stdin("3777 seconds", prompt = True).stdout(timeout = 120)
    checkit(out, "0 days, 1 hours, 2 minutes, 57 seconds")

@check50.check(runs2)
def tostring2():
    """Duration.java's toString method produces the correct String for 374437 seconds"""
    out = check50.run("java Duration").stdin("374437 seconds", prompt = True).stdout(timeout = 120)
    checkit(out, "4 days, 8 hours, 0 minutes, 37 seconds")

@check50.check(runs2)
def tostring3():
    """Duration.java's toString method produces the correct String for 1682 hours"""
    out = check50.run("java Duration").stdin("1682 hours", prompt = True).stdout(timeout = 120)
    checkit(out, "70 days, 2 hours, 0 minutes, 0 seconds")


@check50.check(tostring3)
def longer1():
    """Duration.java correctly reports the longer Duration"""
    out = check50.run("java CBlient").stdin("3 hours", timeout = 120, prompt = True).stdin("45039 seconds", timeout = 120, prompt = True).stdout(timeout = 120)
    checkit(out, "false\nfalse\ntrue")


@check50.check(tostring3)
def longer2():
    """Duration.java again correctly reports the longer Duration"""
    out = check50.run("java CBlient").stdin("63 minutes", timeout = 120, prompt = True).stdin("1 hours", timeout = 120, prompt = True).stdout(timeout = 120)
    checkit(out, "true\nfalse\nfalse")


@check50.check(longer2)
def add1():
    """Duration.java correctly adds Durations"""
    out = check50.run("java CClient").stdin("63 minutes", timeout = 120, prompt = True).stdin("1 hours", timeout = 120, prompt = True).stdout(timeout = 120)
    checkit(out, "0 days, 2 hours, 3 minutes, 0 seconds\n123 minutes")

@check50.check(longer2)
def add2():
    """Duration.java again correctly adds Durations"""
    out = check50.run("java CClient").stdin("370 seconds", timeout = 120, prompt = True).stdin("0 hours", timeout = 120, prompt = True).stdout(timeout = 120)
    checkit(out, "0 days, 0 hours, 6 minutes, 10 seconds\n370 seconds")