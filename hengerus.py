from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = int(mezo3.get())

    d = 3.14 * b * b * c 
    x = d / 100
    mezo4.delete(0, END)
    mezo4.insert(0, str(round(x))+" liter")
    
    s = d / a / 50
    mezo5.delete(0, END)
    mezo5.insert(0, str(round(s))+" bor")
    mezo6.delete(0, END)
    mezo6.insert(0, str()+" igen")

foablak=Tk()
cimke=Label(foablak, text="SZIA URAM!", fg="black")
cimke.pack()
cimke=Label(foablak, text="", fg="black")
cimke.pack()
cimke=Label(foablak, text="bor mennyisége (liter):", fg="black")
cimke.pack()
mezo1=Entry(foablak)
mezo1.pack()
cimke=Label(foablak, text="Hordó magassága (cm):", fg="black")
cimke.pack()
mezo2=Entry(foablak)
mezo2.pack()
cimke=Label(foablak, text="Hordó szélessége (cm):")
cimke.pack()
mezo3=Entry(foablak)
mezo3.pack()
gomb4=Button(foablak, text="Kiszámítás", command=osszeg,)
gomb4.pack()
cimke=Label(foablak, text="Ennyi literes a hordó:", fg="black")
cimke.pack()
mezo4=Entry(foablak)
mezo4.pack()
cimke=Label(foablak, text="Ennyi bor fér bele:", fg="black")
cimke.pack()
mezo5=Entry(foablak)
mezo5.pack()
mezo6=Entry(foablak)
mezo6.pack()

foablak.mainloop()