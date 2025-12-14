from tkinter import*
from time import strftime
root = Tk()
root.title("Tkinker Clock")
root.geometry("400x400")
root.configure(background = "red")
def time():
    Time = strftime("%H:%M:%S %p")
    Cell.config(text = Time)
    Cell.after(1000,time)
Cell = Label(root, fg = "black", font = ("Comic Sans MS", 40, "bold"))
Cell.pack()
time()
root.mainloop()