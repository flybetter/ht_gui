#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk

if __name__ == '__main__':
    window=tk.Tk()
    window.title('entry demo')
    window.geometry("500x300")
    e1=tk.Entry(window,font=('Arial',12),show='*')
    e2=tk.Entry(window,font=('Arial',12),show=None)
    e1.pack()
    e2.pack()
    window.mainloop()

