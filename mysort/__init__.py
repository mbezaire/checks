# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c
import random

@check50.check()
def exists():
    """mysort.c exists"""
    check50.exists("mysort.c")

@check50.check(exists)
def compiles():
    """mysort.c compiles"""
    check50.c.compile("mysort.c", lcs50=True)

@check50.check(compiles)
def short_phrase():
    """Numbers are sorted"""
    err_null = False
    randint1 = random.randint(8,23)
    randint2 = random.randint(45,68)
    if randint2 % 2 == 0:
        randint3 = random.randint(80,99)
        out = check50.run(f"./mysort 79 {randint3} 2 {randint1} 34 3 {randint2} 7").stdout()
        out = out.strip()
        ans = f"2 3 7 {randint1} 34 {randint2} 79 {randint3}"
    else:
        out = check50.run(f"./mysort 79 2 {randint1} 34 3 {randint2} 7").stdout()
        out = out.strip()
        ans = f"2 3 7 {randint1} 34 {randint2} 79"
    if len(out) == 0:
        raise check50.Mismatch(ans, "", help='You may be printing an empty string or only white space')
    elif out!=ans:
        raise check50.Mismatch(ans, out, help='Make sure you take in command line arguments and sort them from least to greatest and print all of them out, separated by a space, on the same line')