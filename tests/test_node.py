# -*- coding: utf-8 -*-

from binpacking import node

def test_one():
    assert True

main = (500, 500)
block1 = (200, 150)
block2 = (100, 60)
block3 = (100, 50)
block4 = (50, 50)

def test_two():
    root = node.Node(*main)

    root.split(0, 0, block1)

    assert root.size == 2

def test_two():
    root = node.Node(*main)

    ok = root.split(block1)
    assert ok != None

    ok = root.split(block2)
    assert ok != None

    ok = root.split(block3)
    assert ok != None

    ok = root.split(block4)
    assert ok != None
