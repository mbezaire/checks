import check50
import check50.py
import builtins
import re
import numpy

less = check50.import_checks("../calc")
from less import *

@check50.check(importlater)
def std1():
    """ The standard deviation of a list is computed correctly  """
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
    oursum = numpy.std([1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64])
    theirsum = calc.std_of_list

    if int(theirsum) != int(oursum):
        raise check50.Mismatch(str(oursum), str(theirsum))


@check50.check(useimport)
def std2():
    """ The standard deviation of a list is computed correctly using NumPy """
    # check50.include("calc.py")
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
    oursum = numpy.std([1, 2, 3, 4, 5, 10, 15, 20, 25, 36, 49, 64])
    theirsum = calc.npstd_of_list

    if int(theirsum) != int(oursum):
        raise check50.Mismatch(str(oursum), str(theirsum))
    elif filedata.count("np.std") < 1:
        raise check50.Failure("Expected NumPy function not called in calculation for standard deviation")