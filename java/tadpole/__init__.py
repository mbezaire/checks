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
    flag = True
    for item in answer:
        if item not in out:
            flag = False
            break

    if not flag:
        raise check50.Mismatch("...\n".join(answer), fix(out))


@check50.check()
def compiles():
    """Tadpole.java exists and compiles"""
    check50.exists("Tadpole.java")
    check50.run("javac Tadpole.java")

@check50.check(compiles)
def runs1():
    """Tadpole.java runs a full frog population correctly"""
    out = check50.run("java Tadpole").stdin("1234").stdout(timeout = 290)
    checkit(out, ["1234 eggs left at day ","135 tadpoles left at day ","36 froglets left at day ","6 frogs left at day "])

@check50.check(compiles)
def runs2():
    """Tadpole.java ensures realistic nest size"""
    out = check50.run("java Tadpole").stdin("2392").stdout(timeout = 290)
    checkit(out, ["2000 eggs left at day ","220 tadpoles left at day ","59 froglets left at day ","10 frogs left at day "])


@check50.check(compiles)
def runs3():
    """Tadpole.java ensures realistic nest size on other end"""
    out = check50.run("java Tadpole").stdin("-55").stdout(timeout = 290)
    checkit(out, ["1 eggs left at day ","0 tadpoles left at day ","0 froglets left at day ","0 frogs left at day "])
