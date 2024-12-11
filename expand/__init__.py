import check50
import check50.c
import random

@check50.check()
def exists():
    """expand.c exists"""
    check50.exists("expand.c")

@check50.check(exists)
def compiles():
    """expand compiles"""
    check50.c.compile("expand.c") #, lcs50=True)

@check50.check(compiles)
def catout():
    """expands array.txt 2x in each direction"""
    
    linewidth = random.randint(2,4)*3 - 4
    numlines = random.randint(3,5)
    expw = (0 if ((linewidth*2)%3) == 0  else 3 - (linewidth*2) % 3) + (linewidth*2)
    data = []
    outdata = []
    with open("array.txt","w") as f:
        f.write(str(linewidth) + '\n')
        f.write(str(numlines) + '\n')
        for w in range(expw):
            rowdata = ''
            outrow = ''
            for h in range(numlines):
                thechar = chr(random.randint(65, 90))
                rowdata += thechar
                outrow += thechar*2
            rowdata += '\n'
            outrow += '\n'
            f.writelines(rowdata)
            data.append(rowdata)
            outdata.append(outrow)
            outdata.append(outrow)


    check50.include("array.txt")
    check50.run("./expand").stdout(outmeh).exit(0)
    with open("array2x.txt") as f:
        outmeh = f.readlines()
    
    if int(outmeh[0].strip()) != linewidth*2:
        raise check50.Mismatch(str(linewidth*2), outmeh[0].strip(), "New width must be double the old one")

    if int(outmeh[1].strip()) != numlines*2:
        raise check50.Mismatch(str(numlines*2), outmeh[1].strip(), "New height must be double the old one")

    if len(outmeh) - 2 != numlines*2:
        raise check50.Mismatch(f"A file with {numlines*2} lines of char data", "\n".join(outmeh))
    
    width = len(outmeh[2].replace("\n",""))
    if width != expw:
        raise check50.Mismatch(f"Each line of char data having {expw} chars including padding", f"Line has {width} chars: {outmeh[2].strip()}")
    
    for i, row in enumerate(outmeh[2:]):
        if len(row.strip()) != expw:
            raise check50.Mismatch(f"Each line of char data having {expw} chars including padding", f"But file contains this line: {row.strip()}")
        if row[:linewidth*2] != outdata[i].strip():
            raise check50.Mismatch(outdata[i].strip(), row[:linewidth*2], f"data row {i} did not match what is expected")
