import check50

@check50.check()
def exists():
    """ Check that stocktax.py exists """
    check50.exists("stocktax.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors and greets the user correctly"""
    output = check50.run("python stocktax.py").stdin("single").stdin("100000").stdout()
    check50.log(output)

