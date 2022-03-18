# Author: CMOB 3/18/2022

import turtle

window = turtle.Screen()
turtl = turtle.Turtle()

window.setup()
window.screensize()
window.title("Lab 4")

turtl.speed(0)
turtl.color("purple")
turtl.stamp()
turtl.fillcolor("blue")

turtl.hideturtle()

turtl.goto(100,0)

turtl.showturtle()

turtl.begin_fill()

turtl.goto(100,100)
turtl.goto(200,100)
turtl.goto(200,0)
turtl.goto(100,0)

turtl.end_fill()

window.mainloop()