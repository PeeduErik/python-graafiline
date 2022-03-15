#Peedu Erik Pajo
#ÜL05
#15.03.2022

from tkinter import *

def arvutamine():
    protsent=var.get()
    kokku=sisestus.get()
    print(protsent,kokku)
    
    
aken = Tk()
aken.title('ÜL05')
aken.geometry("300x300")

silt = Label(aken, text="Hind käibemaksuta:")
silt.grid(row=0,column=0)


sisestus = Entry(aken)
sisestus.grid(row=0,column=1)


nupp1 = Button(aken, text="Arvuta", width=10, command=arvutamine)
nupp1.grid(row=3, column=1)

def naita_valikut():
    print(var.get())

var = IntVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=0.09, command=naita_valikut)
valikukast.grid(row=1,column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=0.2, command=naita_valikut)
valikukast.grid(row=2,column=1)

jah = Label(aken, text="---------------------------------------------")
jah.grid(row=4,columnspan=3)
valjund = Label(aken, text="Siia tuleb käibemaks: ")
valjund.grid(row=5,columnspan=3)
valjund1 = Label(aken, text="Hind käibemaksuga: ")
valjund1.grid(row=6,columnspan=3)





aken.mainloop()


