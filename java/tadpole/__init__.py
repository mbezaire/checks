# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c
from re import match

def fix(out):
    return out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true\n", "").strip()

def checkit(out, answer):
    if not match(answer, fix(out)):
        raise check50.Mismatch(answer, fix(out))


@check50.check()
def compiles():
    """Tadpole.java exists and compiles"""
    check50.exists("Tadpole.java")
    check50.run("javac Tadpole.java")

@check50.check(compiles)
def runs1():
    """Tadpole.java runs a full frog population correctly"""
    out = check50.run("java Tadpole").stdin("1234").stdout(timeout = 120)
    checkit(out, "1234 eggs left at day [0-9]+\n135 tadpoles left at day [0-9]+\n36 froglets left at day [0-9]+\n6 frogs left at day [0-9]+")

@check50.check(compiles)
def runs2():
    """Tadpole.java ensures realistic nest size"""
    out = check50.run("java Tadpole").stdin("2392").stdout(timeout = 120)
    checkit(out, "2000 eggs left at day [0-9]+\n220 tadpoles left at day [0-9]+\n59 froglets left at day [0-9]+\n10 frogs left at day [0-9]+")


@check50.check(compiles)
def runs3():
    """Tadpole.java ensures realistic nest size on other end"""
    out = check50.run("java Tadpole").stdin("-55").stdout(timeout = 120)
    checkit(out, "1 eggs left at day [0-9]+\n0 tadpoles left at day [0-9]+\n0 froglets left at day [0-9]+\n0 frogs left at day [0-9]+")
