import check50

@check50.check()
def exists():
    """ Check that trivia.py exists """
    check50.exists("trivia.py")

@check50.check(exists)
def run():
    """ The correct answer gets congratulated. """
    check50.run("python trivia.py").stdin("4", prompt = True).stdout("Congrats, you got it!", timeout=30).exit(0)

@check50.check(exists)
def run2():
    """ The incorrect answer gets an apology. """
    for r in range(1,4):
        check50.run("python trivia.py").stdin(str(r), prompt = True).stdout("Sorry, wrong answer!", timeout=30).exit(0)

# @check50.check(run2)
# def run3():
#     """ No spaces between the number and the dot in the menu of choices. """
#     for r in range(1,4):
#         check50.run("python trivia.py").stdin(str(r), prompt = True).stdout("Sorry, wrong answer!", timeout=30).exit(0)

