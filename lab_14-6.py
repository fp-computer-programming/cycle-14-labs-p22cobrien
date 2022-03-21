# Author: CMOB 3/21/2022

import turtle

def fill_square():
    x = 0
    while x < 4:
        turtl.forward(100)
        turtl.right(90)
        x += 1


window = turtle.Screen()
turtl = turtle.Turtle()

color = turtle.textinput("Color",  "What color do you want.")
size = turtle.numinput("Size", "What is the Size? max 5, min 1", None, 1, 5)

window.setup()
window.screensize(200,200)
window.title("Lab 6")

turtl.color(color)
turtl.shapesize(size)



window.mainloop()