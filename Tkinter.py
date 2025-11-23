#Importing tkinter
from tkinter import*
#Creating the window
root = Tk()
#Creating the tile of the window
root.title("Star Wars")
#Creating the size of the window
root.geometry("400x400")
#Creating the color of the window
root.configure(background = "red")
#Creating a label
stalk = Label(root, text = "Username", bd = "4", fg = "blue")
stem = Label(root, text = "Password", bd = "4", fg = "blue")
#Creating a entry
flower = Entry(root, width = 30)
pollen = Entry(root, width = 30, show = "*")
#Creating a button
leaf = Button(root, text = "Submit", bd = "4", fg = "blue", command = root.destroy)
#Giving the button it's x and y coordinates
leaf.place(x = 150, y = 275)
#Giving the label it's x and y coordinates
stalk.place(x = 150, y = 75)
stem.place(x = 150, y = 175)
#Giving the entry it's x and y coordinates
flower.place(x = 260, y = 75)
pollen.place(x = 260, y = 175)
#Making sure the window doesn't close the second it opens
root.mainloop()