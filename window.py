import tkinter as tk
import tkinter.font as tkFont
import calc

from tkinter.filedialog import askopenfile 

class App:
    def __init__(self, root):
        #setting title
        root.title("MebelPro")
        #setting window size
        width=583
        height=334
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLineEdit_358=tk.Entry(root)
        GLineEdit_358["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_358["font"] = ft
        GLineEdit_358["fg"] = "#333333"
        GLineEdit_358["justify"] = "left"
        GLineEdit_358["text"] = ""
        GLineEdit_358.place(x=70,y=90,width=395,height=33)

        GLineEdit_624=tk.Entry(root)
        GLineEdit_624["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_624["font"] = ft
        GLineEdit_624["fg"] = "#333333"
        GLineEdit_624["justify"] = "left"
        GLineEdit_624["text"] = ""
        GLineEdit_624.place(x=70,y=160,width=395,height=33)

        GLabel_563=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_563["font"] = ft
        GLabel_563["fg"] = "#333333"
        GLabel_563["justify"] = "center"
        GLabel_563["text"] = "Файл прайса"
        GLabel_563.place(x=70,y=60,width=422,height=30)

        GLabel_292=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_292["font"] = ft
        GLabel_292["fg"] = "#333333"
        GLabel_292["justify"] = "center"
        GLabel_292["text"] = "Рассчетный файл"
        GLabel_292.place(x=70,y=130,width=429,height=30)

        GButton_78=tk.Button(root)
        GButton_78["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_78["font"] = ft
        GButton_78["fg"] = "#000000"
        GButton_78["justify"] = "center"
        GButton_78["text"] = "Рассчитать закупочный лист"
        GButton_78.place(x=70,y=210,width=433,height=30)
        GButton_78["command"] = self.GButton_78_command

        GButton_402=tk.Button(root)
        GButton_402["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_402["font"] = ft
        GButton_402["fg"] = "#000000"
        GButton_402["justify"] = "center"
        GButton_402["text"] = ""
        GButton_402.place(x=470,y=90,width=33,height=33)
        GButton_402["command"] = self.GButton_402_command

        GButton_843=tk.Button(root)
        GButton_843["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_843["font"] = ft
        GButton_843["fg"] = "#000000"
        GButton_843["justify"] = "center"
        GButton_843["text"] = ""
        GButton_843.place(x=470,y=160,width=33,height=33)
        GButton_843["command"] = self.GButton_843_command

    def GButton_78_command(self):
        print("command")


    def GButton_402_command(self):
        self.price_dir = askopenfile(mode='r')



    def GButton_843_command(self):
        self.pro100_dir = askopenfile(mode='r')


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
