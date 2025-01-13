# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c
import re

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
        contents= re.sub(r"\/\*.*?(?=\*\/|\Z)\*/","",contents)

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
    out = check50.run("javac -d ./ ParsonLoop.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

@check50.check(compiles)
def runs():
    """Program prints out the expected output"""
    check50.run("java ParsonLoop").stdout("J L N P R T V \nI K M O Q S U \nH J L N P R T \nG I K M O Q S \nF H J L N P R \nE G I K M O Q \nD F H J L N P \nC E G I K M O \nB D F H J L N \nA C E G I K M ").exit(0)

