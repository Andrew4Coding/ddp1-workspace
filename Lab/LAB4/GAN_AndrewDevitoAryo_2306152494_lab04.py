# Nama          : Andrew Devito Aryo
# NPM           : 2306152494
# Kelas         : C
# Kode Asdos    : GAN

# Fungsi untuk menampilkan Index Line dan Konten line
def lineNumber(line, text):
    return f"{line:03d}. {text}"

# Fungsi Main
def main():
    try:
        print("Lab 04 -- DDP1 -- 2023")
        counter_char = 0                                    # Membuat Variable Counter Character
        contain = ""                                        # Variable untuk menampung konten yang akan di write
        input_file = input("Input File Name: ")             # Meminta input nama file input dari User
        #my_dir = f"File Kuliah\\"                           # Melacak Directory dari File yang diingikan
        try:
            data = open(input_file, "r")           # Membuka File yang diinginkan di read
        except:
            print("File Not Found!")                        # Jika file tidak ditemukan, maka keluarkan message error
            quit()

        output_file = input("Output File Name: ")           # Meminta input nama file output dari User
            
        for index, line in enumerate(data):                 # Mengiterasi setiap line yang ada di File                            # Menambah Counter
            contain += lineNumber(index + 1, line)           # Meng-append setiap line kedalam Contain
            for char in line:                                # Mengiterasi setiap Char dalam Line
                if char.isalnum():                            # Menambah Counter apabila Character bukan whitespace
                    counter_char+=1

        with open(output_file, "w") as writer:     # Membuka file output
            writer.write(contain + f"\n\nThe total number of letters in the file {input_file} is {counter_char}")    # Menuliskan hasil iterasi kedalam file output

        print("-- End Of Program -- ")
    except KeyboardInterrupt:
        print("\n-- Program di Terminate--")

if __name__ == '__main__':      
    main()      # Memanggil Fungsi Main