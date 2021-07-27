import tkinter as tk

version, year = 0.1, 2021
author = 'JKP'

class ZBTframe:

    def __init__(self, master, name, rows, columns, xdim=None, ydim=None):
        self.master = master

        master.title(name)
        if xdim is None:
            xdim = 500
        if ydim is None:
            ydim = 400
        master.geometry('{}x{}'.format(xdim, ydim))
        master.config(bg='lightgrey')
        master.iconbitmap('zbt_logo.ico')

        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)

        master_topframe = tk.Frame(master, bg='grey25', width=500,
                                   height=ydim-20)
        master_botframe = tk.Frame(master, bg='grey20', width=500, height=20)
        master_topframe.grid(row=0, column=0, columnspan=columns,
                             sticky='nesw')
        master_botframe.grid(row=1, column=0, columnspan=columns,
                             sticky='nesw')

        for i in range(rows + 1):
            master_topframe.grid_rowconfigure(i, weight=1)

        for i in range(columns):
            master_topframe.grid_columnconfigure(i, weight=1)

        master_botframe.grid_rowconfigure(0, weight=1)
        master_botframe.grid_columnconfigure(0, weight=1)

        label_01 = tk.Label(master_botframe, text='Ver.: ' + str(version) +
                                           ' (' + str(year) + ') by ' + author,
                            bg='grey20', fg='snow')
        label_01.grid(row=0, column=0, sticky='e')

        self.master_topframe = master_topframe

    def addButton(self, button_name, frame_name, row, column, xdim=None, ydim=None):

        def pressButton(frame_name, xdim, ydim):
            sub = ZBTSubframe(self.master, frame_name, xdim, ydim)

        name = tk.Button(self.master_topframe, text=button_name, bg='lightgrey',
                         command=lambda: pressButton(frame_name,
                                                     xdim, ydim))
        name.grid(row=row, column=column)


class ZBTSubframe:

    def __init__(self, main, name, xdim=None, ydim=None):
        sub = tk.Toplevel(main)
        sub.title(name)
        if xdim is None:
            xdim = 300
        if ydim is None:
            ydim = 200
        sub.geometry('{}x{}'.format(xdim, ydim))
        sub.config(bg='grey25')
        sub.iconbitmap('zbt_logo.ico')


