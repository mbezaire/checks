# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """predict program exists"""
    try:
        check50.exists("predict.c")
        return "predict.c"
    except:
        check50.exists("predict2.c")
        return "predict2.c"
        

@check50.check(exists)
def compiles(filename):
    """Program compiles"""
    check50.c.compile(filename) #, lcs50=True)
    return filename

@check50.check(compiles)
def valgrinds(filename):
    """Valgrind likes the program"""
    noext = filename[:-2]
    check50.c.valgrind(f"./{noext}").stdout().exit(0)
    return noext

@check50.check(valgrinds)
def runs(noext):
    """Program runs alright"""
    check50.run(f"./{noext}").stdout("Janelle\nJennifer\nGerald\nJune\n2018").exit(0)

    #TODO could add another check that includes the program as a library and uses insertnode function

