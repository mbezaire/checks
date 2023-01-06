# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """roomtrie.c exists"""
    check50.exists("roomtrie.c")

@check50.check(exists)
def compiles():
    """roomtrie.c compiles"""
    check50.c.compile("roomtrie.c", lcs50=True)

@check50.check(compiles)
def short_phrase():
    """Rooms and names are encoded until -1 is entered"""
    err_null = False
    try:
        out = check50.run("./roomtrie").stdin("354").stdin("DrB").stdin("337").stdin("Ms Arnold").stdin("-1").stdout()
        out = out.strip()
    except Exception as ME:
        raise check50.Failure("Code failed due to error", help = repr(ME))
    if len(out) == 0:
        raise check50.Failure("Code isn't printing anything out", help='Are you checking for -1 and stopping collecting info after that?')



@check50.check(short_phrase)
def other_phrase():
    """Rooms and names are printed out after -1 is entered"""
    err_null = False
    try:
        out = check50.run("./roomtrie").stdin("354").stdin("DrB").stdin("354").stdin("Ms. Reidy").stdin("359").stdin("Ms. Reidy").stdin("359").stdin("DrB").stdin("337").stdin("DrB").stdin("337").stdin("Ms Arnold").stdin("33").stdin("Mr. Armstrong").stdin("-1").stdout()
        out = out.strip()

    except Exception as ME:
        raise check50.Failure("Code failed due to error", help = repr(ME))
    ans = "33: Mr. Armstrong\n337: DrB, Ms Arnold\n354: DrB, Ms. Reidy\n359: Ms. Reidy, DrB"
    if out!=ans:
        raise check50.Mismatch(ans, out, help='Are you traversing and printing out the trie after -1 is entered?')

