import check50
import check50.py

@check50.check()
def exists():
    """ Check that hello.py exists """
    check50.exists("hello.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors"""
    check50.py.compile("hello.py")

@check50.check(run)
def greet():
    """ File prints greeting """

    out = check50.run("python hello.py").stdout(timeout = 50)
    if "hello" not in out.lower():
        raise check50.Failure("Could not find the word 'hello' in your greeting")
        
@check50.check(greet)
def greet2():
    """ File prints Hello World """

    out = check50.run("python hello.py").stdout(timeout = 50)
    if "Hello World" != out.strip():
        raise check50.Mismatch("Hello World", out.strip())


@check50.check(greet2)
def greet3():
    """ Some other check """
    if False:
        raise check50.Failure("This check should never fail once it runs")
