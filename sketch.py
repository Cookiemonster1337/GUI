import tkinter as tk


x_dim = 500
y_dim = 400

rows = 10
columns = 3

title = 'ZBT Analysis'

window = tk.Tk()
window.iconbitmap('zbt_logo.ico')
window.title(title)
window.geometry('{}x{}'.format(x_dim, y_dim))

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)

frame1 = tk.Frame(bg='grey20', height=480)
frame2 = tk.Frame(bg='grey25', height=20)

frame1.grid(row=0, column=0, sticky='news')
frame2.grid(row=1, column=0, sticky='news')

for r in range(rows):
    frame1.grid_rowconfigure(r, weight=1)

for c in range(columns):
    frame1.grid_columnconfigure(c, weight=1)


frame2.grid_rowconfigure(0, weight=1)
frame2.grid_columnconfigure(0, weight=1)

label1= tk.Label(frame2, text='testtesttest')
label1.grid(row=0, column=2, sticky='e')


b1 = tk.Button(frame1, text='POL', bg='lightgrey', command=lambda: print('test'))
b1.grid(row=0, column=1, sticky='news', padx=10, pady=10)

b2 = tk.Button(frame1, text='EIS', bg='lightgrey')
b2.grid(row=1, column=1, sticky='news', padx=10, pady=10)

b3 = tk.Button(frame1, text='ECR', bg='lightgrey')
b3.grid(row=2, column=1, sticky='news', padx=10, pady=10)

window.mainloop()