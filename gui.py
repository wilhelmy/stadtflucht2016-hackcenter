#!/usr/bin/env python2.7

from Tkinter import Tk, Label

class GUI:
    def __init__(self, num_labels):
        self.root = Tk()
        self.labels = []
        for i in xrange(num_labels):
            l=Label(self.root)
            l.grid(row=0, column=i)
            self.labels.append(l)

    def color(self, i, value):
        self.labels[i].configure(bg=value)

    def mainloop(self):
        self.root.mainloop()

    def delay_color(self, delay, i, color):
        self.root.after(delay, lambda: self.color(i, value))

    def after(self, delay, cb):
        self.root.after(delay, cb)

if __name__ == '__main__':
    gui = GUI(42)
    gui.color(1,'red')
    gui.color(9,'pink')
    gui.delay_color(1000, 10,'green')
    gui.mainloop()
