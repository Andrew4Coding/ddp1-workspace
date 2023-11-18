# Nama          : Andrew Devito Aryo
# NPM           : 2306152494
# Kelas         : C
# Kode Asdos    : GAN
# Membuat Program Pencarian dan Sorting Data

# Mengimport Library yang dibutuhkan
import sys, os, time
terminal_width = os.get_terminal_size().columns     # Menghitung lebar terminal

# Meng-set lokasi folder dataset
main_dir = "C:\\Users\Andrew's Laptop\\Documents\\indo-law-main\\indo-law-main\\dataset\\"

# main dir: cd C:\Users\Andrew's Laptop\Documents\Bot and Kuliah\File Kuliah\TP2\
# Contoh beberapa test case: 
# python search.py all "mustang" provinsi:jateng
# python search.py fakta "laptop acer" provinsi:jateng

# Menggunakan Exception jika argumen yang diberikan kosong
try:
        
    try:
        section     = sys.argv[1].lower()
        if section == "--usage":
            print("Usage: python search.py <section> <keyword1> <operator> <keyword2>")
            sys.exit()
        else:
            keyword1    = sys.argv[2].lower()
    except SystemExit:
        sys.exit()
    except:
        print("Argumen program tidak benar.")
        quit()

    try:
        logic_operator = sys.argv[3]
        if logic_operator not in ['AND', 'OR', 'ANDNOT']:
            if ":" in logic_operator:
                extra_filter = logic_operator
            else:
                print("Mode harus berupa AND, OR atau ANDNOT.")
                sys.exit()
        else:
            try:    
                keyword2 = sys.argv[4].lower()
                try:
                    extra_filter = sys.argv[5].lower()
                except:
                    extra_filter = ""
            except:
                print("Argumen program tidak benar.")
                sys.exit()
    except SystemExit:
        sys.exit()
    except:
        # Jika Logic Operator DAN Keyword2 tidak diisi, maka Logic Operator dan Keyword 2 dianggap ""
        logic_operator = keyword2 = extra_filter = ""

    # Variable File Counter akan digunakan untuk menghitung jumlah file yang diiterasi
    file_counter = 0

    # Memulai Perhitungan waktu Iterasi 
    start_time = time.time()
    result_table = ""

    # Mengiterasi setiap File dalam Folder Data set
    for index, file in enumerate(os.listdir(main_dir)):
        # Membuka File
        with open(main_dir + file, "r") as f:
            data = f.read().replace("\n", ' ').lower()

        # Membuka isi dari section tag yang diinginkan
        section_content = data[data.find(f'<{section}>'):data.find(f'</{section}>')+1]

        # Pengaturan Loading Bar
        percentage = (index / 22630) * 100  # Mencari tahu persentase progres iterasi
        bar_width = terminal_width - len(f"Data Found: {file_counter} | Iterating File {file}") - 20
        bar_word = f"Data Found: {file_counter} | Iterating File: {file} " + "█"*(int(percentage / 100 * bar_width))
        if percentage < 100:
            print(bar_word + f" {percentage:.2f}%", end="\r")
        if percentage > 99.99:
            print(bar_word + f"   Done!", end="\r")
            time.sleep(1.5)          # Menunggu sekian detik sebelum menampilkan hasil akhir

            print(f" "*terminal_width, end="\r")    # Menghilangkan progres bar

        sort_bool_all = True
        sort_bool_section = True
        
        # Mengecek setiap kemungkinan OPERATOR
        if logic_operator == "AND":
            sort_bool_all = keyword1 in data and keyword2 in data
            if sort_bool_all == False:
                continue    # Jika data saja sudah tidak ditemukan di data, maka Skip 
            sort_bool_section = keyword1 in section_content and keyword2 in section_content
        elif logic_operator == "OR":
            sort_bool_all = keyword1 in data or keyword2 in data
            if sort_bool_all == False:
                continue
            sort_bool_section = keyword1 in section_content or keyword2 in section_content
        elif logic_operator == "ANDNOT":
            sort_bool_all = keyword1 in data and not keyword2 in data
            if sort_bool_all == False:
                continue
            sort_bool_section = keyword1 in section_content and not keyword2 in section_content
        else:
            sort_bool_all = keyword1 in data
            sort_bool_section = keyword1 in section_content
            

        # Mengambil setiap atribute pada tag <putusan>
        putusan_content     = data[data.find('<putusan'):data.find('>')+1].split()
        klasifikasi         = putusan_content[4].replace("klasifikasi=", "").replace('"', '')
        lembaga_peradilan   = putusan_content[6].replace("lembaga_peradilan=", '').replace('"', '')
        provinsi            = putusan_content[7].replace("provinsi=", '').replace('"', '')
        sub_klasifikasi     = putusan_content[9].replace("sub_klasifikasi=", '').replace('"', '')
        
        # Untuk specific Search
        index_of_colon = extra_filter.find(":") 
        specific_section = extra_filter[:index_of_colon]
        specific_section_content = extra_filter[index_of_colon+1:]

        # Pengecekan untuk filtrasi dari Specific Section
        if specific_section == "klasifikasi":
            sort_bool_specific_section = specific_section_content in klasifikasi
        elif specific_section == "lembaga_peradilan":
            sort_bool_specific_section = specific_section_content in lembaga_peradilan
        elif specific_section == "provinsi":
            sort_bool_specific_section = specific_section_content in provinsi
        elif specific_section == "sub_klasifikasi":
            sort_bool_specific_section = specific_section_content in sub_klasifikasi
        else:
            sort_bool_specific_section = True

        # Mengecek eksistesi Keyword di data yang ingin dicari
        if ((section == 'all' and sort_bool_all) or (section != 'all' and sort_bool_section)) and sort_bool_specific_section:
            word = "| {:>6} | {:>38} | {:>12}{:>15} | {:>27} | {:>27} |".format(index+1, file, provinsi, klasifikasi, sub_klasifikasi[:20], lembaga_peradilan[:20])
            result_table += word + "\n" 
            file_counter += 1

    end_time = time.time() - 1.5   # Mengakhiri perhitungan waktu

    print("-"*141)
    print("| {:>6} | {:>38} | {:>12} | {:>12} | {:>27} | {:>27} |".format("Num", "Nama File", "Provinsi", "Klasifikasi", "Sub Klasifikasi", "Lembaga Peradilan"))
    print("-"*141)
    print(result_table.rstrip())
    print("-"*141)

    print(f"\nBanyaknya dokumen yang ditemukan\t: {file_counter}")
    print(f"Total waktu pencarian\t\t\t: {(end_time - start_time):.3f} detik")

except KeyboardInterrupt:   # Menghandle kasus dimana Ctrl + C di klik
    print(" "*terminal_width, end='\r')
    print("Program di Interupsi.")
    quit()