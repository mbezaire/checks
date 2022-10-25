# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

# check50.include("testmylib.c") #, "testmylibvowel.c", "testmylibconsonant.c" ])

@check50.check()
def exists():
    """mylib.c and mylib.h exist"""
    check50.exists("mylib.c")
    check50.exists("mylib.h")

@check50.check(exists)
def mylib():
    """mylib contains selectionsort and bubblesort"""
    check50.include("testmylib.c","testselection.c", "testbubble.c")
    check50.run("clang -c mylib.c").exit(0)
    check50.run("clang testmylib.c -lcs50 mylib.o -o testmylib").exit(0)
    check50.run("clang testselection.c -lcs50 mylib.o -o testselection").exit(0)
    check50.run("clang testbubble.c -lcs50 mylib.o -o testbubble").exit(0)
    check50.run("./testmylib").stdin("u").stdout("okay","okay\n").exit(0)

@check50.check(mylib)
def selsort():
    """selectionsort sorts 9,4,7,3,1 into 1,3,4,7,9"""
    check50.run("./testselection").stdout("1,3,4,7,9,").exit(0)

@check50.check(mylib)
def bubsort():
    """bubblesort sorts 3,1,8,4,7,3,1 into 1,1,3,3,4,7,8"""
    check50.run("./testbubble").stdout("1,1,3,3,4,7,8,").exit(0)


@check50.check(exists)
def mylib2():
    """mylib contains linsearch and binsearch and a decimal struct datatype"""
    check50.include("testmylibsearch.c","testlin.c", "testbin.c")
    check50.run("clang -c mylib.c").exit(0)
    check50.run("clang testmylibsearch.c -lcs50 mylib.o -o testmylibsearch").exit(0)
    check50.run("clang testlin.c -lcs50 mylib.o -o testlin").exit(0)
    check50.run("clang testbin.c -lcs50 mylib.o -o testbin").exit(0)
    check50.run("./testmylibsearch").stdin("u").stdout("okay","okay\n").exit(0)

@check50.check(mylib2)
def linsearch():
    """linear search finds 5 in 5, 1, 2, 3, 4"""
    check50.run("./testlin").stdin("5").stdout("true").exit(0)

@check50.check(mylib2)
def linsearch2():
    """linear search does not find 0 in 5, 1, 2, 3, 4"""
    check50.run("./testlin").stdin("0").stdout("false").exit(0)


@check50.check(mylib2)
def binsearch():
    """binary search finds 8 in 12, 4, 6, 8, 10"""
    check50.run("./testbin").stdin("8").stdout("true").exit(0)

@check50.check(mylib2)
def binsearch2():
    """binary search does not find 12 in 12, 4, 6, 8, 10"""
    check50.run("./testbin").stdin("12").stdout("false").exit(0)


@check50.check(mylib2)
def binsearch3():
    """binary search does not find 7 in 12, 4, 6, 8, 10"""
    check50.run("./testbin").stdin("7").stdout("false").exit(0)
