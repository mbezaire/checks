# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c
import os
from PIL import Image
from PIL import ImageChops

@check50.check()
def exists():
    """enlarge.c exists"""
    check50.exists("enlarge.c")

@check50.check(exists)
def compiles():
    """enlarge.c compiles"""
    check50.include("bmp.h")
    check50.c.compile("enlarge.c", lcs50=True)


@check50.check(compiles)
def runs():
    """enlarge.c runs"""
    check50.include("small.bmp")
    out = check50.run("./enlarge small.bmp enlarged_small.bmp").stdout()
    check50.log(out)
    files = os.listdir()
    imgs = []
    for file in files:
        if file.endswith(".bmp") and file not in ['small.bmp',"correct2xsmall.bmp"]:
            imgs.append(file)
    if len(imgs) < 1:
        raise check50.Failure("Your program didn't produce a new image file to check")
    elif imgs[0] != "enlarged_small.bmp":
        with open("wrongname.txt","w") as f:
            f.write(imgs[0])
        out = check50.run(f'mv {imgs[0]} enlarged_small.bmp').stdout()
        check50.log(out)



@check50.check(runs)
def rightname():
    """enlarge.c names the new file correctly"""
    if os.path.exists("wrongname.txt"):
        with open("wrongname.txt","r") as f:
            imgname = f.read()
            raise check50.Mismatch("enlarged_small.bmp", imgname, help="Make sure you use the second command line argument to name your new file")

@check50.check(runs)
def rightsize():
    """enlarge.c enlarges the file size appropriately"""
    sz = os.stat("enlarged_small.bmp").st_size
    if sz != 174:
        raise check50.Mismatch('174',str(sz), help = "Your program produced a file of the wrong size. This could be due to incorrect image data, padding, or header. Try running xxd -g 3 on_your_enlarged.bmp to investigate")


@check50.check(runs)
def headercolors():
    """enlarge.c enlarges the image data"""
    check50.include("correct2xsmall.bmp")
    try:
        image_one = Image.open("correct2xsmall.bmp")
        image_two = Image.open("enlarged_small.bmp")
    except:
        raise check50.Failure("The header of your output file is incorrect - can't be read in as an image file")
    try:
        diff = ImageChops.difference(image_one, image_two)
    except:
        raise check50.Failure("Your output file might be missing some image data. It's not properly enlarged and we can't check it")

    check50.log('enlarged size: ' + str(diff.size))
    if diff.getbbox():
        raise check50.Mismatch(list(image_one.getdata()),list(image_two.getdata()),"The colors in the image are wrong")
