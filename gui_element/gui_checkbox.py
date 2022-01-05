#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk


def print_selection():
    if var1.get() == 1 and var2.get() == 0:
        l1.config(text='I love python')
    elif var1.get() == 0 and var2.get() == 1:
        l1.config(text='I love c++')
    elif var1.get() == 0 and var2.get() == 0:
        l1.config(text='i dont love both')
    else:
        l1.config(text='I love both')


if __name__ == '__main__':
    window = tk.Tk()
    window.title('checkbox demo')
    window.geometry('500x300')
    l1 = tk.Label(window, font=('Arias', 12), width=40, height=2, bg='yellow', text='empty')
    l1.pack()
    #
    # var1 = tk.IntVar()
    # var2 = tk.IntVar()
    # c1 = tk.Checkbutton(window, text='python', textvariable=var1, onvalue=1, offvalue=0, command=print_selection)
    # c2 = tk.Checkbutton(window, text='c++', textvariable=var2, onvalue=1, offvalue=0, command=print_selection)
    # c1.pack()
    # c2.pack()
    var1 = tk.IntVar()  # 定义var1和var2整型变量用来存放选择行为返回值
    var2 = tk.IntVar()
    c1 = tk.Checkbutton(window, text='Python', variable=var1, onvalue=1, offvalue=0,
                        command=print_selection)  # 传值原理类似于radiobutton部件
    c1.pack()
    c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
    c2.pack()

    window.mainloop()
