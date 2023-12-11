from tkinter import *
from tkinter import messagebox 

class barcode(object):
    def __init__(self, window=None):
        window = Tk() # membuka window
        window.title("EAN-13 [by Dara Z. A.]") # judul window
        window.geometry('400x450') # ukuran window
        window.resizable(False, False) # agar main window tidak resizeable

        # meminta user melakukan input nama file .eps
        self.label_file = Label(window, 
                                text= "Save barcode to PS file [eg: EAN13.eps]:",
                                font=("Arial", 12, "bold"))
        self.filename = Entry(window, font=("Arial", 12))
        self.label_file.pack()
        self.filename.pack()
        self.filename.bind('<Return>', self.HandledError)

         # meminta user melakukan input code
        self.label_code = Label(window, 
                                text= "Enter code (first 12 decimal digits):",
                                font=("Arial", 12, "bold"))
        self.codec = Entry(window, font=("Arial", 12))
        self.label_code.pack()
        self.codec.pack()
        self.codec.bind('<Return>', self.HandledError)

        # menyiapkan canvas untuk menggambar barcode
        self.canvas = Canvas(window, height=305, width=355, bg= 'white')
        self.canvas.place(x=20, y=130)
        window.mainloop()

    def HandledError(self, event):
        self.canvas.delete("all") # menghapus barcode
        # menunjukkan error juka user bukan memasukkan file .eps
        if self.filename.get()[-4:] != ".eps":
            messagebox.showerror("ERROR!",
                                 "File name is invalid! \nPlease try again")
        # menunjukkan error jika kode yang diberikan bukan interger
        elif self.codec.get().isdigit() is False:
            messagebox.showerror("CODE ERROR!",
                                 "The code you entered aren't integers." +
                                 "\nPlease try again.")
        # menunjukkan error jika user tidak memasukkan 12 angka
        elif (len(self.codec.get()) != 12):
            messagebox.showerror("Wrong input!",
                                 "Please enter correct input code.")
        else:
            self.checksum()
            self.gambar_barcode()

    #fungsi untuk menghitung check digitnya
    def checksum(self):
        angka = str(self.codec.get()) # mengambil kode yang dimasukkan user
        jumlah = 0
        for i in range(12): 
            if i % 2 == 0:
                jumlah += int(angka[i])
            else:
                jumlah += 3 * int(angka[i])
        a = jumlah % 10

        # membuat perhitungan sesuai soal
        if a != 0:
            self.checkdigit = 10 - a
        else:
            self.checkdigit = a

    def detil_barcode(self):
        EAN_lst = ['LLLLLLL', 'LLGLGG', 'LLGGLG', 'LLGGGL', 'LGLLGG', 'LGGLLG', 
                   'LGGGLL', 'LGLGLG', 'LGLGGL', 'LGGLGL']
        
        EAN_dict = {
                    'L': ('0001101', '0011001', '0010011', '0111101', '0100011',
                          '0110001', '0101111', '0111011', '0110111', '0001011'),                         
                    'G': ('0100111', '0110011', '0011011', '0100001', '0011101', 
                          '0111001', '0000101', '0010001', '0001001', '0010111'),
                    'R': ('1110010', '1100110', '1101100', '1000010', '1011100', 
                          '1001110', '1010000', '1000100', '1001000', '1110100')            
        }
        
        # mencari total dari input kode user dan ditambah checkdigit
        self.total = str(self.codec.get()) + str(self.checkdigit)
        # membuat pola awal untuk barcodenya
        self.pola_bc = EAN_lst[int(self.total[0])] + 'RRRRRR'
        # menghapus digit pertama
        self.total_cut = self.total[1:]
        self.binarycode = ''

        # mengubah bilangan ke biner dari pola_bc
        for i in range(12):
            self.binarycode += EAN_dict[self.pola_bc[i]][int(self.total_cut[i])]
        self.binarycode += '101' # buat S
        # buat 12 code + M
        self.binarycode = (self.binarycode[0:45] + '01010' +
                           self.binarycode[45:])
        self.binarycode += '101' # buat E

    def gambar_barcode(self):
        x = 60
        self.detil_barcode()
        print(self.binarycode)
        for i in range(len(self.binarycode)):
            # self.canvas.create_rectangle(x, 75, x+2, 225, fill="blue", outline="blue")
            if i in [0, 2, 46, 48, 92, 94]:  # Menggambar barcode
                # if self.binarycode[i] == '1':
                self.canvas.create_rectangle(x, 75, x+2, 225, fill="blue", outline="blue")
                # elif self.binarycode[i] == '0':
                #     self.canvas.create_rectangle(x, 75, x+2, 225, fill="white", outline="white")
            else:
                if self.binarycode[i] == '1':
                    self.canvas.create_rectangle(x, 75, x+2, 215, fill="black", outline="black")
                elif self.binarycode[i] == '0':
                    self.canvas.create_rectangle(x, 75, x+2, 215, fill="white", outline="white")
            x += 2.5

        # menaru angka dibawah barcode
        first_6digit = self.total_cut[0:6]
        last_6digit = self.total_cut[6:13]

        # digit pertama
        X1 = 50
        self.canvas.create_text(X1, 235, text=self.total[0], font=("arial", 16, "bold"))

        # 6 digit pertama
        X2 = 78
        for i in range(len(first_6digit)):
            self.canvas.create_text(X2, 235, text=first_6digit[i], font=("arial", 14, "bold"))
            X2 += 17

        # 6 digit terakhir
        X3 = 194
        for i in range(len(last_6digit)):
            self.canvas.create_text(X3, 235, text=last_6digit[i], font=("arial", 14, "bold"))
            X3 += 17

        # membuat text "EAN-13 Barcode:" pada canvas
        self.canvas.create_text(180, 45, text="EAN-13 Barcode:", fill="black",
                                font=("Arial", 16, "bold"))
        # membuat "Check Digit: "
        self.canvas.create_text(180, 270,
                                text=f"Check Digit: {self.checkdigit}",
                                fill="#FFD011", font=("Arial", 16, "bold"))
        # menyimpan Canvas yang berisi Barcode menjadi postscript
        self.canvas.postscript(file=self.filename.get())

if __name__ == "__main__":
    barcode()