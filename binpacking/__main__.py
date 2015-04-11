#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from binpacking.app import *

def run():
    root = tk.Tk()
    app = Application(master=root)
    root.title("Hello World")
    root.geometry('{0}x{1}'.format(DEFAULT_WIDTH, DEFAULT_HEIGHT))
    root.resizable(width= False, height= False)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        app.exit()

if __name__ == '__main__':
	run()
