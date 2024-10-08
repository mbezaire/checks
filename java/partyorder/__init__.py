# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import re
import check50
import check50.c

classname = 'PartyOrder'

@check50.check()
def exists():
    """Program file exists"""
    check50.exists(f"{classname}.java")

@check50.check(exists)
def compiles():
    """Program compiles"""
    out = check50.run(f"javac -d ./ {classname}.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
            

@check50.check(compiles)
def runs():
    """Program should provide 14 cupcakes for 2 parties"""
    check50.include("CupCakeRestaurant.java")
    out = check50.run("javac -d ./ CupCakeRestaurant.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to run due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to run", help=finderror)
    check50.log("Fabulous Person 1 called in an order for 6 people for their party...")
    check50.log("Fun Family called in an order for 6 people for their birthday party...")
    check50.log("Fabulous Person 1 called back ... now 8 people are attending their party...")

    check50.run(f"java CupCakeRestaurant").stdin("6", prompt = False).stdin("6", prompt = False).stdin("8", prompt = False).stdout("2 orders with 14 cupcakes", timeout = 60)

@check50.check(runs)
def runs60():
    """Program should provide 28 cupcakes for 2 other parties"""
    check50.include("CupCakeRestaurant.java")
    check50.run(f"java CupCakeRestaurant").stdin("6", prompt = False).stdin("6", prompt = False).stdin("22", prompt = False).stdout("2 orders with 28 cupcakes", timeout = 60)
