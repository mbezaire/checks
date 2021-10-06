# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """initials.c exists"""
    check50.exists("largest_digit.c")

@check50.check(exists)
def compiles():
    """initials.c compiles"""
    check50.c.compile("initials.c", lcs50=True)

@check50.check(compiles)
def full_name():
    """A full name returns both initials"""
    check50.run("./initials").stdin("Tina Fey").stdout("T F\n").exit(0)

@check50.check(compiles)
def three_word():
    """A 3 word name returns 3 initials"""
    check50.run("./initials").stdin("John Kabat Zinn").stdout("JKZ\n").exit(0)

@check50.check(compiles)
def extra():
    """Extraneous characters are ignored"""
    check50.run("./initials").stdin("Grace #Hopper").stdout("G H\n").exit(0)
