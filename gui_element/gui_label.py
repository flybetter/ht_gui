#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    window.title("my window")
    window.geometry('500x300')
    l = tk.Label(window, text='你好，this is tkinter', bg='green', font=('Arial', 12), width=30, height=2)
    l.pack()
    window.mainloop()
