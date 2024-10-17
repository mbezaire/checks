import check50
import check50.c

@check50.check()
def exists():
    """cp.c and cat.c exist"""
    check50.exists("cp.c").exists("cat.c")

@check50.check(exists)
def compiles():
    """cat.c and cp.c compile"""
    check50.c.compile("cat.c", lcs50=True)
    check50.c.compile("cp.c", lcs50=True)

@check50.check(compiles)
def catout():
    """cat.c prints file contents to the terminal"""
    check50.include("meh.txt")
    check50.include("psa.txt")
    with open("meh.txt") as f:
        outmeh = f.read()
    with open("meh.txt") as f:
        outpsa = f.read()
    check50.run("./cat meh.txt").stdout(outmeh + "\n").exit(0)
    check50.run("./cat psa.txt").stdout(outpsa + "\n").exit(0)

@check50.check(compiles)
def cprun():
    """cp.c prints file contents to another file"""
    check50.run("./cp meh.txt yummy.txt").stdout()
    check50.include("yummy.txt")
    with open("meh.txt") as f:
        oldtext = f.read()
    with open("yummy.txt") as f:
        newtext = f.read()
    if oldtext.strip() != newtext.strip():
        raise check50.Mismatch(oldtext, newtext, help="Expected the new file to contain the same contents as the old file")