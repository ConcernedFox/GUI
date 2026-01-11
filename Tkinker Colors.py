from tkinter import*
from tkinter.filedialog import*
root = Tk()
root.title("Memorizer")
root.geometry("400x400")
root.config(background = "white")
Scroll1 = Scrollbar(root)
Listbox1 = Listbox(root, width = 25, height = 10, background = "silver", yscrollcommand = Scroll1.set)
for j in range:
    Listbox1.insert(END,j)