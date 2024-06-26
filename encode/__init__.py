# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50
import check50.c

@check50.check()
def exists():
    """encode.c exists"""
    check50.exists("encode.c")

@check50.check(exists)
def compiles():
    """encode.c compiles"""
    check50.c.compile("encode.c", lcs50=True)

@check50.check(compiles)
def short_phrase():
    """A phrase is encoded"""
    err_null = False
    out = check50.run("./encode").stdin("today is monday").stdout()
    out = out.strip()
    ans = "tid osa dmy ao yn"
    if len(out) == 0:
        raise check50.Mismatch(ans, "", help='You may be printing an empty string or only white space')
    try:
        if out[-1] == "\n" or ord(out[-1]) == 32:
            out = out[:-1]
        null_str = ""
        check_end = len(out)
        for i, char in enumerate(out):
            if ord(out[i]) == 0 and i < check_end-1:
                err_null = True
                null_str += "NULL"
                check_end -= 1
            elif ord(out[i]) != 0:
                null_str += out[i]
    except Exception as ME:
        raise check50.Failure("Code failed due to error", help = repr(ME))
    if err_null:
        check50.log("Any premature null characters in your string were replaced with 'NULL' to make them more visible")
        raise check50.Mismatch(ans, null_str, help='Do you have a premature null character?')
    elif out!=ans:
        raise check50.Mismatch(ans, out, help='Are you printing locations from your 2D array that you never assigned?')



@check50.check(short_phrase)
def other_phrase():
    """Another phrase is encoded"""
    err_null = False
    try:
        out = check50.run("./encode").stdin("today is friday").stdout()
        out = out.strip()
        if out[-1] == "\n" or ord(out[-1]) == 32:
            out = out[:-1]
        ans = "tid osa dfy ar yi"
        null_str = ""
        for i, char in enumerate(out):
            if ord(out[i]) == 0 and i < len(out)-1:
                err_null = True
                null_str += "NULL"
            else:
                null_str += out[i]
    except Exception as ME:
        raise check50.Failure("Code failed due to error", help = repr(ME))
    if err_null:
        check50.log("Any premature null characters in your string were replaced with 'NULL' to make them more visible")
        raise check50.Mismatch(ans, null_str, help='Do you have a premature null character?')
    elif out!=ans:
        raise check50.Mismatch(ans, out, help='Are you printing locations from your 2D array that you never assigned?')


@check50.check(other_phrase)
def spacey_word():
    """A phrase with several spaces is encoded"""
    try:
        out = check50.run("./encode").stdin("csAP  is    a super   awesome  class").stdout()
        out = out.strip()
        if out[-1] == "\n" or ord(out[-1]) == 32:
            out = out[:-1]
    except Exception as ME:
        raise check50.Failure("Code failed due to error", help = repr(ME))
    if out != "caae sswc Auel Ppsa ieos srms":
        raise check50.Mismatch("caae sswc Auel Ppsa ieos srms\n", out, help='Can your code skip multiple spaces in a row?')
