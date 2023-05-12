import check50

@check50.check()
def exists():
    """ Check that pycal.py exists """
    check50.exists("pycal.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors and calculates day correctly"""
    check50.run("python pycal.py").stdin("2").stdout("Wednesday", "Wednesday\n", timeout=30).exit()
