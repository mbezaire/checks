import check50

@check50.check()
def exists():
    """ Check that trivia.py exists """
    check50.exists("trivia.py")

@check50.check(exists)
def run():
    """ File presents the question and answers correctly"""
    out = check50.run("python trivia.py").stdout(timeout=40).stdin("4").stdout(timeout=30)
    check50.log(out)