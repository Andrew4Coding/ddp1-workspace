# IMPORT TURTLE
import turtle, random, math

# INISIASI TURTLE
area = turtle.Screen()
pencil = turtle.Turtle()
pencil.speed(10)

r = 10
segi = 20
sudut_dalam = 360 / segi
sudut_sisi = (180 - sudut_dalam) / 2
turn = 180 - sudut_sisi

def create_segment(radius):
    pencil.forward(radius)
    pencil.left(turn)

    sisi = math.sin(math.radians(sudut_dalam / 2))*radius*2
    pencil.forward(sisi)
    pencil.left(turn)
    pencil.forward(radius)
    pencil.right(180)

def create_next(radius, i):
    pencil.forward(radius)
    pencil.left(turn)

    sisi = math.sin(math.radians(sudut_dalam / 2))*radius*2*i
    pencil.forward(sisi)
    pencil.left(turn)
    pencil.forward(radius)
    pencil.right(180)

def pick_random_color():
    list_warna = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "black", "white"]
    randomizer = random.randrange(0, len(list_warna), 1)
    return list_warna[randomizer]

if __name__ == "__main__":
        for i in range(segi):
            pencil.fillcolor(pick_random_color())
            pencil.begin_fill()
            create_segment(r)
            r+=5
            pencil.end_fill()

        for a in range(2, 5, 1): 
            for j in range(segi):
                pencil.fillcolor(pick_random_color())
                pencil.begin_fill()
                create_next(r, a) 
                r+=5
                pencil.end_fill()
            pencil.forward(r)


turtle.done()