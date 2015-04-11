# -*- coding: utf-8 -*-
"""
    main.app 
    ~~~~~~~~

    :copyright: (c) 2015 by Towry Wang.
    :license: MIT, see <http://towry.me/mit-license/>.

    :requires:
        python >= 3
"""

import tkinter as tk
from tkinter import ttk
import re
import random
from datetime import datetime

import binpacking.node as mnode

__all__ = ['Application', 'tk', 'DEFAULT_WIDTH', 'DEFAULT_HEIGHT']

DEFAULT_WIDTH = 400
DEFAULT_HEIGHT = 500

class Application(object):

    def __init__(self, master= None):
        master.columnconfigure(0, weight= 1)
        master.rowconfigure(0, weight= 1)
        self.master = master
        self.frame = tk.Frame(master, width= DEFAULT_WIDTH, height= DEFAULT_HEIGHT)
        self.frame.grid_propagate(False)
        self.frame.columnconfigure(0, weight= 1)
        self.frame.columnconfigure(1, weight= 1)
        self.frame.rowconfigure(3, weight= 1)
        self.frame.grid(row= 0, column= 0, sticky=(tk.N, tk.W, tk.E, tk.S), padx= 5)
        self._help_text = tk.StringVar(master)

        self._create_widgets()

        w, h = self.get_canvas_winfo()
        self._help_text.set("Input in this form:\nwidth*height\nor width*height*number\nCanvas: w{}:h{}".format(w, h))

    def _create_widgets(self):
        # label
        label = tk.Label(self.frame, justify= "left", textvariable= self._help_text, font= ("Consolas", 11))
        label.grid(row= 0, column= 0, sticky= tk.W)

        # text
        frame_text = tk.Frame(self.frame)
        frame_text.grid(row= 1, column= 0, sticky= (tk.N, tk.W, tk.E, tk.S))

        text = tk.Text(frame_text, height= 5, width= 25)
        text.insert(tk.END, "50*60")
        text.grid(row= 0, column= 0, pady= (0, 10), sticky= (tk.W, tk.E))
        
        text_log = tk.Text(frame_text, height= 5)
        text_log.grid(row= 0, column= 1, pady= (0, 10), sticky= (tk.W, tk.E))
        self._log_text_widget = text_log

        #button
        frame_button = tk.Frame(self.frame)
        frame_button.grid(row= 2, column= 0, pady= (0, 10), sticky= tk.W)
        button = tk.Button(frame_button, text= "Update", command= self._btn_click)
        button.grid(row= 0, column= 0)
        button_clear = tk.Button(frame_button, text= "Clear", command= self._btn_clear)
        button_clear.grid(row= 0, column= 1, padx= (10, 0))

        #canvas
        # canvas_sh = tk.Scrollbar(self.master, orient= tk.HORIZONTAL)
        # canvas_sv = tk.Scrollbar(self.master, orient= tk.VERTICAL)
        # scrollregion=(0, 0, 1000, 1000)
        canvas = tk.Canvas(self.frame, bg= "white")
        # canvas['yscrollcommand'] = canvas_sv.set
        # canvas['xscrollcommand'] = canvas_sh.set
        # canvas_sh['command'] = canvas.xview
        # canvas_sv['command'] = canvas.yview
        # ttk.Sizegrip(self.master).grid(column= 1, row= 3, sticky= (tk.S, tk.E))
        # canvas_sh.grid(column= 0, row= 3, sticky= (tk.W, tk.E))
        # canvas_sv.grid(column= 1, row= 3, sticky= (tk.N, tk.S))
        canvas.grid(row= 3, column= 0, ipadx= 5, pady= (0, 5), sticky= tk.W+tk.N+tk.E+tk.S)

        self.text = text 
        self.canvas = canvas

    def _btn_click(self):
        text = self.text.get(1.0, tk.END)
        if text.strip() == "": return
        self._process(text)
    def _btn_clear(self):
        self.canvas.delete('all')
        self.text.delete(1.0, tk.END)
        self._log_text_widget.delete(1.0, tk.END)

    def _log(self, msg):
        now = datetime.now().strftime("%H:%M:%S")
        print("{} - {}".format(now, msg))
        self._log_text_widget.insert(tk.END, "{} - {}\n".format(now, msg))

    def _process(self, text):
        text = text.split('\n')
        pattern = re.compile('^(\d+)\*(\d+)(?:\*(\d+))?$')
        matrix = []
        for t in text:
            m = pattern.match(t)
            if not m:
                continue
            else:
                group = m.groups()
                if group[2] != None:
                    for i in range(int(group[2])):
                        matrix.append(tuple(int(x) for x in group[:-1]))
                else:
                    matrix.append(tuple(int(x) for x in group[:-1]))

        if not len(matrix): return

        # clean the canvas
        self.canvas.delete('all')
        self._draw_all(matrix)
        
    def _draw_all(self, matrix):
        color = None
        node = None
        cw, ch = self.get_canvas_winfo()
        root = mnode.Node(cw, ch)
        self.missed = []
        for unit in matrix:
            node = root.split(unit)
            if node is None:
                self._log("missed")
                self.missed.append(unit)
            else:
                if node.occupied(): print(node) 
                # draw the block
                color = self._color()
                self.draw_block(node.x, node.y, node.w, node.h, fill= color)

    def exit(self):
        self.master.destroy()

    def get_canvas_winfo(self):
        return (self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight())

    def draw_block(self, x, y, w, h, fill= 'blue', outline= 'white'):
        # space for outline
        if outline is None:
            outline = fill

        self.canvas.create_rectangle(x, y, x + w, y + h, fill= fill, outline= outline)

    @classmethod
    def _color(cls):
        r = lambda: random.randint(0, 255)
        return "#{0:02X}{1:02X}{2:02X}".format(r(), r(), r())
