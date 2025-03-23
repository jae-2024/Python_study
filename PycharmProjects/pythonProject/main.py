from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def back_forwards():
    tim.backward(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(back_forwards, "s")
screen.onkey(clear, "c")
screen.exitonclick()