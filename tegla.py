from tkinter import*

abl1 = Tk()

def ujablak():
    abl2 = Toplevel(abl)
    uz2 = Message(abl2, text="Készítette: Milánkovics Sámuel", width=300)
    gomb2 = Button(abl2,Text="Kilép", command = abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()

szoveg1 = Label(abl1, text="Kattints a gombra!")
gomb1 = Button(abl1, text="Névjegy", command=ujablak)

szoveg1.pack()
gomb1.pack()

abl1.mainloop()