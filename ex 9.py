import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Spiral Flower")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

# Use RGB colors
turtle.colormode(1.0)

# Draw the pattern
h = 0
for i in range(360):
    color = colorsys.hsv_to_rgb(h, 1, 1)
    t.pencolor(color)
    h += 0.005

    t.forward(i)
    t.left(59)

turtle.done()
