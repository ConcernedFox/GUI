from tkinter import*
from tkinter.ttk import *
root = Tk()
root.title("Multiplication Tables")
root.geometry("400x1000")
root.config(background = "White")
Label1 = Label(root, text = "Multiplication Tables")
Label2 = Label(root)
def generate():
    X = ""
    for i in range(On_se_Moque.get()):
        X += str(Minimum_Ca.get()) + "   X   " + str(i+1) + "   =   " + str((Minimum_Ca.get())*(i+1)) + "\n"
    Mon_Regarde.configure(text = X)
Button1 = Button(root, text = "Generate", command = generate)
Minimum_Ca = IntVar()
Sois_pas_Timide = Combobox(root, textvariable = Minimum_Ca, width = 5)
Sois_pas_Timide["values"] = tuple(range(31))
On_se_Moque = IntVar()
r1 = Radiobutton(root, text = "10", variable = On_se_Moque, value = 10)
r2 = Radiobutton(root, text = "20", variable = On_se_Moque, value = 20)
r3 = Radiobutton(root, text = "30", variable = On_se_Moque, value = 30)
On_se_Moque.set(10)
Label1.place(x = 25, y = 100)
Sois_pas_Timide.place(x = 180, y = 100)
r1.place(x = 250, y = 100)
r2.place(x = 250, y = 130)
r3.place(x = 250, y = 160)
Button1.place(x = 160, y = 200)
Mon_Regarde = Label(root)
Mon_Regarde.place(x = 160, y = 250)
root.mainloop()