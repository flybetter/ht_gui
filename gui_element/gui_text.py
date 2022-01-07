#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter


def insert_point():
    var = e1.get()
    t.insert("insert", var)


def insert_end():
    var = e1.get()
    t.insert("end", var)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('text demo')
    window.geometry('500x300')
    e1 = tk.Entry(window, show=None)
    e1.pack()
    b1 = tk.Button(window, text='insert', width=40, height=3, command=insert_point)
    b1.pack()
    b2 = tk.Button(window, text='end', width=40, height=3, command=insert_end)
    b2.pack()
    scroll=tk.Scrollbar()
    scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    t = tk.Text(window)
    t.pack(side=tkinter.LEFT, fill=tkinter.Y)
    scroll.config(command=t.yview)
    t.config(yscrollcommand=scroll.set)


    window.mainloop()
