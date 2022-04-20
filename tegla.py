from tkinter import *

ablak1=Tk()
ablak1.title("A téglatest adatai")
ablak1.minsize(width=300, height=100)

def ujablak():

    ablak2=Toplevel(ablak1)
    ablak2.title("Eredmények")
    ablak2.minsize(width=300, height=100)
    sz1=Label(ablak2,text="Felszín:")
    sz2=Label(ablak2,text="Térfogat:")
    m1=Entry(ablak2)
    m2=Entry(ablak2)

sz1.grid(row=1)
sz2.grid(row=2)
m1.grid(row=1,column=2,sticky=W)
m2.grid(row=2,column=2,sticky=W)

a=eval(mezo1.get())
b=eval(mezo2.get())
c=eval(mezo3.get())

Felszín=2*(a*b+a*c+b*c)
Térfogat=a*b*c

m1.delete(0,END)
m1.insert(0,str(Felszín))
m2.delete(0,END)
m2,insert(0,str(terfogat))

ablak2.mainloop()


sz1=Label(ablak2,text="Felszín:")
sz2=Label(ablak2,text="Térfogat:")
m1=Entry(ablak2)
m2=Entry(ablak2)

#laptördelés a "grid" segítségével:

sz1.grid(row=1)
sz2.grid(row=2)
m1.grid(row=1,column=2,sticky=W)
m2.grid(row=2,column=2,sticky=W)

a=eval(mezo1.get())
b=eval(mezo2.get())
c=eval(mezo3.get())

Felszín=2*(a*b+a*c+b*c)
Térfogat=a*b*c

m1.delete(0,END)
m1.insert(0,str(Felszín))
m2.delete(0,END)
m2,insert(0,str(terfogat))

ablak2.mainloop()

#a widgetek létrehozása:

szoveg1=Label(ablak1,text="a")
szoveg2=Label(ablak1,text="b")
szoveg2=Label(ablak1,text="c")
gomb1=grid(row=4,column=2,sticky=W)
mezo1=grid(row=1,column=2,sticky=W)
mezo2=grid(row=2,column=2,sticky=W)
mezo3=grid(row=3,column=2,sticky=W)

#indítás:

ablak1.mainloop()