# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """words.c exists"""
    check50.exists("words.c")

@check50.check(exists)
def compiles():
    """words.c compiles"""
    check50.c.compile("words.c", lcs50=True)

@check50.check(compiles)
def words_pos():
    """When words are used with spaces around them, they are counted correctly"""
    check50.run("./words").stdout("very: 2\nstuff: 0\ninterestingly: 0\nseems: 0\nthings: 0\nlike: 2").exit(0)