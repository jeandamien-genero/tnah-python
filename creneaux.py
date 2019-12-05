#Ce code permet de dessiner des créneaux en utilisant turtle. 
#Il a été réalisé par Jean-Damien Généro dans le cadre d'un cours du master TNAH de l'École nationale des chartes en 2019.

monter = 150
haut = 50
bas = 20

def debut():
    t.forward(300)
    t.left(90)
    t.forward(300)

def creneau():
    t.left(90)
    t.forward(haut)
    t.left(90)
    t.forward(bas)
    t.right(90)
    t.forward(haut)
    t.right(90)
    t.forward(bas)

def fin():
    t.left(90)
    t.forward(haut)
    t.left(90)
    t.forward(300)
    t.left(90)
    t.forward(haut)

import turtle
t = turtle.Turtle()
t.speed(6)
t.color("grey", "green")

t.begin_fill()

debut()
for a in range(5):
    creneau()
fin()

t.end_fill()

turtle.done()