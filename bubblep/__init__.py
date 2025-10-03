import check50
import check50.c
import random
import re

@check50.check()
def exists():
    """bubblep.c exists"""
    check50.exists("bubblep.c")


@check50.check(exists)
def compiles():
    """bubblep.c compiles"""
    check50.c.compile("bubblep.c", lcs50=True)


@check50.check(compiles)
def test_valid_tri():
    """Bubble sorter sorts alright"""
    mynums = ""
    nums = []
    length = random.randint(3,7)
    for _ in range(length):
        val = random.randint(10,500)
        mynums += " " + str(val)
        nums.append(val)

    nums.sort()

    corrnums = ""
    for num in nums:
        corrnums += str(num) + "\n"


    check50.run("./bubblep" + mynums).stdout(corrnums).exit(0)



@check50.check(compiles)
def nosquares():
    """Bubble sorter using pointers, not square brackets"""
    with open("bubblep.c") as f:
        contents = f.read()


    cs50bool = contents.find("<cs50.h>")

    squares = contents.count("[")

    if cs50bool:
        squares += 1

    if squares > 2:
        patt = re.compile(r"([a-zA-Z]*\s*[a-zA-Z]+\[.*?\]\s*[a-zA-Z]*)")
        matches = re.findall(patt, contents)
        msg = "Too many square brackets in your program" + (" considering you're using the cs50 library" if cs50bool else "") + "!"
        for m in matches:
            msg += "\n" + m
        raise check50.Failure(msg)

