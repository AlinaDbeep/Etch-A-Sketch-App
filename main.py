from turtle import Turtle, Screen

tim = Turtle()
tim.pensize(2)
screen = Screen()


def up():
    tim.setheading(90)
    tim.forward(10)

def down():
    tim.setheading(270)
    tim.forward(10)

def left():
    tim.setheading(180)
    tim.forward(10)

def right():
    tim.setheading(0)
    tim.forward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(clear, "c")


screen.exitonclick()