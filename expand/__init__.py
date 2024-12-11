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
    """Program runs"""
    
    linewidth = random.randint(2,4)*3 - 4
    numlines = random.randint(3,5)
    expw = (0 if ((linewidth*2)%3) == 0  else 3 - (linewidth*2) % 3) + (linewidth*2)
    data = []
    outdata = []

    with open("array.txt","w") as f:
        f.write(str(linewidth) + '\n')
        f.write(str(numlines) + '\n')
        for w in range(numlines):
            rowdata = ''
            outrow = ''
            for h in range(linewidth):
                thechar = chr(random.randint(65, 90))
                rowdata += thechar
                outrow += thechar*2
            for h in range(expw - linewidth):
                rowdata += 'a'
                outrow += 'aa'
            rowdata += '\n'
            outrow += '\n'
            f.writelines(rowdata)
            data.append(rowdata)
            outdata.append(outrow)
            outdata.append(outrow)

    with open("array.txt","r") as f:
        arr = f.read()

    expd = f"{linewidth*2}\n{numlines*2}\n{''.join(outdata)}"


    #check50.include("array.txt")
    check50.run("./expand").exit(0)
    check50.log(check50.run("ls -l").stdout())
    with open("array2x.txt") as f:
        outmeh = f.readlines()

    return outmeh, linewidth, numlines, expw, outdata, arr, expd

@check50.check(catout)
def check1(instuff):
    """ New width is double the old one """
    # expands array.txt 2x in each direction
    outmeh = instuff[0]
    linewidth = instuff[1]
    numlines = instuff[2]
    expw = instuff[3]
    outdata = instuff[4]
    arr = instuff[5]
    expd = instuff[6]
    if int(outmeh[0].strip()) != linewidth*2:
        raise check50.Mismatch(str(linewidth*2), outmeh[0].strip(), "New width must be double the old one")
    return outmeh, linewidth, numlines, expw, outdata, arr, expd

@check50.check(check1)
def check2(instuff):
    """ New height is double the old one """
    outmeh = instuff[0]
    linewidth = instuff[1]
    numlines = instuff[2]
    expw = instuff[3]
    outdata = instuff[4]
    arr = instuff[5]
    expd = instuff[6]
    if int(outmeh[1].strip()) != numlines*2:
        raise check50.Mismatch(str(numlines*2), outmeh[1].strip(), "New height must be double the old one")

    return outmeh, linewidth, numlines, expw, outdata, arr, expd

@check50.check(check2)
def check3(instuff):
    """ Actual rows of data is double the original """
    outmeh = instuff[0]
    linewidth = instuff[1]
    numlines = instuff[2]
    expw = instuff[3]
    outdata = instuff[4]
    arr = instuff[5]
    expd = instuff[6]
    check50.log(str(len(outmeh)))
    check50.log("array.txt was:")

    arrlines = arr.split("\n")
    for line in arrlines:
        check50.log(line)
    if len(outmeh) - 2 != numlines*2:
        raise check50.Mismatch(expd, "\n".join(outmeh))
    
    return outmeh, linewidth, numlines, expw, outdata, arr, expd

@check50.check(check3)
def check4(instuff):
    """ Actual width of data is double the original + necessary padding"""
    outmeh = instuff[0]
    linewidth = instuff[1]
    numlines = instuff[2]
    expw = instuff[3]
    outdata = instuff[4]
    arr = instuff[5]
    expd = instuff[6]
    width = len(outmeh[2].replace("\n",""))
    if width != expw:
        raise check50.Mismatch(f"Each line of char data having {expw} chars including padding", f"Line has {width} chars: {outmeh[2].strip()}")
    return outmeh, linewidth, numlines, expw, outdata, arr, expd

@check50.check(check4)
def check5(instuff):
    """ Actual data is doubled in horizontal and vertical directions"""
    outmeh = instuff[0]
    linewidth = instuff[1]
    numlines = instuff[2]
    expw = instuff[3]
    outdata = instuff[4]
    arr = instuff[5]
    expd = instuff[6]
    for i, row in enumerate(outmeh[2:]):
        if len(row.strip()) != expw:
            raise check50.Mismatch(f"Each line of char data having {expw} chars including padding", f"But file contains this line: {row.strip()}")
        if row[:linewidth*2] != outdata[i].strip()[:linewidth*2]:
            raise check50.Mismatch(outdata[i].strip()[:linewidth*2], row[:linewidth*2], f"data row {i} did not match what is expected (padding not shown here)")
