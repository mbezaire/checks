# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """matrix.c exists"""
    check50.exists("matrix.c")

@check50.check(exists)
def compiles():
    """matrix.c compiles"""
    check50.c.compile("matrix.c", lcs50=True)

@check50.check(compiles)
def spacey_phrase():
    """A 2d array prints correctly"""
    check50.run("./matrix 3 4").stdout("2 3 3 2[\s]{0,1}\n3 4 4 3[\s]{0,1}\n2 3 3 2[\s]{0,1}[\n]{0,1}", "2 3 3 2\n3 4 4 3\n2 3 3 2\n", regex=True).exit(0)

@check50.check(compiles)
def spacey_phrase1():
    """A wide array prints correctly"""
    check50.run("./matrix 1 5").stdout("1 2 2 2 1[\s]{0,1}[\n]{0,1}", "1 2 2 2 1\n", regex=True).exit(0)

@check50.check(compiles)
def spacey_phrase2():
    """A tall array prints correctly"""
    check50.run("./matrix 4 1").stdout("1[\s]{0,1}[\n]2[\s]{0,1}[\n]2[\s]{0,1}[\n]1[\s]{0,1}[\n]{0,1}", "1\n2\n2\n1\n", regex=True).exit(0)



@check50.check()
def dexists():
    """diagonal.c exists"""
    check50.exists("diagonal.c")

@check50.check(dexists)
def dcompiles():
    """diagonal.c compiles"""
    check50.c.compile("diagonal.c", lcs50=True)

@check50.check(dcompiles)
def dspacey_phrase():
    """A 2d array prints correctly and includes diagonals"""
    check50.run("./diagonal 3 4").stdout("3 5 5 3[\s]{0,1}\n5 8 8 5[\s]{0,1}\n3 5 5 3[\s]{0,1}[\n]{0,1}", "3 5 5 3\n5 8 8 5\n3 5 5 3\n", regex=True).exit(0)

@check50.check(dcompiles)
def dspacey_phrase1():
    """A wide array prints correctly, including diagonals"""
    check50.run("./diagonal 1 5").stdout("1 2 2 2 1[\s]{0,1}[\n]{0,1}", "1 2 2 2 1\n", regex=True).exit(0)

@check50.check(dcompiles)
def dspacey_phrase2():
    """A tall array prints correctly, including diagonals"""
    check50.run("./diagonal 4 1").stdout("1[\s]{0,1}[\n]2[\s]{0,1}[\n]2[\s]{0,1}[\n]1[\s]{0,1}[\n]{0,1}", "1\n2\n2\n1\n", regex=True).exit(0)


