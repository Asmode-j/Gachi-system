import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
import random

kol_vo=0


def random_chislo():
    global kol_vo
    for i in range(1,11):
        kol_vo+=1
        lbl.configure(text=f'Кол-во: {kol_vo}')
        j=random.randint(1, 1000)
        if j<=6:
            txt_area.insert(tk.INSERT, '5* ')

            txt_area1.insert(tk.INSERT, f'Лега на {kol_vo}\n')
        elif j>1 and j<300:
            txt_area.insert(tk.INSERT, '4* ')
        else:
            txt_area.insert(tk.INSERT, '3* ')
    txt_area.insert(tk.INSERT, '\n')


window = tk.Tk()
window.title("Гача")  
window.geometry('750x550')

txt_area = scrolledtext.ScrolledText(window, width = 40)
txt_area.grid(sticky=tk.W, row=0,column=0, columnspan=2, padx=3)

btn = tk.Button(text = 'Крутить гачу', command=random_chislo)
btn.grid(sticky=tk.W + tk.N, column=0, row=1)
lbl = tk.Label(window, text=f'Кол-во: {kol_vo}', font=("Arial Bold", 16))
lbl.grid(sticky=tk.N,column=1, row=1)

txt_area1 = scrolledtext.ScrolledText(window, width = 40)
txt_area1.grid(sticky=tk.W, row=0,column=2, columnspan=2, padx=3)


window.mainloop()
