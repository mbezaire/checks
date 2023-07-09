import check50
import check50.py
import builtins
import re

@check50.check()
def exists():
    """ Check that calc.py exists """
    check50.exists("calc.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors"""
    out = check50.run("pwd").stdout()
    check50.log(out)
    out = check50.run("ls").stdout()
    check50.log(out)
    check50.include("calc.py")
    out = check50.run("ls").stdout()
    check50.log(out)
    out = check50.run("python calc.py").exit(0) # stdout(timeout = 60) #



@check50.check(run)
def importlater():
    """ First calculations don't use imported packages """
    check50.include("calc.py")

    # Read in the file
    with open('calc.py', 'r') as file:
        filedata = file.read()

    sum_pos = filedata.rfind("sum_of_list")
    avg_pos = filedata.rfind("avg_of_list")
    import_pos = filedata.find("import")

    if import_pos < max(avg_pos, sum_pos):
        raise check50.Failure("Your program imports numpy or other packages too soon (or not at all)",\
                              help="Rearrange your code so that your sum_of_list and " +\
                                "mean_of_list variables\nare computed before you import any packages")

@check50.check(importlater)
def sum1():
    """ The sum is computed correctly """
    check50.include("calc.py")
    check50.log("Checking list of [5, 2, 0, 6, 1, 8]")

    # Read in the file
    with open('calc.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub('list_of_nums = \[[0-9\s,]+\]', 'list_of_nums = [5, 2, 0, 6, 1, 8]', filedata)

    # Write the file out again
    with open('calc.py', 'w') as file:
        file.write(filedata)
    calc = check50.py.import_("calc.py")
    oursum = builtins.sum([5, 2, 0, 6, 1, 8])
    theirsum = calc.sum_of_list

    if int(theirsum) != int(oursum):
        raise check50.Mismatch(str(oursum), str(theirsum))


@check50.check(sum1)
def sum2():
    """ The sum is computed correctly for a different list """
    check50.include("calc.py")
    check50.log("Checking list of [10, 12, 8]")

    # Read in the file
    with open('calc.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub('list_of_nums = \[[0-9\s,]+\]', 'list_of_nums = [10, 12, 8]', filedata)

    # Write the file out again
    with open('calc.py', 'w') as file:
        file.write(filedata)

    calc = check50.py.import_("calc.py")
    oursum = builtins.sum([10, 12, 8])
    theirsum = calc.sum_of_list

    if theirsum != oursum:
        raise check50.Mismatch(str(oursum), str(theirsum))


@check50.check(sum)
def sum3():
    """ The sum is computed correctly for a longer list """
    check50.include("calc.py")
    check50.log("Checking list of [100, 102, 104, 106, 44, 21, 19, 50, 1]")

    # Read in the file
    with open('calc.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub('list_of_nums = \[[0-9\s,]+\]', 'list_of_nums = [100, 102, 104, 106, 44, 21, 19, 50, 1]', filedata)

    # Write the file out again
    with open('calc.py', 'w') as file:
        file.write(filedata)

    calc = check50.py.import_("calc.py")
    oursum = builtins.sum([100, 102, 104, 106, 44, 21, 19, 50, 1])
    theirsum = calc.sum_of_list

    if theirsum != oursum:
        raise check50.Mismatch(str(oursum), str(theirsum))

@check50.check(importlater)
def avg1():
    """ The mean of a list is computed correctly  """
    check50.include("calc.py")
    check50.log("Checking list of [1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64]")

    # Read in the file
    with open('calc.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub('list_of_nums = \[[0-9\s,]+\]', 'list_of_nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64]', filedata)

    # Write the file out again
    with open('calc.py', 'w') as file:
        file.write(filedata)
    calc = check50.py.import_("calc.py")
    oursum = builtins.sum([1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64])/len([1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64])
    theirsum = calc.avg_of_list

    if int(theirsum) != int(oursum):
        raise check50.Mismatch(str(oursum), str(theirsum))

@check50.check(importlater)
def useimport():
    """ Later calculations use NumPy """
    check50.include("calc.py")

    # Read in the file
    with open('calc.py', 'r') as file:
        filedata = file.read()

    sum_pos = filedata.count("np.")

    if sum_pos < 2:
        raise check50.Failure("Your program doesn't make enough calls to the NumPy module's functions",\
                              help="Make sure TODO exercises 4 and 5 call NumPy functions in their computations")

@check50.check(useimport)
def sumnp():
    """ The sum is computed correctly using NumPy """
    check50.include("calc.py")
    check50.log("Checking list of [5, 2, 0, 6, 1, 8]")

    # Read in the file
    with open('calc.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub('list_of_nums = \[[0-9\s,]+\]', 'list_of_nums = [5, 2, 0, 6, 1, 8]', filedata)

    # Write the file out again
    with open('calc.py', 'w') as file:
        file.write(filedata)
    calc = check50.py.import_("calc.py")
    oursum = builtins.sum([5, 2, 0, 6, 1, 8])
    theirsum = calc.npadd_of_list

    if int(theirsum) != int(oursum):
        raise check50.Mismatch(str(oursum), str(theirsum))


@check50.check(sumnp)
def sumnplong():
    """ The sum of a longer list is computed correctly using NumPy """
    check50.include("calc.py")
    check50.log("Checking list of [1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64]")

    # Read in the file
    with open('calc.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub('list_of_nums = \[[0-9\s,]+\]', 'list_of_nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64]', filedata)

    # Write the file out again
    with open('calc.py', 'w') as file:
        file.write(filedata)
    calc = check50.py.import_("calc.py")
    oursum = builtins.sum([1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64])
    theirsum = calc.npadd_of_list

    if int(theirsum) != int(oursum):
        raise check50.Mismatch(str(oursum), str(theirsum))

@check50.check(useimport)
def mean1():
    """ The mean of a list is computed correctly using NumPy """
    check50.include("calc.py")
    check50.log("Checking list of [1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64]")

    # Read in the file
    with open('calc.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub('list_of_nums = \[[0-9\s,]+\]', 'list_of_nums = [1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64]', filedata)

    # Write the file out again
    with open('calc.py', 'w') as file:
        file.write(filedata)
    calc = check50.py.import_("calc.py")
    oursum = builtins.sum([1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64])/len([1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64])
    theirsum = calc.npmean_of_list

    if int(theirsum) != int(oursum):
        raise check50.Mismatch(str(oursum), str(theirsum))
    elif filedata.count("np.mean") < 1:
        raise check50.Failure("Expected NumPy function not called in calculation for average")