# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """doublesort.c exists"""
    check50.exists("doublesort.c")

@check50.check(exists)
def compiles():
    """doublesort.c compiles - other checks will occur manually"""
    check50.c.compile("doublesort.c", lcs50=True)

#@check50.check(compiles)
#def short_phrase():
#    """The doubly linked list builds and sorts and inserts correctly"""
#    err_null = False
#    try:
#        out = check50.run("./encode").stdin("today is monday").stdout()
#        out = out.strip()
#        if out[-1] == "\n" or ord(out[-1]) == 32:
#            out = out[:-1]
#        ans = "tid osa dmy ao yn"
#        null_str = ""
#        check_end = len(out)
#        for i, char in enumerate(out):
#            if ord(out[i]) == 0 and i < check_end-1:
#                err_null = True
#                null_str += "NULL"
#                check_end -= 1
#            elif ord(out[i]) != 0:
#                null_str += out[i]
#    except Exception as ME:
#        raise check50.Failure("Code failed due to error", help = repr(ME))
#    if err_null:
#        check50.log("Any premature null characters in your string were replaced with 'NULL' to make them more visible")
#        raise check50.Mismatch(ans, null_str, help='Do you have a premature null character?')
#    elif out!=ans:
#        raise check50.Mismatch(ans, out, help='Are you printing locations from your 2D array that you never assigned?')