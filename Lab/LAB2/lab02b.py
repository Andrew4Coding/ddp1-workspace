## Author         : Andrew Devito Aryo
## File name      : lab02b.py
## using turtle to draw regular polygons
## prompt user for the number of sides and the color components (r,g,b)

# Import and Set up Turtle
import turtle
turtle.shape('turtle')
turtle.title('Lab 02')

# get the number of sides from user
n = int(turtle.textinput("Lab 02", "The number of sides: "))

# Move turtle pen to the left side of the window
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()

# draw the n-side polygon using a for loop
# the length of a side is getting shorter as n getting larger
# When n = 4, the length of a side is 100.

side_length = 360 / n
angle = 360 / n
if n == 4:
    side_length = 100
for i in range(n):
    # Turtle moves forward
    turtle.forward(side_length)

    # Turtle turns left 'angle' degrees
    turtle.left(angle)

# get the value of red color from user
r = float(turtle.textinput("Lab 02",
 "The red color component [between 0 and 1]: "))

# get the value of green color from user
g = float(turtle.textinput("Lab 02",
 "The green color component [between 0 and 1]: "))

# get the value of blue color from user
b = float(turtle.textinput("Lab 02",
 "The blue color component [between 0 and 1]: "))

# create the color from rgb values given by user
turtle.color(r, g, b)

# move the turtle to a new location
turtle.penup()
turtle.goto(200, 0)

# draw a regular polygon with n sides and color(r,g,b)
# use a for loop
turtle.begin_fill()

for i in range(n):
    turtle.forward(side_length)
    turtle.left(angle)

turtle.end_fill()

# make the turtle invisible
turtle.hideturtle()

# message for user
turtle.up()
turtle.goto(0,-100)
turtle.down()
turtle.color('blue')
turtle.write("Please click on the graphics window to exit ...",
 False, align='center', font=('Arial', 20, 'normal'))

# wait for user to click on the screen to exit
turtle.exitonclick()

# the end