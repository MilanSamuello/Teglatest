
from Tkinter import *

def nevjegy():
    abl2 = Toplevel(foablak)
    uz2 = Message(abl2, text = "Készítette: Milánkovics Sámuel")
    gomb2 = Button(abl2, text = "kilép", command = abl2.destroy)
    uz2.pack()
    gomb2.pack()
    abl2.mainloop()

def felszin():
    def szamit():
        a = eval(mezo1.get())
        a = eval(mezo2.get())
        a = eval(mezo3.get())
        felszin = 2*(a*b+a*c+b*c)
        mezo4.delete(0, END)
        mezo4.insert(0, str(felszin))

    abl3 = Toplevel(foablak)
    abl3.title("A téglatest felszíine")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")
    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

def terfogat():
    def szamit():
        a = eval(mezo1.get())
        a = eval(mezo2.get())
        a = eval(mezo3.get())
        terfogat = a*b*c
        mezo4.delete(0, END)
        mezo4.insert(0, str(terfogat))

    abl3 = Toplevel(foablak)
    abl3.title("A téglatest térfogata")
    abl3.minsize(width = 300, height = 100)
    szoveg1 = Label(abl3, text = "a:")
    szoveg2 = Label(abl3, text = "b:")
    szoveg3 = Label(abl3, text = "c:")
    szoveg4 = Label(abl3, text = "Eredmény:")

    gomb1 = Button(abl3, text = "Számítás", command = szamit)
    mezo1 = Entry(abl3)
    mezo2 = Entry(abl3)
    mezo3 = Entry(abl3)
    mezo4 = Entry(abl3)
    szoveg1.grid(row = 1)
    szoveg2.grid(row = 2)
    szoveg3.grid(row = 3)
    szoveg4.grid(row = 5)
    gomb1.grid(row = 4, column = 2, sticky = W)
    mezo1.grid(row = 1, column = 2, sticky = W)
    mezo2.grid(row = 2, column = 2, sticky = W)
    mezo3.grid(row = 3, column = 2, sticky = W)
    mezo4.grid(row = 5, column = 2, sticky = W)
    
    abl3.mainloop()

foablak = Tk()
foablak.title("A téglatest adatai")
foablak.minsize(width = 300, height = 100)