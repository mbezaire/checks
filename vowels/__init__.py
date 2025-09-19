import check50
import check50.c
import random

@check50.check()
def exists():
    """vowels.c exists"""
    check50.exists("vowels.c")


@check50.check(exists)
def compiles():
    """vowels.c compiles"""
    check50.c.compile("vowels.c", lcs50=True)


@check50.check(compiles)
def test_valid_tri():
    """The vowels program counts vowels accurately"""

    worddata = random.choice([['recursion', 4], ['coding', 2], ['education', 5],['instrument', 3]])

    check50.run("./vowels" + worddata[0]).stdout(str(worddata[1]) + '\n').exit(0)


@check50.check(test_valid_tri)
def noloops():
    """The vowels program doesn't use any loops"""

    with open('vowels.c') as f:
        contents = f.read()

    if 'for' in contents or 'while' in contents:
        raise check50.Failure("Uh oh, you may have referred to a loop somewhere in your code!")