#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk


def print_selection():
    value=box.get(box.curselection())
    var1.set(value)


if __name__ == '__main__':
    window = tk.Tk()
    window.title('listbox demo')
    window.geometry('500x300')

    var1 = tk.StringVar()
    l1 = tk.Label(window, bg='green', fg='yellow', font=('Arial', 12), width=12, height=2, textvariable=var1)
    l1.pack()

    b1 = tk.Button(window, width=12, height=1, text='print selection', command=print_selection)
    b1.pack()

    var2 = tk.StringVar()
    var2.set((1, 2, 3, 4))

    box = tk.Listbox(window, listvariable=var2)
    list_items = [11, 22, 33, 44];
    for item in list_items:
        box.insert("end", item)

    box.pack()

    window.mainloop()
