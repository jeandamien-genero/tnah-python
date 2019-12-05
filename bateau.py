#Ce code permet de dessiner un bâteau en utilisant turtle. 
#Il a été réalisé par Jean-Damien Généro dans le cadre d'un cours du master TNAH de l'École nationale des chartes en 2019.

import turtle
boat = turtle
boat.speed(3)
boat.color("blue")
boat.begin_fill()

boat.forward(150)
boat.left(45)
boat.forward(50)
boat.left(135)
boat.forward(188)
boat.right(90)
boat.forward(150)


boat.right(90)
boat.forward(50)
boat.right(90)
boat.forward(45)
boat.left(-90)
boat.forward(50)


boat.penup()
boat.right(-90)
boat.forward(105)
boat.pendown()


boat.left(-90)
boat.forward(188)
boat.left(130)
boat.forward(46)
boat.left(50)
boat.forward(170)

boat.end_fill()

boat.done()