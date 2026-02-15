from tkinter import*
from tkinter import messagebox
from tkinter.filedialog import*
root = Tk()
root.title("Address Book")
root.geometry("400x400")
root.config(background = "light green")
Label1 = Label(root, text = "My Address Book", fg = "black")
Label2 = Label(root, text = "Name", fg = "black")
Label3 = Label(root, text = "Address", fg = "black")
Label4 = Label(root, text = "Mobile", fg = "black")
Label5 = Label(root, text = "Email", fg = "black")
Label6 = Label(root, text = "Birthday", fg = "black")
Dictionary = {}
def open():
    GHI = askopenfile(defaultextension = ".txt")
    if GHI == "":
        messagebox.showinfo("Error","Select a file. Or we can't open your work.")
    else:
        global Dictionary
        Dictionary = eval(GHI.read())
        for j in Dictionary:
            Listbox1.insert(END, j)
Button1 = Button(root, text = "Open",bd = 4, fg = "black", command = open)
def edit():
    v = Listbox1.curselection()
    w = Listbox1.get(v)
    x = Dictionary[w]
Button2 = Button(root, text = "Edit",bd = 4, fg = "black")
def delete():
    Index = Listbox1.curselection()
    if Index:
        del Dictionary[Listbox1.get(Index)]
        Listbox1.delete(Index)
        dele()
def dele():
    Entry1.delete(0, END)
    Entry2.delete(0, END)
    Entry3.delete(0, END)
    Entry4.delete(0, END)
    Entry5.delete(0, END)
Button3 = Button(root, text = "Delete",bd = 4, fg = "black", command = delete)
def Update():
    ABC = Entry1.get()
    if ABC == "":
        messagebox.showinfo("Error", "You NEED to enter your name, or this won't work?!")
    else:
        if ABC not in Dictionary.keys():
            Listbox1.insert(END, ABC)
            Dictionary[ABC] = (Entry2.get(), Entry3.get(), Entry4.get(), Entry5.get())
            print(Dictionary)
            dele()
Button4 = Button(root, text = "Update/Add",bd = 4, fg = "black", command = Update)
def save():
    DEF = asksaveasfile(defaultextension = ".txt")
    if DEF == "":
        messagebox.showinfo("Error", "Add a title. Or we can't accept your work") 
    else:
        print(Dictionary, file = DEF)
        Dictionary.clear()
        Listbox1.delete(0,END)
Button5 = Button(root, text = "Save",bd = 4, fg = "black", command = save)
Listbox1 = Listbox(root, width = 20, height = 15, background = "white")
Entry1 = Entry(root, width = 30)
Entry2 = Entry(root, width = 30)
Entry3 = Entry(root, width = 30)
Entry4 = Entry(root, width = 30)
Entry5 = Entry(root, width = 30)
Label1.grid(row = 0, column = 0)
Label2.place(x = 250, y = 50)
Entry1.place(x = 250, y = 75)
Label3.place(x = 250, y = 100)
Entry2.place(x = 250, y = 125)
Label4.place(x = 250, y = 150)
Entry3.place(x = 250, y = 175)
Label5.place(x = 250, y = 200)
Entry4.place(x = 250, y = 225)
Label6.place(x = 250, y = 250)
Entry5.place(x = 250, y = 275)
Button1.place(x = 0, y = 350)
Button2.place(x = 75, y = 350)
Button3.place(x = 150, y = 350)
Button4.place(x = 225, y = 350)
Button5.place(x = 330, y = 350)
Listbox1.place(x = 0, y = 50)
root.mainloop()