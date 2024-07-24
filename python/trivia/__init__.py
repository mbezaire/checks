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

@check50.check(run2)
def run3():
    """ No spaces between the number and the dot in the menu of choices. """
    with open("trivia.py") as f:
        contents = f.read().replace(" ","").replace("\"","").replace("\'","").replace(".","#")

    if ",#+country" in contents:
        raise check50.Mismatch("1. Country","1 . Country",help="expected a period right after the number for each country")


@check50.check(run3)
def run4():
    """ Question and menu of choices look correct. """
    with open("trivia.py") as f:
        contents = f.read().replace(" ","").replace("\"","").replace("\'","").replace(".","#")

    if "Inwhichcountryisitillegaltoownjustoneguineapig?" not in contents:
        raise check50.Failure('Expected the question to be exactly: "In which country is it illegal to own just one guinea pig?"')


    if "i+1" not in contents and "1+i" not in contents:
        raise check50.Failure('Expected the menu choices to run from 1 to 4')
