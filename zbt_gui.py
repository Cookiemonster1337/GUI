import tkinter as tk
from PIL import ImageTk, Image

version, year = 0.1, 2021
author = 'JKP'


class ZBTframe(tk.Frame):

    def __init__(self, rows, columns, height=500, width=400, bg='grey20'):
        tk.Frame.__init__(self)
        self.config(bg=bg, width=width, height=height)

        for r in range(rows):
            self.grid_rowconfigure(r, weight=1)

        for c in range(columns):
            self.grid_columnconfigure(c, weight=1)


class ZBTbutton(tk.Button):

    def __init__(self, frame, text, command):
        tk.Button.__init__(self, frame)
        self.master = frame
        self.config(bg='lightgrey', text=text, command=lambda: command)


class ZBTwindow(tk.Tk):

    def __init__(self, name, rows=1, columns=1, x_dim=500, y_dim=400):
        tk.Tk.__init__(self)
        self.title(name)
        self.geometry('{}x{}'.format(x_dim, y_dim))
        self.config(bg='lightgrey')
        self.iconbitmap('zbt_logo.ico')
        self.rows = rows
        self.columns = columns
        self.y_dim = y_dim
        self.x_dim = x_dim

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.top = ZBTframe(rows, columns, height=(y_dim - 20), width=x_dim)
        self.top.grid_propagate(0)
        self.bot = ZBTframe(1, 1, height=20, width=x_dim, bg='grey25')
        self.bot.grid_propagate(0)

        self.top.grid(row=0, column=0, sticky='nesw')
        self.bot.grid(row=1, column=0, sticky='nesw')

        self.footnote = 'Ver.: ' + str(version) + ' (' + str(year) + ') by ' + \
                        author
        self.foot = tk.Label(self.bot, text=self.footnote, bg='grey25',
                             fg='snow')
        self.foot.grid(row=0, column=0, sticky='e')

    def addButton(self, row, column, id, name, text='unnamed'):
        id = ZBTbutton(main.top, text=text, command=lambda: print('test'))
        # id = ZBTbutton(zbt.top, text=text, command=lambda: ZBTtoplevel(self, name=name))
        id.grid(row=row, column=column, sticky='news', padx=10, pady=10)


class ZBTtoplevel(tk.Toplevel):

    def __init(self, name):
        tk.Toplevel.__init__(self)
        self.title(name)
        self.geometry('1000x800')
        self.iconbitmap('zbt_logo.ico')


main = ZBTwindow('Data Analysis', rows=10, columns=3)


def ButtonEvent(name):
        buttonevent = ZBTtoplevel(name=name)
        buttonevent.mainloop()

b1 = ZBTbutton(main.top, text='POL', command=lambda arg='1': print(arg))
# command=lambda: ButtonEvent(name='pol-analysis')
b1.grid(row=0, column=1, sticky='news', padx=10, pady=10)

# zbt.addButton(0, 1, id='b1', text='POL', name='POL-Analysis')
# zbt.addButton(1, 1, id='b2', text='EIS', name='EIS-Analysis')
# zbt.addButton(2, 1, id='b3', text='MS', name='MS-Analysis')
# zbt.addButton(3, 1, id='b4', text='ECR', name='ECR-Analysis')

img_pol = Image.open('pol-curve.png')
img_eis = Image.open('eis-curve.png')
img_ms = Image.open('ms-spectra.png')
img_ecr = Image.open('ecr-curve.png')

ph_pol = ImageTk.PhotoImage(img_pol.resize((50, 50), Image.ANTIALIAS))
ph_eis = ImageTk.PhotoImage(img_eis.resize((50, 50), Image.ANTIALIAS))
ph_ms = ImageTk.PhotoImage(img_ms.resize((50, 50), Image.ANTIALIAS))
ph_ecr = ImageTk.PhotoImage(img_ecr.resize((50, 50), Image.ANTIALIAS))

label_ph_pol = tk.Label(main.top, image=ph_pol, width=50, height=50, padx=10, pady=10)
label_ph_eis = tk.Label(main.top, image=ph_eis, width=50, height=50, padx=10, pady=10)
label_ph_ms = tk.Label(main.top, image=ph_ms, width=50, height=50, padx=10, pady=10)
label_ph_ecr = tk.Label(main.top, image=ph_ecr, width=50, height=50, padx=10, pady=10)

label_ph_pol.grid(row=0, column=0)
label_ph_eis.grid(row=1, column=0)
label_ph_ms.grid(row=2, column=0)
label_ph_ecr.grid(row=3, column=0)

main.mainloop()
