# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:28:44 2021

@author: marianne.bezaire
"""

import check50

@check50.check()
def exists():
    """LoopQuilts.java and the image quilt exist"""
    check50.exists("LoopQuilts.java")
    check50.exists("Quilt_1.bmp")


