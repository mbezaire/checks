# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re
import random
import math

classname = ['Teenager', 'Adult','Person']

@check50.check()
def exists():
    """Program file exists"""
    for cls in classname:
        check50.exists(f"{cls}.java")

@check50.check(exists)
def compiles():
    """Program compiles"""
    out = check50.run(f"javac -d ./ *.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            
@check50.check(compiles)
def runs():
    """Program runs and prints expected output"""
    teenstring = "What's up?\nPete, What's up?\nPete\nAge: 18\nAndover High School\nGrade: 12"
    adultstring = "Hello, how are you?\nHello Pete how are you?\nPete\nAge: 39\ndoorman\nMarried: true"

    teenout = check50.run("java Teenager 2>&1").stdout(timeout = 30)
    adultout = check50.run("java Adult 2>&1").stdout(timeout = 30)
    if teenstring != teenout.strip():
        raise check50.Mismatch(teenstring, teenout)
    if adultstring != adultout.strip():
        raise check50.Mismatch(adultstring, adultout)

            
@check50.check(runs)
def dry():
    """No repetition"""
    with open("Teenager.java") as f:
        teencode = f.read()

    with open("Adult.java") as f:
        adultcode = f.read()
    
    allcode = teencode + '\n' + adultcode

    checks = ['public void setAge', 'public void setName', 'private String name', 'private int age']

    for chk in checks:
        if chk in allcode:
            raise check50.Failure("Uh oh, it looks like you still have redundant code in Teenager or Adult")
        
    with open("Person.java") as f:
        personcode = f.read()

    for chk in checks:
        if chk not in personcode:
            raise check50.Failure("Uh oh, it looks like your Person code is not complete yet")
