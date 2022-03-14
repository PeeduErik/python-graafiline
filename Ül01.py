#Peedu Erik Pajo
#Ül 01
#14.03.2022

import turtle
import random


#akna seaded
aken = turtle.Screen()
aken.setup(300,300)
aken.title("ÜL01")

colors = ("blue", "orange", "red", "green")
turn = 0
spikes = 8
size = 10

for i in range(spikes):
    kk = turtle.Turtle()
    kk.color(random.choice(colors))
    kk.left(turn)
    kk.forward(100)
    turn+=45
    


#kolmnurk

kk2 = turtle.Turtle()
for i in range(spikes):
    kk2.color(random.choice(colors))
    kk2.forward(100)
    kk2.left
    turn+=45
 

turtle.exitonclick()

 
