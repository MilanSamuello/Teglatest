from tkinter import *

class Aru():
    def __init__ (self, areNev, aruEgysegar, mennyiseg):
        self.aruNev = aruNev
        self.aruEgysegar = aruEgysegar
        self.mennyiseg = mennyiseg

    def aruEgysegar(self, aruEgysegar):
        if aruEgysegar >0:
            self.aruEgysegar = aruEgysegar

    def getAru(self):
        return self.mennyiseg * self.aruEgysegar

    def hozzatesz (self, aruMennyiseg):
        if mennyiseg > 0:
            self.mennyiseg = self.mennyiseg + aruMennyiseg

    def __doc__ (self):
        mezo1.delete(0, END)
        mezo1.insert(0, self.aruNev+"Egységár:" +str(self.aruEgysegar)+"Mennyiség:" "+str(self.menny)+Ár"+str(self.getAru()))

    ar = Aru("Paradicsom", 300)

    def bevezetes():
        
        def rogzit():
            mennyiseg = eval(m1.get())
            ar.hozzatesz(menny)
            ar.__doc__()
            abl2.destroy()

        abl2 = Toplevel(foablak)
        abl2.title("Bevételezés")
        abl2.minsize(width = 300, height = 100)
        sz1 = Label(abl2, text = "Mennyiség:")
        g1 = Button(abl2, text = "Rögzít", command = rogzit)
        m1 = Entry(abl2)
        sz1.grid(row = 1)
        g1.grid(row = 2, column = 2, sticky = W)
        m1.grid(row = 1, column = 2, sticky = W)

    def kivitelezes():

        def rogzit():
            menny= eval(m1.get())
            ar.elvesz(menny)
            ar.__doc__()
            abl3.destroy()

        abl3 = Toplevel(foablak)
        abl3.title("Kivitelezés")
        abl.minsize(width = 300, height = 100)
        sz1 = Label(abl3, text = "Mennyiség:")
        g1 = Button(abl3, text = "Rögzít", command = rogzit)
        m1 = Entry(abl3)
        sz1.grid(row = 1)
        g1.grid(row = 2, column = 2, sticky = W)
        m1.grid(row = 1, column = 2, sticky = W)
        abl3.mainloop()


    def rogzit():
        ujar = eval(m1.get())
        aru.__doc__()
        abl4.destroy()

    abl4 = Toplevel(foablak)
    abl4.title("Árváltozás")
    abl4.minsize(width = 300, height = 100)
    sz1 = Label(abl4, text = "Új ár:")
    g1 = Button(abl4, text = "Rögzít", command = rogzit)
    m1 = Entry(abl4)
    sz1.grid(row = 1)
    g1.grid(row = 2, column = 2, sticky = W)
    m1.grid(row = 1, column = 2, sticky = W)
    
    abl4.mainloop()

foablak = Tk()
foablak.title("Raktárprogram")
foablak.minsize(width = 400, height = 100)

menusor = Frame(foablak)
menusor.pack(side = TOP, fill = X)

menu1 = Menubutton(menusor, text = "Lehetségek", underline = 0)
menu1.pack(side = LEFT)
fajl = Menu(menu1)
fajl.add_command(label ="Bevételezés", command = bevetelezes, underline = 0)
fajl.add_command(label ="Kivitelezés", command = kivitelezes, underline = 0)
fajl.add_command(label ="Árváltoztatás", command = arvaltoztatas, underline = 0)