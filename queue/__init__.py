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
    """queue.c, queue.h and testqueue.c exist"""
    check50.exists("testqueue.c")
    check50.exists("queue.c")
    check50.exists("queue.h")

@check50.check(exists)
def compiles():
    """queue contains enqueue and dequeue"""
    check50.include("slugqueue.c","queueup.c","queuedown.c")
    check50.run("clang -c queue.c").exit(0)
    outcode = check50.run("clang testqueue.c -lcs50 queue.o -o testqueue").exit()
    if outcode == 1:
        check50.log('Did you #include "queue.c" or "queue.h" in your testqueue.c?')
    check50.run("clang slugqueue.c -lcs50 queue.o -o slugqueue").exit(0)
    check50.run("clang queueup.c -lcs50 queue.o -o queueup").exit(0)
    check50.run("clang queuedown.c -lcs50 queue.o -o queuedown").exit(0)
    check50.run("./slugqueue").stdout("okay","okay\n").exit(0)

@check50.check(compiles)
def qup():
    """queues up 5,3,1,2 correctly"""
    check50.run("./queueup").stdout("front:0 size:4 in queue:5,3,1,2,").exit(0)

@check50.check(compiles)
def qdown():
    """queues up 1, 2, 3, 4, 5 and down 1, 2, and up 6, 7 and down 3 correctly"""
    check50.run("./queuedown").stdout("front:3 size:4 dequeued:1 2 3 in queue:4,5,6,7,").exit(0)


