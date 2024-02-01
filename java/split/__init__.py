# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c


@check50.check()
def exists():
    """Split.java exists"""
    check50.exists("Split.java")

@check50.check(exists)
def compiles():
    """Split.java compiles"""
    out = check50.run("javac -d ./ Split.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

@check50.check(compiles)
def runs():
    """Split.java prints out an array of Strings"""
    check50.run("java Split").stdout('["one", "two", "three", "four"]',timeout = 5);


@check50.check(compiles)
def runs40():
    """Find.java uses a your custom split method"""
    with open("Split.java") as f:
        content = f.read()
    content = content.replace(" ","").replace("\n","").replace("\t","")
    if "=split(" not in content:
        raise check50.Failure("Looks like you used the regular String split method instead of your own")
    if "publicstaticString[]split(Stringwhole,chardelimiter){}" in content:
        raise check50.Failure("Looks like you forgot to write your own split method")

