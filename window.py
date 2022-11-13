import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("MebelPro")
        #setting window size
        width=578
        height=348
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
        GLineEdit_358["justify"] = "center"
        GLineEdit_358["text"] = ""
        GLineEdit_358.place(x=70,y=90,width=423,height=30)

        GLineEdit_624=tk.Entry(root)
        GLineEdit_624["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_624["font"] = ft
        GLineEdit_624["fg"] = "#333333"
        GLineEdit_624["justify"] = "center"
        GLineEdit_624["text"] = ""
        GLineEdit_624.place(x=70,y=160,width=427,height=31)

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
        GButton_78["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_78["font"] = ft
        GButton_78["fg"] = "#000000"
        GButton_78["justify"] = "center"
        GButton_78["text"] = "Рассчитать закупочный лист"
        GButton_78.place(x=70,y=230,width=427,height=34)
        GButton_78["command"] = self.GButton_78_command

    def GButton_78_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
