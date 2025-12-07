from tkinter import*


Luke = Tk()


Luke.title("Celsuis - Farenhait")
Luke.geometry("400x400")
Luke.configure(background = "light green")
Anakin = Label(Luke, text = "Celsuis", fg = "black")
ObiWan = Entry(Luke, width = "100")
def Convert():
    Han = float(ObiWan.get())*1.8+32
    print(Han)
    ObiWan.insert(END, Han)

Yoda = Button(Luke, text = "Convert to Farenhait - Part 1", bd = 4, fg = "black", command = Convert)

Anakin.place(x = 150, y = 75)
ObiWan.place(x = 250, y = 75)
Yoda.place(x = 150, y = 175)

Luke.mainloop()