from tkinter import*
root = Tk()
root.title("Warriors Books'")
root.geometry("400x600")
root.configure(background = "silver")
Scroll1 = Scrollbar(root)
Scroll1.pack(side = RIGHT, fill = Y)
Listbox1 = Listbox(root, width = 25, height = 10, background = "dark gray", yscrollcommand = Scroll1.set)

for j in range(120):
    Listbox1.insert(END, j)

Listbox1.pack()
Scroll1.config(command = Listbox1.yview)
root.mainloop()