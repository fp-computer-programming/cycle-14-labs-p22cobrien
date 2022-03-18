# Author: CMOB 3/18/2022

import turtle

window = turtle.Screen()
turtl = turtle.Turtle()

window.setup(500, 500)
window.screensize(450,450)
window.title("Lab 3")
window.bgcolor("gray")

turtl.shape('turtle')
turtl.color("cyan")

turtl.left(180)
for x in range(3):
    turtl.forward(200)
    turtl.left(120)

window.mainloop()
