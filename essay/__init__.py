import check50
import check50.c

@check50.check()
def exists():
    """essaymetrics.c exists"""
    check50.exists("essaymetrics.c")

@check50.check(exists)
def compiles():
    """essaymetrics.c compiles"""
    check50.c.compile("essaymetrics.c", lcs50=True)

@check50.check(compiles)
def single_sentence_complex():
    """prints out useful metrics on essay.txt"""
    check50.include("essay.txt")
    out = check50.run("./essaymetrics essay.txt").stdout()
    check50.log(out)
    if len(out) < 20 or "Dvorak" not in out:
        raise check50.Failure("It seems that your metrics report is lacking...", help="Make sure to print out the readability, all the metrics from readability, any repeated words, and the number of times the word Dvorak appears in the essay")
