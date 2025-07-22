import check50

@check50.check()
def exists():
    """ Check that decision.py exists """
    check50.exists("decision.py")

@check50.check(exists)
def run():
    """ Check that you are getting at least 2 inputs from the user. """
    with open('decision.py') as f:
        contents = f.read()

    if contents.count("input(") < 2:
        raise check50.Failure('Expected you to ask the user for at least 2 pieces of info using the input() function but only found ' + str(contents.count("input(")))


@check50.check(run)
def run2():
    """ Check that you are asking at least two logic questions (if conditions) in your code """
    with open('decision.py') as f:
        contents = f.read()

    if contents.count("if ") < 2 or contents.count("else:") < 1:
        raise check50.Failure('Expected you to have at least a few if statements and at least one else somewhere')

@check50.check(run2)
def run3():
    """ Check that you are printing at least a few statements for the user"""
    with open('decision.py') as f:
        contents = f.read()

    if contents.count("print(") < 4:
        raise check50.Failure('Expected you to have at least 4 print statements for the user but only found ' + str(contents.count("print(")))
