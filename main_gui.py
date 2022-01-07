#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter


def search_button_function(var1=None,search_content=None):
    if var1.get() == 1:
        search_content.insert('end','')
    if var1.get() == 2:
        search_content.insert('end','')


def main_function():
    window = tk.Tk()
    window.title('华泰自测小程序')
    window.geometry('800x600')

    left_menu = tk.Frame(window, width=80, relief='groove', borderwidth=1)

    top_tile = tk.Frame(window, relief='groove', borderwidth=1)

    right_workspace = tk.Frame(window, relief='groove', borderwidth=1)

    left_menu.pack(side='left', expand='no', fill='y')
    top_tile.pack(side='top', fill='x')
    right_workspace.pack(side='right', expand='yes', fill='both')
    # top_tile
    tk.Label(top_tile, text='华泰自测程序', height=1, bg='red').pack(fill='both')
    # left_menu
    tk.Button(left_menu, text='首页请求', font=('Arial', 12), width=10, height=1).pack()
    tk.Button(left_menu, text='业务请求', font=('Arial', 12), width=10, height=1).pack()
    tk.Button(left_menu, text='场景请求', font=('Arial', 12), width=10, height=1).pack()
    # right_workspace
    right_workspace_left = tk.Frame(window, relief='groove', borderwidth=1)
    right_workspace_left.pack(side='left', fill='y')
    right_workspace_right = tk.Frame(window, relief='groove', borderwidth=1)
    right_workspace_right.pack(side='right', fill='y')

    # right_workspace_right
    scroll = tk.Scrollbar(right_workspace_right)
    scroll.pack(side='right', fill='y')
    right_workspace_right_tx = tk.Text(right_workspace_right)
    right_workspace_right_tx.pack(side='left', fill='y')
    scroll.config(command=right_workspace_right_tx.yview)
    right_workspace_right_tx.config(yscrollcommand=scroll.set)

    # right_workspace_left
    search_content = tk.Entry(right_workspace_left, font=('Arial', 12), show=None)
    search_content.pack()

    var1 = tk.IntVar()
    var1.set(1)
    custerm_radio = tk.Radiobutton(right_workspace_left, variable=var1, text='custerm search', value=1)
    asset_radio = tk.Radiobutton(right_workspace_left, variable=var1, text='asset search', value=2)
    custerm_radio.pack()
    asset_radio.pack()

    search_button = tk.Button(right_workspace_left, width=20, text='搜索', command=lambda :search_button_function(var1,search_content))
    search_button.pack()

    # main function
    window.mainloop()


if __name__ == '__main__':
    main_function()
