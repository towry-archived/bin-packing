# -*- coding: utf-8 -*-

class Rect(object):
    def __init__(self, w, h, x= 0, y= 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.occupied = False

    def __repr__(self):
        return "<Rect {}, {}, {}, {}>".format(self.x, self.y, self.w, self.h)
