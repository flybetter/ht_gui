#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk


def print_selection():
    l1.config(text="you select " + var1.get())


if __name__ == '__main__':
    window = tk.Tk()
    window.title('raido demo')
    window.geometry('500x300')

    var1 = tk.StringVar()
    l1 = tk.Label(window, bg='yellow', font=('Arial', 12), width=40, height=4, text='empty')
    l1.pack()

    r1 = tk.Radiobutton(window, text='Opthon A', variable=var1, value='A', command=print_selection)
    r2 = tk.Radiobutton(window, text='Opthon B', variable=var1, value='B', command=print_selection)
    r3 = tk.Radiobutton(window, text='Opthon C', variable=var1, value='C', command=print_selection)
    r1.pack()
    r2.pack()
    r3.pack()

    window.mainloop()
