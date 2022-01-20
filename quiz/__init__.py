# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import os
import re
import check50
import check50.py

@check50.check()
def exists():
    """grade_program.py was submitted"""
    check50.exists("grade_program.py")


@check50.check(exists)
def imports():
    """shoppinglist.py imports"""
    check50.py.import_("grade_program.py").exit(0)


@check50.check(exists)
def grade():
    """check the missing list"""
    check50.run("python3 grade_program.py").stdout(['Ron - Aparecium', 'Ginny - Levicorpus', 'Ginny - Fidelius Charm', 'Luna - Aparecium']).exit(0)

# def check_tournament(*args):
#     tournament = check50.py.import_("tournament.py")
#     actual = tournament.simulate_tournament(args[0])
#     teams = [x["team"] for x in args[0]]

#     if (not actual in teams):
#         raise check50.Failure("simulate_tournament fails to return the name of 1 winning team")