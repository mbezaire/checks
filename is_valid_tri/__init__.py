# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

from check50 import *

class ValidTri(Checks):

	@check()
	def exists(self):
		"""is_valid_tri.c exists"""
		self.require("is_valid_tri.c")

	@check("exists")
	def compiles(self):
		"""is_valid_tri.c compiles"""
		self.spawn("clang -o is_valid_tri is_valid_tri.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_valid_tri(self):
		"""Valid triangle yields true"""
		self.spawn("./is_valid_tri").stdin("4","2","1").stdout("true\n", "true\n").exit(0)

	@check("compiles")
	def test_invalid_tri(self):
		"""Invalid triangle yields false"""
		self.spawn("./is_valid_tri").stdin("4","2","7").stdout("false\n", "false\n").exit(0)