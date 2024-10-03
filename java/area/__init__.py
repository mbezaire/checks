# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re
import random
import math

classname = 'ShapeArea'

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
    """Program runs and prints out 4 different areas for 4 different shape types"""
    inputflag = True
    radius = random.randrange(5,20)
    width = random.randrange(17,27)
    length = random.randrange(3,11)
    side1 = random.randrange(5,12)
    side2 = random.randrange(3, 8)
    side3 = random.randrange(max(1,max(side2,side1) - min(side2,side1)), side2 + side1)
    out = check50.run("java ShapeArea 2>&1").stdin(str(radius)).stdin(f"{length} {width}").stdin(f"{side1} {side2} {side3}").stdout(timeout = 30)
    if len(out) == 0:
        out2 = check50.run("java ShapeArea 2>&1").stdout(timeout = 30)
        inputflag = False
        check50.log(out)
        check50.log(out2)
        if len(out2) > 0:
            raise check50.Failure("There was an issue with your code.", help="Check that you are scanning in a radius, 2 rectangle sides, and 3 triangle sides")
        else:
            raise check50.Failure("There was an issue with your code.", help="Check that you are printing out the areas of the 4 shapes")
    findtemp = re.findall(r'([0-9]+.[0-9]+)', out)  # replace search with findall to find last
    if findtemp == None or len(findtemp) == 0:
        raise check50.Failure("Failed to find a decimal number in your printed output: " + out, help="Make sure to print out circle and sphere areas as doubles")
    result = re.findall(r'([0-9\.]+)', out)  # replace search with findall to find last
    if len(result) < 4:
        raise check50.Failure("Failed to find 4 separate numbers " + out, help="Make sure to print out all four area results")

    circArea = math.pi*radius*radius
    sphereArea = 4*circArea
    rectArea = length*width
    s = (side1 + side2 + side3)/2.0
    triArea = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    areas = [circArea, sphereArea, rectArea, triArea]
    for area in areas:
        found = False
        for res in result:
            if abs(float(res) - area) <= 0.0001:
                found = True
                result.remove(res)
                break
        if not found:
            raise check50.Mismatch(f"Circle Area: {circArea}\nSphere Area: {sphereArea}\nRectangle Area: {rectArea}\nTriangle Area: {triArea}", out, help="Check your calculations and make sure to print out all four area results")

@check50.check(runs)
def runs2():
    """Methods are good"""
    check50.include("Client.java")
    out = check50.run(f"javac -d ./ Client.java 2>&1").stdout(timeout = 60)
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
    out = check50.run('java Client').stdout(timeout = 20)
    if out.strip() == '16.707963267948966':
        raise check50.Mismatch('17.140975969841186', out.strip(), help='Did you use integer division accidentally somewhere?')
    elif out.strip() != '17.140975969841186':
        raise check50.Mismatch('17.140975969841186', out.strip(), help='Check your math for your formulae')

