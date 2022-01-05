#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    window.title('frame demo')
    window.geometry('500x300')

    tk.Label(window, bg='yellow', font=('Arial', 12), width=40, height=2, text='i love yellow').pack()

    frame = tk.Frame(window)
    frame.pack()

    f1 = tk.Frame(frame)
    f2 = tk.Frame(frame)
    f1.pack(side='left')
    f2.pack(side='right')

    tk.Label(f1, text='frame 1 number 1', bg='red').pack()
    tk.Label(f1, text='frame 1 number 2', bg='red').pack()
    tk.Label(f1, text='frame 1 number 3', bg='red').pack()

    tk.Label(f2, text='frame 1 number 1', bg='green').pack()
    tk.Label(f2, text='frame 1 number 2', bg='green').pack()
    tk.Label(f2, text='frame 1 number 3', bg='green').pack()

    window.mainloop()
