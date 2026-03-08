from tkinter import*
from tkinter.filedialog import*
root = Tk()
root.title(" City Book Management ")
root.geometry("400x400")
root.config(background = "white")
Label1 = Label(root, text = "City Book Management", fg = "White")
Label2 = Label(root, text = "Book Title", fg = "White")
Entry1 = Entry(root, width = 30)
Label3 = Label(root, text = "Author", fg = "White")
Entry2 = Entry(root, width = 30)
Label4 = Label(root, text = "Book in Series")
Entry3 = Entry(root, width = 30)
def add():
    Listbox1.insert(END,Entry1.get() + ", by " + Entry2.get() + ", Book " + Entry3.get())
    Entry1.delete(0, END)
    Entry2.delete(0, END)
    Entry3.delete(0, END)
def issue():
    Index = Listbox1.curselection()
    if Index:
        Listbox1.delete(Index)
        Listbox1.insert(Index, "Unavailable")
def send():
    Index = Listbox1.curselection()
    if Index:
        Listbox1.delete(Index)
        Listbox1.insert(END,Entry1.get() + ", by " + Entry2.get() + ", Book " + Entry3.get())
def save():
    Save1 = asksaveasfile(defaultextension = ".txt")
    if Save1 is not None:
        for l in Listbox1.get(0,END):
            print(l, file = Save1)
        Listbox1.delete(0,END)
Button1 = Button(root, text = "Add book", bd = 4, fg = "black", command = add)
Button2 = Button(root, text = "Issue book", bd = 4, fg = "black", command = issue)
Button3 = Button(root, text = "Return book", bd = 4, fg = "black", command = send)
Button4 = Button(root, text = "Save", bd = 4, fg = "black", command = save)
Listbox1 = Listbox(root, width = 45, height = 10, background = "silver")
Label1.place(x = 50, y = 0)
Label2.place(x = 75, y = 25)
Label3.place(x = 75, y = 50)
Label4.place(x = 75, y = 75)
Entry1.place(x = 175, y = 25)
Entry2.place(x = 175, y = 50)
Entry3.place(x = 175, y = 75)
Button1.place(x = 0, y = 100)
Button2.place(x = 100, y = 100)
Button3.place(x = 200, y = 100)
Button4.place(x = 300, y = 100)
Listbox1.place(x = 0, y = 150)
root.mainloop()