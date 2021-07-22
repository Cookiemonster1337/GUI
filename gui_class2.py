import tkinter as tk

class ZBTMasterframe(tk.Tk):

    def __init__(self, name, rows, columns, xdim=None, ydim=None):

        self.title(name)
        if xdim is None:
            xdim = 500
        if ydim is None:
            ydim = 400
        self.geometry('{}x{}'.format(xdim, ydim))
        self.config(bg='lightgrey')
        self.iconbitmap('zbt_logo.ico')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)

        master_topframe = tk.Frame(master, bg='grey25', width=500,
                                   height=ydim - 20)
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
                                                  ' (' + str(
            year) + ') by ' + author,
                            bg='grey20', fg='snow')
        label_01.grid(row=0, column=0, sticky='e')

        self.master_topframe = master_topframe

main = ZBTMasterframe()
main.mainloop()