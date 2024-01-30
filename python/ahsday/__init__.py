import check50

@check50.check()
def exists():
    """ Check that days.py exists """
    check50.exists("days.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors and prints some days"""
    check50.include("data.csv")
    out = check50.run("python days.py").stdout(timeout=30)
    check50.log(out)
    if len(out) < 10:
        raise check50.Failure("Make sure your program has some client code that creates a Day, and AHSDay, and prints them out")

