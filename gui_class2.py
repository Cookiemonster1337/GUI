import tkinter as tk

version, year = 0.1, 2021
author = 'JKP'

class ZBTMasterframe(tk.Tk):

    def __init__(self):
        pass

class ZBTwindow(tk.Tk):

    def __init__(self, name, rows=1, columns=3, xdim=500, ydim=400):
        tk.Tk.__init__(self)
        self.title(name)
        self.geometry('{}x{}'.format(xdim, ydim))
        self.config(bg='lightgrey')
        self.iconbitmap('zbt_logo.ico')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        topframe = tk.Frame(bg='grey20', height=(ydim-20), width=ydim)
        botframe = tk.Frame(bg='grey25', height=20, width=ydim)

        topframe.grid(row=0, column=0, sticky='nesw')
        botframe.grid(row=1, column=0, sticky='nesw')

        for i in range(rows+1):
            topframe.grid_rowconfigure(i, weight=1)

        for i in range(columns):
            topframe.grid_columnconfigure(i, weight=1)

        botframe.grid_rowconfigure(0, weight=1)
        botframe.grid_columnconfigure(0, weight=1)

        footnote = 'Ver.: ' + str(version) +' (' + str(year) + ') by ' + author
        footlabel = tk.Label(botframe, text=footnote, bg='grey25', fg='snow')
        footlabel.grid(row=0, column=0, sticky='e')

    i = 0

    @classmethod
    def addButton(cls, i=i, title='unnamed', row=i, column=1):
        b_id = 'b_'+ str(i)
        b_id = tk.Button(cls.topframe, text=title)
        b_id.grid(row=row, column=column)
        #i += 1

class ZBTbutton():
    def __init__(self):
        tk.Button.__init__(self)


class ZBTframe(tk.Toplevel):

    def __init__(self):
        pass

sub = ZBTSubframe('test')

sub.mainloop()