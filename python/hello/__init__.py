import check50

@check50.check()
def exists():
    """ Check that hello.py exists """
    check50.exists("hello.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors and greets the user correctly"""
    check50.run("python hello.py").stdin("Mr. Govoni").stdout("[Hh]ello[,]{0,1} Mr. Govoni", "Hello, Mr. Govoni\n", timeout=30, regex=True).exit(0)

@check50.check(exists)
def run2():
    """ Program greets another correctly"""
    check50.run("python hello.py").stdin("there").stdout("[Hh]ello[,]{0,1} there", "Hello, there\n", timeout=30, regex=True).exit(0)
