import turtle
import colorsys

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Moving Spiral")

turtle_speed = 0  # Adjust this value to change the drawing speed
num_circles = 100  # Number of circles in the spiral
circle_spacing = 5  # Distance between circles
max_radius = 500  # Maximum radius of the spiral
hue_offset = 0.01  # Hue change per circle

# Function to draw a single circle
def draw_circle(radius, hue):
    turtle.color(colorsys.hsv_to_rgb(hue, 1.0, 1.0))
    turtle.circle(radius)

# Function to draw the entire spiral
def draw_spiral():
    for i in range(num_circles):
        hue = (i * hue_offset) % 1.0
        radius = max_radius - i * circle_spacing
        turtle.penup()
        turtle.sety(-radius)  # Move to the starting position for the circle
        turtle.pendown()
        draw_circle(radius, hue)

# Initialize the turtle
turtle.speed(turtle_speed)
turtle.pensize(2)

# Draw the spiral
draw_spiral()

# Exit on click
turtle.done()
