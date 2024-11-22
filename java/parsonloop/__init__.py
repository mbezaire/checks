# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """Program exists"""
    check50.exists("ParsonLoop.java")        

@check50.check(exists)
def contents():
    """Program is an ordered version of its original"""
    check50.include("Orig.java")

    with open("ParsonLoop.java") as f:
        contents = f.read().replace('\n','').replace('{','').replace('}','')

    with open("Orig.java") as f:
        lines = f.readlines()

    for line in lines:
        print(len(contents))
        contents = contents.replace(line.replace("{","").replace("}","").strip(),"")

    contents = contents.strip()
    check50.log(contents)
    if len(contents) > 50:
        raise check50.Failure("There may be an issue with your program code")


@check50.check(contents)
def compiles():
    """Program compiles"""
    check50.c.compile("parson.c") #, lcs50=True)


@check50.check(compiles)
def runs():
    """Program runs alright"""
    check50.include("data.txt")
    check50.run(f"./parson").stdout("Anya: 94\nArnold: 93\nAnwar: 91\nAvery: 95\nAnnalise: 98\nAmy: 90\nAndrew: 92").exit(0)


@check50.check(runs)
def valgrinds():
    """Valgrind likes the program"""
    check50.c.valgrind(f"./parson").stdout("Anya: 94\nArnold: 93\nAnwar: 91\nAvery: 95\nAnnalise: 98\nAmy: 90\nAndrew: 92").exit(0)
