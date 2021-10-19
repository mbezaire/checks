import check50
import check50.c


@check50.check()
def exists():
    """compute_score.c exists"""
    check50.exists("compute_score.c")


@check50.check(exists)
def compiles():
    """compute_score.c compiles"""
    check50.c.compile("compute_score.c", lcs50=True)


@check50.check(compiles)
def super_achiever():
    """Super achiever caps at 50 """
    check50.run("./compute_score").stdin("50").stdin("65").stdout("50\n", "50\n").exit(0)

@check50.check(compiles)
def checked_out():
    """Checked out student keeps same score"""
    check50.run("./compute_score").stdin("41").stdin("0").stdout("41\n", "41\n").exit(0)


@check50.check(compiles)
def student():
    """Other student gets some buffer points"""
    check50.run("./compute_score").stdin("42").stdin("48").stdout("46\n", "46\n").exit(0)
