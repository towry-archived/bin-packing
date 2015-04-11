# -*- coding: utf-8 -*-

import os
from binpacking import rect, node


def test_one():
    r = rect.Rect(30, 40)

    assert r.x == 0
    assert r.y == 0
    assert r.w == 30
    assert r.h == 40

def test_two():
    r = rect.Rect(20, 30, x= 100, y= 50)

    assert r.x == 100
    assert r.y == 50
    assert r.w == 20
    assert r.h == 30

def test_three():

    try:
        r = rect.Rect(30, x= 100)
    except:
        assert True
        return
    assert False
