import check50

import check50
import check50.c


@check50.check()
def exists():
    """is_valid_tri.c exists"""
    check50.exists("is_valid_tri.c")


@check50.check(exists)
def compiles():
    """is_valid_tri.c compiles"""
    check50.c.compile("is_valid_tri.c", lcs50=True)


@check50.check(compiles)
def test_valid_tri():
    """Valid triangle yields true"""
    check50.run("./is_valid_tri").stdin("4","2","1").stdout("true\n", "true\n").exit(0)

@check50.check(compiles)
def test_invalid_tri():
    """Invalid triangle yields false"""
    check50.run("./is_valid_tri").stdin("4","2","7").stdout("false\n", "false\n").exit(0)
