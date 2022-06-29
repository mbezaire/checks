# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50

@check50.check()
def exists():
    """seaslug.py was submitted"""
    check50.exists("seaslug.py")

@check50.check(exists)
def calc_ex1():
    """No habituation"""
    check50.run("python seaslug.py").stdin("0").stdout("[0, 0, 4, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0, 0.0, 0.0, 4.0, 0.0, 0.0]").exit(0)


@check50.check(exists)
def calc_ex2():
    """Habituation rate of 0.3"""
    check50.run("python seaslug.py").stdin("0.3").stdout("[0, 0, 4, 0.0, 0.0, 0.0, 0.0, 2.8, 0.0, 0.0, 0.0, 0.0, 1.9599999999999997, 0.0, 0.0, 0.0, 0.0, 1.3719999999999997, 0.0, 0.0, 0.0, 0.0, 0.9603999999999997, 0.0, 0.0, 0.0, 0.0, 0.6722799999999998, 0.0, 0.0]").exit(0)

