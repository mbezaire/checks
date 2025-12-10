# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """nametree.c was submitted"""
    check50.exists("nametree.c")

@check50.check(exists)
def compiles():
    """nametree.c compiles"""
    check50.c.compile("nametree.c", lcs50=True)

@check50.check(compiles)
def runs2():
    """nametree.c prints a list of Jonas Brothers"""
    check50.include("names.csv")
    check50.c.run("./nametree").stdout("Album\nFrankie\nJoe\nKevin\nNick\n").exit(0)


@check50.check(runs2)
def runs():
    """nametree.c prints a list of ppl who lived in Andover"""
    check50.include("names.csv")
    with open("names.csv", "w") as f:
        f.write("Michael\nJay\nRyan\nBriga\nMartin\nKara\nBlanchard\n")

    check50.c.run("./nametree").stdout("Blanchard\nBriga\nJay\nKara\nMartin\nMichael\nRyan\n").exit(0)

@check50.check(runs)
def runs3():
    """nametree.c finds a name correctly and has the correct functions and headers"""
    check50.include('test_time.c',"names.csv")
    with open("names.csv", "w") as f:
        f.write("Michael\nJay\nRyan\nBriga\nMartin\nKara\nBlanchard\n")
    with open('nametree.c') as f:
        data = f.read()

    data = data.replace("int main(void)","void other()")
    with open('nametree.c','w') as f:
        f.write(data)

    check50.run("clang -c nametree.c").stdout() #.exit(0)
    check50.c.compile("test_time.c", lcs50=True)
    check50.c.run("./test_time").stdin("Martin").stdout("Found Martin\n").exit(0)

@check50.check(runs3)
def runs4():
    """nametree.c does not find a missing name"""
    check50.include('test_time.c',"names.csv")
    with open("names.csv", "w") as f:
        f.write("Michael\nJay\nRyan\nBriga\nMartin\nKara\nBlanchard\n")
    with open('nametree.c') as f:
        data = f.read()

    data = data.replace("int main(void)","void other()")
    with open('nametree.c','w') as f:
        f.write(data)

    check50.run("clang -c nametree.c").stdout() #.exit(0)
    check50.c.compile("test_time.c", lcs50=True)
    check50.c.run("./test_time").stdin("Morticia").stdout("Did not find Morticia\n").exit(0)