# -*- coding: utf-8 -*-
"""

@author: marianne.bezaire
"""

import check50

@check50.check()
def exists():
    """ghk.py was submitted"""
    check50.exists("ghk.py")


@check50.check(exists)
def test50():
    """GHK compute resting membrane potential"""
    check50.run("python3 ghk.py").stdout("-65.86336684929927").exit()
