import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('root')
root.geometry('{}x{}'.format(300,200))


root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


def button1_event():
    subroot1 = tk.Toplevel(root)
    subroot1.title('subroot1')
    subroot1.geometry('500x400')

    frame1 = tk.Frame(subroot1, bg='blue', width=500, height=100)
    frame2 = tk.Frame(subroot1, bg='red', width=500, height=100)
    frame3 = tk.Frame(subroot1, bg='cyan', width=500, height=100)
    frame4 = tk.Frame(subroot1, bg='magenta', width=500, height=100)

    subroot1.grid_rowconfigure(0, weight=1)
    subroot1.grid_rowconfigure(1, weight=1)
    subroot1.grid_rowconfigure(2, weight=1)
    subroot1.grid_rowconfigure(3, weight=1)
    subroot1.grid_columnconfigure(0, weight=1)

    frame1.grid(row=0, sticky='nesw')
    frame2.grid(row=1, sticky='nesw')
    frame3.grid(row=2, sticky='nesw')
    frame4.grid(row=3, sticky='nesw')

    frame1.grid_rowconfigure(1, weight=1)
    frame1.grid_columnconfigure(0, weight=1)
    frame1.grid_columnconfigure(1, weight=1)
    frame1.grid_columnconfigure(2, weight=1)

    frame2.grid_rowconfigure(1, weight=1)
    frame2.grid_columnconfigure(0, weight=1)

    frame3.grid_rowconfigure(1, weight=1)
    frame3.grid_columnconfigure(0, weight=1)

    frame4.grid_rowconfigure(1, weight=1)
    frame4.grid_columnconfigure(0, weight=1)

    label1 = tk.Label(frame1, text='Label 1', bg='green')
    label2 = tk.Label(frame2, text='Label 2', bg='green')
    label3 = tk.Label(frame3, text='Label 3', bg='green')
    label4 = tk.Label(frame4, text='Label 4', bg='green')

    label1.grid(row=0, column=0, padx=5, pady=5, sticky='nesw')
    label1.config(font=('helvetica', 14))
    label2.grid(row=0, column=0, padx=5, pady=5, sticky='nesw')
    label3.grid(row=0, column=0, padx=5, pady=5, sticky='nesw')
    label4.grid(row=0, column=0, padx=5, pady=5, sticky='nesw')

    entry1 = tk.Entry(frame1, bg='white', bd=2)

    entry1.grid(row=0, column=1, sticky='nesw')

    OptionList1 = ['option1', 'option2', 'option3', 'option4']

    var1 = tk.StringVar(frame1)
    var1.set(OptionList1[0])

    optlist1 = tk.OptionMenu(frame1, var1, *OptionList1)
    optlist1.config(width=10, font=('Helvetica', 14), bg='grey')

    optlist1.grid(row=0, column=2, sticky='nesw')

    vlist = ["option1", "option2", "option3", "option4"]

    def changevalue():
        vlist.append('option5')

    combobox1 = ttk.Combobox(frame2, values=vlist, postcommand=changevalue)

    combobox1.grid(row=0, column=2, sticky='nesw')
    combobox1.current(0)

    def callbackFunc(event):
        print('new element selected')

    combobox1.bind('<<ComboboxSelected>>', callbackFunc)

    subroot1.mainloop()

button1 = tk.Button(root, text='Button 1', bg='yellow', command=button1_event)

button1.grid(row=0, column=0)

root.mainloop()


