# Author: CMOB 3/21/2022

import turtle

def move_forward():
    turtl.forward(50)

def move_backward():
    turtl.backward(50)

def turn_right():
    turtl.right(90)

def turn_left():
    turtl.left(90)


window = turtle.Screen()
turtl = turtle.Turtle()

window.onkey(move_forward, "Up")
window.onkey(move_backward, "Down")
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")

window.listen()


window.onkey




window.mainloop()
