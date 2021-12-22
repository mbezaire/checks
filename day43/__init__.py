# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """an array implementation of stacks was submitted"""
    check50.exists("astack.c")

@check50.check()
def exists1():
    """an array implementation of queues was submitted"""
    check50.exists("aqueue.c")

@check50.check()
def exists2():
    """a linked list implementation of stacks was submitted"""
    check50.exists("llstack.c")

@check50.check()
def exists3():
    """a linked list implementation of queues was submitted"""
    check50.exists("llqueue.c")
    
@check50.check(exists)
def compiles():
    """astack.c compiles"""
    check50.c.compile("astack.c", lcs50=True)
    
@check50.check(exists1)
def compiles1():
    """aqueue.c compiles"""
    check50.c.compile("aqueue.c", lcs50=True)
    
@check50.check(exists2)
def compiles2():
    """llstack.c compiles"""
    check50.c.compile("llstack.c", lcs50=True)
    
@check50.check(exists3)
def compiles3():
    """llqueue.c compiles"""
    check50.c.compile("llqueue.c", lcs50=True)
