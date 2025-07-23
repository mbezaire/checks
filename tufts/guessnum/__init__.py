import check50

@check50.check()
def exists():
    """ Check that guess_a_number.py exists """
    check50.exists("guess_a_number.py")

@check50.check(exists)
def run():
    """ Check that you are getting at least 2 inputs from the user. """
    check50.run('python guess_a_number.py').stdin("1").stdin("1").stdin("1").stdin("1").stdin("1").stdin("1").stdin("1").exit(0)

@check50.check(run)
def run2():
    """ Check that you are using random.randint"""
    with open('decision.py') as f:
        contents = f.read()

    if contents.count("random.randint(") < 1:
        raise check50.Failure('Expected you to call the randint method of random to set the number')

@check50.check(run2)
def run3():
    """ Check that you are using a loop to give the user up to 7 chances"""
    with open('decision.py') as f:
        contents = f.read()

    if (contents.count("for ") + contents.count("if ")) < 1:
        raise check50.Failure('Expected you to use a for or while loop')
