# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """Book.java, Author.java, and BClient.java exist"""
    check50.exists("Book.java")
    check50.exists("Author.java")
    check50.exists("BClient.java")
    
@check50.check(exists)
def compiles():
    """Everything compiles"""
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
    """BClient.java runs and prints out info for 3 books that got added to bookstore"""
    out = check50.run("java BClient.java").stdout(timeout = 60)
    if len(out) < 50 or out.count("$") < 3 or (out.lower().count("by") + out.lower().count("thor")) < 3:
        raise check50.Failure("Your BClient needs to print detailed info for 3 separate books.", help="Your BClient only prints:\n" + out)