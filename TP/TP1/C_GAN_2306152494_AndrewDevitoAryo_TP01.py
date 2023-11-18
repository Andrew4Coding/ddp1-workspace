# NAMA  : Andrew Devito Aryo
# NPM   : 2306152494

# Membuat Tower Mario

# Mengimport Turtle
import turtle as t, random as r
from tkinter import messagebox

# Setup Turtle
t.title("Andrew Devito Aryo - 2306152494 - TP 1 - DDP 1")
t.speed(0)

# Set Background Color ke Biru Langit
t.Screen().bgcolor('sky blue')
t.Screen().setup(1.0, 1.0)

# Membuat rumput / ground
t.fillcolor('#82CD47')
t.begin_fill()
t.penup()
t.goto(-1000, -100)
t.pendown()
for i in range(2):
    t.forward(2000)
    t.right(90)
    t.forward(400)
    t.right(90)
t.end_fill()

# Meminta Input dari User

# Setiap While dan Else digunakan untuk memvalidasi float / integer dari input
jumlah_tower = t.numinput("Jumlah Tower", "Masukkan jumlah tower yang ingin dibuat (Harap masukkan Integer, min 1)", minval=1)
while not (jumlah_tower.is_integer()):
    messagebox.showerror('Float Error', 'Angka yang dimasukkan tidak boleh float')
    jumlah_tower = t.numinput("Jumlah Tower", "Masukkan jumlah tower yang ingin dibuat (Harap masukkan Integer, min 1)", minval=1)
else:
    jumlah_tower = int(jumlah_tower)

selisih_tinggi_tower = 0
jarak_antar_tower = 0

# Jika Jumlah Tower yang Diinginkan Lebih dari 1, maka akan meminta input jarak antar tower dan selisih tinggi
if jumlah_tower != 1:
    jarak_antar_tower = t.numinput("Jarak Antar Tower", "Masukkan jarak antar tower (Harap masukkan Integer, min 2, max 5)", minval=2, maxval=5, default=2)
    while not (jarak_antar_tower.is_integer()):
        messagebox.showerror('Float Error', 'Angka yang dimasukkan tidak boleh float')
        jarak_antar_tower = t.numinput("Jarak Antar Tower", "Masukkan jarak antar tower (Harap masukkan Integer, min 2, max 5)", minval=2, maxval=5, default=2)
    else:
        jarak_antar_tower = int(jarak_antar_tower)

    selisih_tinggi_tower = t.numinput("Selisih Jumlah Layer", "Masukkan selisih jumlah lapisan pada setiap tower (Harap masukkan Integer, min 2, max 5)", minval=2, maxval=5, default=2)
    while not (selisih_tinggi_tower.is_integer()):
        messagebox.showerror('Float Error', 'Angka yang dimasukkan tidak boleh float')
        selisih_tinggi_tower = t.numinput("Selisih Jumlah Layer", "Masukkan selisih jumlah lapisan pada setiap tower (Harap masukkan Integer, min 2, max 5)", minval=2, maxval=5, default=2)
    else:
        selisih_tinggi_tower = int(selisih_tinggi_tower)

lebar_bata = t.numinput("Lebar Batu Bata", "Masukkan lebar batu bata (Harap masukkan Integer, max 35)", minval=1, maxval=35, default=30)
while not(lebar_bata.is_integer()):
    messagebox.showerror('Float Error', 'Angka yang dimasukkan tidak boleh float')
    lebar_bata = t.numinput("Lebar Batu Bata", "Masukkan lebar batu bata (Harap masukkan Integer, max 35)", minval=1, maxval=35, default=30)
else:
    lebar_bata = int(lebar_bata)

tinggi_bata = t.numinput("Tinggi Batu Bata", "Masukkan tinggi batu bata (Harap masukkan Integer, max 25)", minval=1, maxval=25, default=20)
while not (tinggi_bata.is_integer()):
    messagebox.showerror('Float Error', 'Angka yang dimasukkan tidak boleh float')
    tinggi_bata = t.numinput("Tinggi Batu Bata", "Masukkan tinggi batu bata (Harap masukkan Integer, max 25)", minval=1, maxval=25, default=20)
else:
    tinggi_bata = int(tinggi_bata)

tinggi_tower = t.numinput("Banyak Lapisan Tower Pertama", "Masukkan banyak lapisan untuk tower pertama (Harap masukkan Integer, min 1, max 25)", minval=1, maxval=25, default=3)
while not (tinggi_tower.is_integer()):
    messagebox.showerror('Float Error', 'Angka yang dimasukkan tidak boleh float')
    tinggi_tower = t.numinput("Banyak Lapisan Tower Pertama", "Masukkan banyak lapisan untuk tower pertama (Harap masukkan Integer, min 1, max 25)", minval=1, maxval=25, default=3)
else:
    tinggi_tower = int(tinggi_tower)

lebar_tower = t.numinput("Lebar Badan Tower", "Masukkan lebar badan tower (Harap masukkan Integer, max 10)", minval=1, maxval=10, default=3)
while not (lebar_tower.is_integer()):
    messagebox.showerror('Float Error', 'Angka yang dimasukkan tidak boleh float')
    lebar_tower = t.numinput("Lebar Badan Tower", "Masukkan lebar badan tower (Harap masukkan Integer, max 10)", minval=1, maxval=10, default=3)
else:
    lebar_tower = int(lebar_tower)

# Deklarasi variable Counter untuk menghitung jumlah batu bata yang dipakai
jumlah_bata = 0

# Agar Graphic berada di tengah Layar
xstart = -(jumlah_tower * (lebar_tower * lebar_bata  + jarak_antar_tower * lebar_bata) - jarak_antar_tower*lebar_bata) / 2

# Membuat turtle menuju posisi koordinat yang diinginkan
t.penup()
t.goto(xstart, -150)
t.pendown()

# Membuat tower sesuai jumlah yang diinginkan
for i in range(jumlah_tower):
    # Membuat tumpukan bata sesuai dengan tinggi tower yang diinginkan
    for j in range(tinggi_tower + i * selisih_tinggi_tower + 1):
        t.fillcolor("#CA7F65")
        adder = 0
        # Jika turtle sudah mencapai puncak tower, maka:
        if j == (tinggi_tower + i * selisih_tinggi_tower):
            t.fillcolor("#693424")
            t.goto(t.xcor() - lebar_bata/2, t.ycor())
            # Variable adder akan di set menjadi 1, untuk menambah jumlah bata pada kepala tower
            adder = 1
        t.begin_fill()
        
        # Membuat deretan bata sesuai dengan lebar tower yang diinginkan
        for _ in range(lebar_tower + adder):
            # Membuat sebuah batu bata
            for _ in range(2):
                t.forward(lebar_bata)
                t.left(90)
                t.forward(tinggi_bata)
                t.left(90)
            t.forward(lebar_bata)
            jumlah_bata += 1
        
        t.end_fill()
        t.penup()
        t.goto(t.xcor() - lebar_bata*lebar_tower, t.ycor() + tinggi_bata)
        t.pendown()

    # MEMBUAT KOMPONEN JAMUR
    # Setup awal posisi dan warna
    t.forward(((lebar_tower - 2) * lebar_bata) / 2)
    t.fillcolor('#F2F7A1')
    t.begin_fill()

    # Membuat badan Jamur
    for _ in range(6):
        t.forward(lebar_bata)
        t.left(90)
    t.end_fill()

    # Membuat kepala Jamur
    # Warna kepala jamur
    warna_kepala = r.choice(['red', '#004225', '#F39F5A', '#AE445A'])
    t.fillcolor(warna_kepala)
    
    t.begin_fill()
    t.left(180)
    t.forward(lebar_bata / 2)
    t.left(90)
    t.circle(lebar_bata, 180)

    t.penup()
    t.left(90)
    t.forward(lebar_bata / 2)
    t.end_fill()
    t.forward(0.3 * lebar_bata)
    t.right(90)
    t.forward(0.5 * lebar_bata)
    t.left(90)
    t.fillcolor('black')
    t.pendown()
    t.begin_fill()

    # Membuat Mata Jamur
    t.circle(0.1 * lebar_bata)
    t.forward(0.4 * lebar_bata)
    t.circle(0.1 * lebar_bata)
    t.end_fill()

    # Setup Posisi untuk persiapan membuat tower selanjutnya
    t.penup()
    t.color("black")
    xstart += (lebar_tower * lebar_bata) + (jarak_antar_tower*lebar_bata)
    t.goto(xstart, -150)
    t.pendown()

t.penup()
t.goto(0, -250)
t.pendown()

# Mengeluarkan tulisan berupa jumlah tower dan jumlah batu bata yang digunakan
t.write(f"{jumlah_tower} Mario's Tower berhasil dibuat dengan {jumlah_bata} bata", False, align='center', font=('Arial', 16, 'bold'))
t.hideturtle()
t.done()