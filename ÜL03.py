#Peedu Erik Pajo
#ÜL03
#15.03.2022


from tkinter import *


aken = Tk()
aken.title('ÜL03')
aken.configure(background='black')
kiri = "Peedu Erik Pajo \n IT21 \n 2022"
tekst = Label(aken, text=kiri,font="Tahoma 12",foreground="red", background="black")
tekst.pack()
aken.minsize(200,100)
aken.maxsize(800, 400)

aken.mainloop()



