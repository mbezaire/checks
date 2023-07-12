import check50
import check50.py
import builtins
import re

@check50.check()
def exists():
    """ Check that game.py exists """
    check50.exists("game.py")

@check50.check(exists)
def run():
    """ File runs without syntax errors"""
    check50.py.compile("game.py")