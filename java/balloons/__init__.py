# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c
import os


@check50.check()
def exists():
    """Balloon files exist (Round, Oval, Square, Fancy)"""
    check50.exists("RoundBalloon.java").exists("OvalBalloon.java").exists("SquareBalloon.java").exists("FancyBalloon.java")

        
        
# @check50.check(compiles)
# def getvalue():
#     """Fraction value can be computed"""
#     out = check50.run("javac -d ./ F0Client.java").stdout(timeout = 60)
    # check50.log(out)
    # check50.log(check50.run("pwd").stdout())
    # check50.log(check50.run("ls ./").stdout())
#     check50.run("java F0Client").stdin("1", prompt=False).stdin("4", prompt=False).stdout("0.25\n").exit(0)
