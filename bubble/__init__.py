import check50
import check50.c
import random

@check50.check()
def exists():
    """bubblesort.c exists"""
    check50.exists("bubblesort.c")


@check50.check(exists)
def compiles():
    """bubblesort.c compiles"""
    check50.c.compile("bubblesort.c", lcs50=True)


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


    check50.run("./bubblesort" + mynums).stdout(corrnums).exit(0)