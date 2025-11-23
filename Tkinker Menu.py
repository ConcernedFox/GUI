from tkinter import*
Earth = Tk()
Earth.title("Menu")
Earth.geometry("400x400")
Earth.configure(background = "silver")

Mercury = Menu(Earth)
Venus = Menu(Mercury)
Mercury.add_cascade(label = "File", menu = Venus)
Venus.add_command(label = "New File", command = None)
Earth.config(menu = Mercury)
Earth.mainloop()