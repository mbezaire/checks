# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import re
import random
import os

@check50.check()
def exists():
    """Your Client.java and 3 class files, image file, and README exist"""
    check50.exists("Client.java")
    check50.exists("README.md")
    with open("README.md") as f:
        text = f.read()

    if len(text) < 80:
        raise check50.Failure("Add more content to your README.", help="Include a top-level header, a few sentences about your project, and an image of your UML diagram.")
    elif '#' not in text:
        raise check50.Failure("Include a header in your README.", help="Use a # symbol, then a space, then your heading")
    elif text.replace(" ","").count('![') < 1:
        raise check50.Failure("Make sure to include the UML image in your README.")

    files = os.listdir()
    flag = False
    java_files = []
    for file in files:
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            flag = True
        elif file.endswith(".java"):
            java_files.append(file)

    if len(java_files) < 3:
        raise check50.Failure("Make sure to include at least 3 Java files. So far you have: " + ", ".join(java_files))
    elif not flag:
        raise check50.Failure("Make sure to generate a UML diagram at https://yuml.me and save it as an image (png, jpg, or jpeg) in your custom class folder")
    return java_files

@check50.check(exists)
def compiles(java_files):
    """All java files compile"""
    out = check50.run("javac -d ./ *.java").stdout(timeout = 60)
    out = out.replace("Picked up JAVA_TOOL_OPTIONS: -Dsun.java2d.opengl=true","")
    if "error" in out:
        finderror = re.search(r'([\s\S]+)?(?=([0-9]+ error[s]{0,1}))', out.replace("Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output",""))
        if finderror != None:
            result = finderror.groups()
            raise check50.Failure("Failed to compile due to " + result[1], help=result[0].strip())
        else:
            raise check50.Failure("Failed to compile", help=finderror)
    return java_files

@check50.check(compiles)
def relations(java_files):
    """Checking for HAS A and IS A relations"""
    hasa = False
    isa = False
    extends = False
    helptext = ''

    for file in java_files:
        with open(file) as f:
            text = f.read()
            st = text.find("public class")
            if st == -1: st = text.find("public  class")
            text = text[st:]

        if "extends" in text and ("//" not in text or text.find("extends") < text.find("//")):
            extends = True
            st = text.find("extends") + 7
            en = min(min(min(text.find("{", st+1),text.find("//", st+1)),text.find("/*", st+1)),text.find(" ", st+1))
            check50.log(f'{st} to {en}')
            myclass = text[st : en].strip()
            if myclass + ".java" in java_files and (not isa or len(helptext) > 0):
                isa = True
            else:
                helptext += "We found an extends statement in your file " + file + " but the class it extends was " + myclass + " and you didn't upload anything by that name.\n"

        for cl in java_files:
            if cl[:-5] in text[text.find("{"):]:
                hasa = True
    
    if extends == False:
        helptext += "We didn't find an extends statement in any of your files. You need at least one.\n"
    
    if hasa == False:
        helptext += "We didn't find a field in any of your classes that represents an object of one of your other classes. You need at least one.\n" 

    if not isa or not hasa:
        raise check50.Failure("You need both a HAS A and an IS A relationship among your 3 classes", help=helptext)


@check50.check(relations)
def runs(java_files):
    """Checking that your Client runs alright and prints out some content"""
    out = check50.run("javac Client.java").stdout(timeout = 60)
    if len(out) < 10:
        raise check50.Failure("Your code only printd: " + out, help="Expected more output from your Client class")

