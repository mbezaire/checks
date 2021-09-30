# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50

@check()
def exists():
        """is_valid_tri.c exists"""
        check50.require("is_valid_tri.c")

@check("exists")
def compiles():
        """is_valid_tri.c compiles"""
        check50.spawn("clang -o is_valid_tri is_valid_tri.c -lcs50 -lm").exit(0)

@check("compiles")
def test_valid_tri():
        """Valid triangle yields true"""
        check50.spawn("./is_valid_tri").stdin("4","2","1").stdout("true\n", "true\n").exit(0)

@check("compiles")
def test_invalid_tri():
        """Invalid triangle yields false"""
        check50.spawn("./is_valid_tri").stdin("4","2","7").stdout("false\n", "false\n").exit(0)