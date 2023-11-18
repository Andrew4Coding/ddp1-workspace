# Nama          : Andrew Devito Aryo
# NPM           : 2306152494
# Kelas         : C
# Kode Asdos    : GAN

# TODO: Fungsi ini me-Return row segitiga pascal
def make_new_row(old_row):
    new_row = [1]
    for index in range(len(old_row)):
        try:
            new_row.append(sum(old_row[index:index+2]))
        except IndexError:
            break
    return new_row

# TODO: Fungsi Main
def main():
    # Validasi Input User
    while True:
        try:
            height = int(input("Enter the height of Pascal's triangle (integer > 2):"))
            # Prompt Input akan berhenti jika user memasukkan angka > 2
            if height > 2:
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input")
    
    temp = [1]
    contain_lists = []

    print("\nPrinting the whole list of lists:")
    print("[")
    for _ in range(height):
        contain_lists.append(temp)  # Mengappend list barisan ke list utama
        print(f"{temp},")

        # Memperbarui nilai temp dengan hasil olahan fungsi terhadap nilai temp lama
        temp = make_new_row(temp)   
    print("]\n")

    # Jika kita lihat, temp menjadi penampung row terakhir segitiga Pascal
    str_last_row = [str(i) for i in temp]   # Mengcopy list integer dan mengubahnya menjadi String
    str_last_row = ' '.join(str_last_row)   # Menggabungkan element dalam list
    
    print(f"Pascal's triangle of height {height}:")
    for list in contain_lists:  # Mengiterasi setiap list row dalam list utama
        str_list = [str(i) for i in list]   # Mengubah komponen list row kedalam bentuk String list
        result = ' '.join(str_list) # Menggabungkan element String list menjadi string
        print(result.center(len(str_last_row))) # Memprint hasil dengan posisi centered berdasarkan panjang string row terakhir
        
    input("\nPress Enter to exit ...")

if __name__ == "__main__":
    main()