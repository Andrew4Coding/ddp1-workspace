# IMPORT TURTLE
import turtle, random, math

# INISIASI TURTLE
pencil = turtle.Turtle()
pencil.speed(0)
turtle.delay(0)

r = 10
stack = 25
segi = 40
sudut_dalam = 360 / segi
sudut_sisi = (180 - sudut_dalam) / 2
turn = 180 - sudut_sisi

def create_segment(radius, i):
    pencil.forward(radius)
    pencil.left(turn)
    sisi = math.sin(math.radians(sudut_dalam / 2))*radius*2*i
    pencil.forward(sisi)
    pencil.left(turn)
    pencil.forward(radius)
    pencil.right(180)
    
def pick_random_color():
    list_warna = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "black"]
    randomizer = random.randrange(0, len(list_warna), 1)
    return list_warna[randomizer]

if __name__ == "__main__":
        jumlah_segmen = 0
        for i in range(1, stack+1, 1):  
            for j in range(segi):
                pencil.fillcolor(pick_random_color())
                pencil.color(pick_random_color())
                pencil.begin_fill()
                create_segment(r, i)
                jumlah_segmen += 1
                pencil.end_fill()     
            pencil.forward(r)    
        pencil.penup()
        pencil.goto(300, -250)
        pencil.down()
        pencil.write(f"Jumlah Segmen: {jumlah_segmen}")
turtle.done()