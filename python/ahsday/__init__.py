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
    if len(out) < 10 or 'error' in out.lower():
        raise check50.Failure("Make sure your program has no erorrs and that it includes some client code that creates a Day, and AHSDay, and prints them out")

