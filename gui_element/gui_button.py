#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk


def hit_me():
    global on_hit
    if on_hit is False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("...")


if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('500x300')
    window.title('button demo')
    var = tk.StringVar()
    l = tk.Label(window, bg='green', font=('Arial', 12), textvariable=var, width=30, height=2)
    l.pack()
    on_hit=False
    b=tk.Button(window,text='hit me',font=('Arial',12),width=10,height=1,command=hit_me)
    b.pack()
    window.mainloop()
