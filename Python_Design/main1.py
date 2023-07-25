import turtle
import random

# Set up the turtle
t = turtle.Turtle()
turtle.bgcolor("black")
t.speed(0)
t.width(1)

# Define colors
colors = ["white", "yellow", "orange", "red", "pink", "purple", "blue", "green"]

# Draw the galaxy
for i in range(1000):
    color = random.choice(colors)
    t.color(color)
    t.forward(i)
    t.right(91)
    if i % 10 == 0:
        t.circle(i // 10)

# Keep the turtle window open
turtle.mainloop()

print(10, 20,50, sep=' - ')


