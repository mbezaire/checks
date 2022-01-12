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
    """shoppinglist.py was submitted"""
    check50.exists("shoppinglist.py")


@check50.check(exists)
def imports():
    """shoppinglist.py imports"""
    check50.py.import_("shoppinglist.py").stdin("done\n")


@check50.check(imports)
def shop():
    """check the list"""
    out = check50.run("python3 shoppinglist.py").stdin("carrots").stdin("parsnips").stdin("done").stdout()
    if out.strip() != "Buy eggs":
        raise check50.Mismatch("Buy carrots", out, help="Check your logic")

# def check_tournament(*args):
#     tournament = check50.py.import_("tournament.py")
#     actual = tournament.simulate_tournament(args[0])
#     teams = [x["team"] for x in args[0]]

#     if (not actual in teams):
#         raise check50.Failure("simulate_tournament fails to return the name of 1 winning team")