# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """time_program.c was submitted"""
    check50.exists("time_program.c")

@check50.check(exists)
def compiles():
    """time_program.c compiles"""
    check50.c.compile("time_program.c", lcs50=True)

@check50.check(compiles)
def runs2():
    """time_program.c computes elapsed time"""
    check50.c.run("./time_program").stdin("10:22:59").stdin("10:23:01").stdout("00:00:02\n").exit(0)


@check50.check(compiles)
def runs():
    """time_program.c computes different elapsed time"""
    check50.c.run("./time_program").stdin("02:31:15").stdin("12:05:00").stdout("09:33:45\n").exit(0)


@check50.check(runs)
def runs2():
    """time_program.c has a 'time' data type with fields: hours, minutes, seconds"""
    check50.include('test_time.c')
    with open('time_program.c') as f:
        data = f.read()

    data = data.replace("int main(void)","void other()")
    with open('time_program.c','w') as f:
        f.write(data)

    #check50.c.compile("time_program.c", lcs50=True)
    check50.c.compile("test_time.c", lcs50=True)
    check50.log('Checking for a data structure of type time with fields: hours, minutes, seconds')
    check50.log('and an elapsed_time function that takes in an early time and a later time')
    check50.c.run("./test_time").stdout("00:04:10\n").exit(0)