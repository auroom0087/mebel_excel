from typing import Literal
import calc
from tkinter import *

def on_click():
    result, final_sum = calc.calc_report()
    print(result)

window = Tk()
window.title("Рассчет стоимости мебели")
window.geometry('400x200')
lbl = Label(window, text="Выберите файл-отчет из программы PRO100")  
lbl.grid(column=0, row=0)
btn = Button(window, text="Рассчет", command=on_click)  
btn.grid(column=0, row=1)  
window.mainloop()