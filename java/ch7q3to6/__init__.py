# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

check50.include("FClient.java", "F0Client.java", "F1Client.java", "F2Client.java", "F3Client.java", "F4Client.java", "F5Client.java")

@check50.check()
def exists():
    """Chapter7part1.java exists"""
    check50.exists("Chapter7part1.java")

@check50.check(exists)
def compiles():
    """Chapter7part1.java compiles"""
    check50.run("javac Chapter7part1.java")


@check50.check()
def dexists():
    """HelloNTimes.java exists"""
    check50.exists("HelloNTimes.java")

@check50.check(dexists)
def dcompiles():
    """HelloNTimes.java compiles"""
    check50.run("javac HelloNTimes.java")
