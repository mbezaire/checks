import check50

@check50.check()
def exists():
    """ Check that trivia.py exists """
    check50.exists("trivia.py")

@check50.check(exists)
def run():
    """ File presents the question and answers correctly"""
    out = check50.run("python trivia.py").stdout("In which country is it illegal to own just one guinea pig?", timeout=30, regex=True).stdout().stdin("4").stdout()
    check50.log(out)