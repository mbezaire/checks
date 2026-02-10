import check50

@check50.check()
def exists():
    """ Check that stocktax.py and stock.py exist """
    check50.exists("stocktax.py")
    check50.exists("stock.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors and greets the user correctly"""
    output = check50.run("python stocktax.py").stdin("single").stdin("100000").stdout()
    check50.log(output)

@check50.check(run)
def stock():
    """ The stock class works alright"""
    output = check50.run("python makestock.py").stdout()
    check50.log(output)
