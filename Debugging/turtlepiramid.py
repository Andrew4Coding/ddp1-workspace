# IMPORT TURTLE
import turtle, random

# INISIASI TURTLE
area = turtle.Screen()
area.bgcolor("gray")
pencil = turtle.Turtle()
pencil.speed(0)

# SET X,Y START POSITION
xstart = -450; ystart = -300
box_sum = 0

pencil.penup()
pencil.setpos(xstart, ystart)
pencil.pendown()
pencil.write("Hello world")

# SQUARE WIDTH
boxwidth = 40

n = 20
def create_square():
    for i in range(2):
        pencil.forward(boxwidth)
        pencil.left(90)
        pencil.forward(boxwidth/2)
        pencil.left(90)
    pencil.forward(boxwidth)

def fill_color_border(color):
    pencil.fillcolor(color)
    pencil.begin_fill()
    
def pick_random_color():
    list_warna = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "black", "white"]
    randomizer = random.randrange(0, len(list_warna), 1)
    return list_warna[randomizer]

if __name__ == "__main__":
    for i in range(0, n, 1):
        for j in range(n-i):
            if (j == 0 or j == (n-i - 1)):
                fill_color_border("brown")
            elif (i == 0):
                fill_color_border("brown")
            else:
                fill_color_border(pick_random_color())
            
            create_square()
            box_sum += 1
            pencil.end_fill()

        pencil.penup()
        xstart += boxwidth/2; ystart += boxwidth/2
        pencil.setpos(xstart, ystart)
        pencil.pendown()

    pencil.penup()
    pencil.goto(500 , -300)
    pencil.pendown
    pencil.write(f"Jumlah kotak: {box_sum}")
    turtle.done()