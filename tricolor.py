import turtle

# Create a turtle object
screen = turtle.Screen()
t = turtle.Turtle()

# Set up the screen
screen.bgcolor("white")
t.speed(10)

# Draw the top saffron rectangle
t.penup()
t.goto(-180, 60)
t.pendown()
t.color("orange")
t.begin_fill()
t.forward(360)
t.right(90)
t.forward(40)
t.right(90)
t.forward(360)
t.right(90)
t.forward(40)
t.end_fill()

# Draw the middle white rectangle
t.left(90)
t.penup()
t.goto(-180, 20)
t.pendown()
t.color("white")
t.begin_fill()
t.forward(360)
t.right(90)
t.forward(40)
t.right(90)
t.forward(360)
t.right(90)
t.forward(40)
t.end_fill()

# Draw the bottom green rectangle
t.left(90)
t.penup()
t.goto(-180, -20)
t.pendown()
t.color("green")
t.begin_fill()
t.forward(360)
t.right(90)
t.forward(40)
t.right(90)
t.forward(360)
t.right(90)
t.forward(40)
t.end_fill()

# Draw the Ashoka Chakra (blue wheel)
t.penup()
t.goto(0, 2)
t.pendown()
t.color("navy")
t.circle(20)

# Draw the 24 spokes of the Ashoka Chakra
t.penup()
t.goto(-20, 2)
t.pendown()
for i in range(24):
    t.forward(20)
    t.backward(20)
    t.left(20)

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()