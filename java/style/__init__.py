# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c


def compiles():
	"""Java file(s) compile"""
	out = check50.run("javac -d ./ *.java").stdout(timeout = 60)
	check50.log(out)
