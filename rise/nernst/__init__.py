# -*- coding: utf-8 -*-
"""

@author: marianne.bezaire
"""

import check50

@check50.check()
def exists():
    """nernst.py was submitted"""
    check50.exists("nernst.py")


@check50.check(exists)
def test50():
    """Potassium reversal potential"""
    check50.run("python3 nernst.py").stdin("1").stdin("140").stdin("5").stdout("-85.56512331602639").exit()


@check50.check(exists)
def calc_ex2():
    """Chloride reversal potential"""
    check50.run("python3 nernst.py").stdin("-1").stdin("5").stdin("50").stdout("-59.12631617478978").exit()


@check50.check(exists)
def calc_ex3():
    """Sodium reversal potential"""
    check50.run("python3 nernst.py").stdin("1").stdin("15").stdin("145").stdout("58.25578423688606").exit()

