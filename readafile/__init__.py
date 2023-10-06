import check50
import check50.c

@check50.check()
def exists():
    """readafile.c exists"""
    check50.exists("readafile.c")

@check50.check(exists)
def compiles():
    """readafile.c compiles"""
    check50.c.compile("readafile.c", lcs50=True)

@check50.check(compiles)
def single_sentence():
    """handles a file of a single sentence with multiple words"""
    check50.include("one_sentence.txt")
    check50.run("./readafile one_sentence.txt").stdout("Grade 7\n").stdout(check50.EOF).exit(0)

@check50.check(compiles)
def single_sentence_other():
    """handles incorrect usage"""
    check50.run("./readafile").stdout("Usage: ./readafile filename\n").exit(1)

@check50.check(compiles)
def single_sentence_other_punctuation():
    """handles a file that doesn't exist"""
    check50.run("./readafile notafile.txt").stdout("File notafile.txt not found\n").exit(1)

@check50.check(compiles)
def single_sentence_complex():
    """handles a file with multiple paragraphs"""
    check50.include("essay.txt")
    check50.run("./readafile essay.txt").stdout("Grade 8\n").stdout(check50.EOF).exit(0)
