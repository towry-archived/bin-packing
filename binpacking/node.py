# -*- coding: utf-8 -*-

from binpacking import rect

class Node(object):
    def __init__(self, width= None, height= None, parent=None):
        self.left = None
        self.right = None
        self.parent = parent
        if width and height:
            self.rect = rect.Rect(width, height)
        else:
            self.rect = None

        self.size = 0

    def __repr__(self):
        return "<Node {}>".format(self.rect if self.rect else "None")

    @property
    def x(self):
        return self.rect.x
    @property
    def y(self):
        return self.rect.y
    @property
    def w(self):
        return self.rect.w
    @property
    def h(self):
        return self.rect.h

    def occupied(self):
        return self.rect and self.rect.occupied

    def occupy(self):
        if not self.rect: return
        self.rect.occupied = True

    def fit(self, *args):
        if len(args) == 1:
            if len(args[0]) != 2: raise ValueError()
            w, h = args[0]
        elif len(args) == 2:
            w, h = args
        else:
            raise ValueError("requires width and height")

        if self.rect.w == w and self.rect.h == h:
            return True
        else:
            return False

    def embrace(self, *args):
        if len(args) == 1:
            if len(args[0]) != 2: raise ValueError()
            w, h = args[0]
        elif len(args) == 2:
            w, h = args
        else:
            raise ValueError("requires width and height")

        if not self.rect: return False
        elif self.rect.w >= w and self.rect.h >= h:
            return True
        else:
            return False

    def split(self, *args):
        if len(args) == 1:
            if len(args[0]) != 2: raise ValueError()
            w, h = args[0]
        elif len(args) == 2:
            w, h = args
        else:
            raise ValueError("requires width and height")

        # sentinel
        if self.occupied():
            return None
        if not self.embrace(w, h):
            return None

        if self.fit(w, h):
            self.occupy()
            return self

        # if not splited
        if self.size == 0:
            self.left = Node()
            self.right = Node()
            self.size += 2
            # if self.rect.w - w == self.rect.h - h:
            # left/right or top/down is ok
            if self.rect.w - w > self.rect.h - h:
                # go with left/right
                self.left.rect = rect.Rect(w, self.rect.h, x= self.rect.x, y= self.rect.y)
                self.right.rect = rect.Rect(self.rect.w - w, self.rect.h, x= self.rect.x + w, y= self.rect.y)
            else:
                # go with top/down 
                self.left.rect = rect.Rect(self.rect.w, h, x= self.rect.x, y= self.rect.y)
                self.right.rect = rect.Rect(self.rect.w, self.rect.h - h, x= self.rect.x, y= self.rect.y + h)

        # recursively split it
        ok = self.left.split(w, h)
        if not ok:
            return self.right.split(w, h)
        else:
            return ok


"""
node = Node()
node.rect = Rect(500, 500)

box = (200, 150)
node.split(0, 0, box)

"""

def traverse(root):
    if root is None: return

    parent = root
    yield parent

    for n in traverse(parent.left):
        yield n 

    for n in traverse(parent.right):
        yield n
