# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re
    - !require .java
    - !require .java
check50.include("FClient.java", "F0Client.java")

@check50.check()
def exists():
    """ClientSavingsAccount and SavingsAccount.java exist"""
    check50.exists("SavingsAccount.java")
    check50.exists("ClientSavingsAccount.java")

@check50.check(exists)
def compiles():
    """SavingsAccount.java and ClientSavingsAccount.java compile"""
    out = check50.run("javac -d ./ SavingsAccount.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
    out = check50.run("javac -d ./ ClientSavingsAccount.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)

#    check50.run("javac -d ./ FClient.java").stdout(timeout = 60)
#    check50.run("javac -d ./ F0Client.java").stdout(timeout = 60)



#@check50.check(compiles)
#def run1():
#    """addOdds works correctly"""
#    out5 = check50.run("java FClient").stdin("5", prompt = False).stdout()
#    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
#    out5 = out5.strip()
#    if out5 != "9":
#        raise check50.Failure("Given addOdds(5), expected 9, actual " + str(out5))
#    out5 = check50.run("java FClient").stdin("8", prompt = False).stdout()
#    out5 = out5.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
3    out5 = out5.strip()
#    if out5 != "16":
#        raise check50.Failure("Given addOdds(8), expected 16, actual " + str(out5))

#@check50.check(compiles)
#def run3():
#    """addUpTo() sums and prints correctly"""
#    out = check50.run("java F0Client").stdin("6", prompt = True, timeout = 60).stdout() #"0").exit(0)
#    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
#    out = out.strip()
#    if "1 + 2 + 3 + 4 + 5 + 6 = 21" not in out:
#        raise check50.Failure("expected 1 + 2 + 3 + 4 + 5 + 6 = 21, actual " + str(out))
#    out = check50.run("java F0Client").stdin("1", prompt = True).stdout() #"0").exit(0)
#    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
#    out = out.strip()
#    if out != "1 = 1":
#        raise check50.Failure("expected 1 = 1, actual " + str(out))
