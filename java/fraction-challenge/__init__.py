# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

check50.include("FClient.java", "F1Client.java", "F2Client.java", "F3Client.java", "F4Client.java", "F5Client.java", "F6Client.java", "F7Client.java")

out = check50.run("ls .").stdout()
check50.log(out)
out = check50.run("ls ..").stdout()
check50.log(out)

# less = check50.import_checks("../fraction")
# from less import *


# @check50.check(compiles)
# def reduce():
#     """Fractions can be reduced"""
#     out = check50.run("javac -d ./ F6Client.java").stdout(timeout = 60)
#     # check50.log(out)
#     # check50.log(check50.run("pwd").stdout())
#     # check50.log(check50.run("ls ./").stdout())
#     check50.run("java F6Client").stdin("13", prompt=False).stdin("52", prompt=False).stdout("1/4\n").exit(0)


# @check50.check(compiles)
# def makedouble():
#     """Fractions can be constructed from a double"""
#     out = check50.run("javac -d ./ F7Client.java").stdout(timeout = 60)
#     # check50.log(out)
#     # check50.log(check50.run("pwd").stdout())
#     # check50.log(check50.run("ls ./").stdout())
#     check50.run("java F7Client").stdin("1.25", prompt=False).stdout("5/4\n").exit(0)
