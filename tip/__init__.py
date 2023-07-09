import check50
import check50.py

@check50.check()
def exists():
    """ Check that tip.py exists """
    check50.exists("tip.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors"""
    check50.py.compile("tip.py")



@check50.check(run)
def importlater():
    """ No import statements allowed in this program """

    # Read in the file
    with open('tip.py', 'r') as file:
        filedata = file.read()

    import_pos = filedata.count("import")

    if import_pos > 0:
        raise check50.Failure("Your program imports packages when it should not",\
                              help="Remove any import statements and resubmit")

@check50.check(importlater)
def tip1():
    """ The total is computed correctly """
    check50.run("python tip.py").stdin("100").stdin("15").stdout("Leave $115.00")

@check50.check(importlater)
def tip2():
    """ The total is computed correctly for a different cost and tip """
    check50.run("python tip.py").stdin("35").stdin("18").stdout("Leave $41.30")


@check50.check(importlater)
def tip3():
    """ The sum is computed correctly for a different cost and cheapskate """
    check50.run("python tip.py").stdin("47").stdin("0").stdout("Leave $47.00")