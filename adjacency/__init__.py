# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """adjacency.c was submitted"""
    check50.exists("adjacency.c")

@check50.check(exists)
def compiles():
    """adjacency.c compiles"""
    check50.c.compile("adjacency.c", lcs50=True)

@check50.check(compiles)
def runs2():
    """adjacency.c prints the correct numbers"""
    check50.c.run("./adjacency").stdout("3 4 3 2 \n4 5 4 2 \n4 4 4 1 \n2 2 3 1 \n").exit(0)


@check50.check(compiles)
def runs():
    """adjacency function looks good"""
    check50.include('test1.c')
    check50.c.compile("test1.c", lcs50=True)

    check50.c.run("./test1").stdout("3432454244412231\n").exit(0)


@check50.check(compiles)
def runs3():
    """adjacency function works for another table"""
    check50.include('test2.c')
    check50.c.compile("test2.c", lcs50=True)
    check50.c.run("./test2").stdout("1232246436962464\n").exit(0)

