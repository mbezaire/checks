import check50
import check50.c
import re

SAMPLE_IMAGES = [

    # 0
    ["testing with sample 3x3 image",
    "first row: (255, 0, 0), (255, 0, 0), (255, 0, 0)",
    "second row: (0, 255, 0), (0, 255, 0), (0, 255, 0)",
    "third row: (0, 0, 255), (0, 0, 255), (0, 0, 255)"],

    # 1
    ["testing with sample 3x3 image",
    "first row: (10, 20, 30), (40, 50, 60), (70, 80, 90)",
    "second row: (110, 130, 140), (120, 140, 150), (130, 150, 160)",
    "third row: (200, 210, 220), (220, 230, 240), (240, 250, 255)"],

    # 2
    ["testing with sample 4x4 image",
    "first row: (10, 20, 30), (40, 50, 60), (70, 80, 90), (100, 110, 120)",
    "second row: (110, 130, 140), (120, 140, 150), (130, 150, 160), (140, 160, 170)",
    "third row: (195, 204, 213), (205, 214, 223), (225, 234, 243), (245, 254, 253)",
    "fourth row: (50, 28, 90), (0, 0, 0), (255, 255, 255), (85, 85, 85)"],

    # 3
    ["testing with sample 1x2 image",
    "first row: (255, 0, 0), (0, 0, 255)"],

    # 4
    ["testing with sample 1x3 image",
    "first row: (255, 0, 0), (0, 255, 0), (0, 0, 255)"]
]

def SAMPLE_PIXEL(r, g, b):
    return f"testing with pixel ({r}, {g}, {b})"

def log(lines):
    if isinstance(lines, list):
        for line in lines:
            check50.log(line)
    else:
        check50.log(lines)

@check50.check()
def exists():
    """helpers.c and helpers.h exist"""
    check50.exists("helpers.c")
    check50.include("Makefile", "bmp.h", "helpers.h", "testing.c")

@check50.check(exists)
def compiles():
    """filter compiles"""
    check50.run("make").exit(0)

@check50.check(compiles)
def grayscale4x4():
    """grayscale correctly filters 4x4 image"""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 0 5").stdout("".join([
        "20 20 20\n", "50 50 50\n", "80 80 80\n", "110 110 110\n",
        "127 127 127\n", "137 137 137\n", "147 147 147\n", "157 157 157\n",
        "204 204 204\n", "214 214 214\n", "234 234 234\n", "251 251 251\n",
        "56 56 56\n", "0 0 0\n", "255 255 255\n", "85 85 85\n"
    ]))

@check50.check(compiles)
def reflect4():
    """reflect correctly filters 4x4 image"""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 2 4").stdout("".join([
        "100 110 120\n", "70 80 90\n", "40 50 60\n", "10 20 30\n",
        "140 160 170\n", "130 150 160\n", "120 140 150\n", "110 130 140\n",
        "245 254 253\n", "225 234 243\n", "205 214 223\n", "195 204 213\n",
        "85 85 85\n", "255 255 255\n", "0 0 0\n", "50 28 90\n"
    ]))


@check50.check(compiles)
def blur4():
    """blur correctly filters 4x4 image"""
    log(SAMPLE_IMAGES[2])
    check50.run("./testing 3 4").stdout("".join([
        "70 85 95\n", "80 95 105\n", "100 115 125\n", "110 125 135\n",
        "113 126 136\n", "123 136 145\n", "142 155 163\n", "152 165 173\n",
        "113 119 136\n", "143 151 164\n", "156 166 171\n", "180 190 194\n",
        "113 112 132\n", "155 156 171\n", "169 174 177\n", "203 207 209\n"
    ]))


@check50.check(compiles)
def custom():
    """custom uniquely filters 4x4 image"""
    log(SAMPLE_IMAGES[2])
    out = check50.run("./testing 3 4").stdout()
    if out in ["".join([ # blur
        "70 85 95\n", "80 95 105\n", "100 115 125\n", "110 125 135\n",
        "113 126 136\n", "123 136 145\n", "142 155 163\n", "152 165 173\n",
        "113 119 136\n", "143 151 164\n", "156 166 171\n", "180 190 194\n",
        "113 112 132\n", "155 156 171\n", "169 174 177\n", "203 207 209\n"
    ]), "".join([ # grayscale
        "20 20 20\n", "50 50 50\n", "80 80 80\n", "110 110 110\n",
        "127 127 127\n", "137 137 137\n", "147 147 147\n", "157 157 157\n",
        "204 204 204\n", "214 214 214\n", "234 234 234\n", "251 251 251\n",
        "56 56 56\n", "0 0 0\n", "255 255 255\n", "85 85 85\n"
    ]), "".join([ # reflect
        "100 110 120\n", "70 80 90\n", "40 50 60\n", "10 20 30\n",
        "140 160 170\n", "130 150 160\n", "120 140 150\n", "110 130 140\n",
        "245 254 253\n", "225 234 243\n", "205 214 223\n", "195 204 213\n",
        "85 85 85\n", "255 255 255\n", "0 0 0\n", "50 28 90\n"
    ]), "".join([ # original
        "10 20 30\n", "40 50 60\n", "70 80 90\n", "100 110 120\n",
        "110 130 140\n", "120 140 150\n", "130 150 160\n", "140 160 170\n",
        "195 204 213\n", "205 214 223\n", "225 234 243\n", "245 254 253\n",
        "50 28 90\n", "0 0 0\n", "255 255 255\n", "85 85 85\n"
    ]), "".join([ # sepia
        "25 22 17\n", "66 58 45\n", "106 94 74\n",
        "170 151 118\n", "183 163 127\n", "197 175 136\n",
        "255 251 195\n", "255 255 214\n", "255 255 232\n"
    ]), "".join([ # edges
        "76 117 255\n", "213 228 255\n", "255 255 255\n", "255 255 255\n",
        "114 102 255\n", "210 150 60\n", "177 171 156\n", "250 247 255\n",
        "161 89 255\n", "126 128 181\n", "114 170 192\n", "247 220 192\n",
        "148 71 156\n", "133 100 121\n", "181 148 212\n", "212 170 255\n"
    ])]
               check50.Mismatch("Expected a unique image to be produced","Looks like one of the other algorithms",help="Make something custom!")
