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
    """grade_program.py and grades.csv were submitted"""
    check50.exists("grade_program.py")
    check50.exists("grades.csv")


@check50.check(exists)
def imports():
    """grade_program.py imports"""
    check50.py.import_("grade_program.py")


@check50.check(exists)
def extra():
    """check the missing list and the averages dictionary (either this check or the next one should pass)"""
    check50.run("python3 grade_program.py").stdout("['Ron - Aparecium', 'Ginny - Levicorpus', 'Ginny - Fidelius Charm', 'Luna - Aparecium']").stdout("{'Rictusempra': 15.375, 'Levicorpus': 17.642857142857142, 'Fidelius Charm': 17.714285714285715, 'Aparecium': 10.0}").exit(0)


@check50.check(exists)
def extraorig():
    """check the missing list and the averages dictionary according to original instructions (either this check or the previous one should pass)"""
    check50.run("python3 grade_program.py").stdout("['Ron - Aparecium', 'Ginny - Levicorpus', 'Ginny - Fidelius Charm', 'Luna - Aparecium']").stdout("{'Rictusempra': 0.76875, 'Levicorpus': 0.8821428571428571, 'Fidelius Charm': 0.8857142857142857, 'Aparecium': 1.0}").exit(0)

# def check_tournament(*args):
#     tournament = check50.py.import_("tournament.py")
#     actual = tournament.simulate_tournament(args[0])
#     teams = [x["team"] for x in args[0]]

#     if (not actual in teams):
#         raise check50.Failure("simulate_tournament fails to return the name of 1 winning team")