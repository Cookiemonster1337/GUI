import tkinter as tk
from gui_classes import ZBTframe

root = tk.Tk()
w_main = ZBTframe(root, 'Data Analysis', 2, 3)

w_main.addButton('ECR', 'ECR Analysis', 0, 1)
w_main.addButton('POL', 'POL Analysis', 1, 1)
# b_main_01 = tk.Button(w_main, text='Contact Resistance')
# b_main_01.grid(row=0, column=0)
root.mainloop()
