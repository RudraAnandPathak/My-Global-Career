import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Dragon Curve Fractal")

t = turtle.Turtle()
t.speed(100)
t.color("cyan")
t.pensize(2)
t.hideturtle()

# Position the turtle
t.penup()
t.goto(-150, 0)
t.pendown()

def dragon(length, depth, sign):
    if depth == 0:
        t.forward(length)
    else:
        dragon(length, depth - 1, 1)
        t.right(90 * sign)
        dragon(length, depth - 1, -1)
        t.left(90 * sign)

# Draw the dragon curve
dragon(8, 12, 1)

turtle.done()
