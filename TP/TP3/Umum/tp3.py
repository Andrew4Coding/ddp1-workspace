'''
Nama  : Andrew Devito Aryo
NPM   : 2306152494
Kelas : DDP1 - C
Asdos : GAN
'''

import matplotlib.pyplot as plt

def get_type(a_str):
  """ 
    Fungsi ini akan mengembalikan tipe dari literal
    string a_str.
    
    get_type("0.5") -> "float"
    get_type("5.") -> "float"
    get_type("5") -> "int"
    get_type("5.a") -> "str"
    
    parameter:
    a_str (string): string literal dari sebuah nilai
    
    return (string): "int", "float", atau "str"
  """
  try:
    int(a_str)
    return "int"
  except:
    try:
      float(a_str)
      return "float"
    except:
      return "str"
    
def read_csv(file_name, delimiter = ',', dir = r"./File_Pendukung/"):
  """
    Dataframe adalah sebuah abstraksi tabel data siap 
    proses yang dalam tugas kali ini direpresentasikan 
    sebagai 3-tuple:
    
      (data, list nama kolom, list tipe data)
    
    'data' merupakan list of lists yang menyimpan 
    nilai-nilai pada tabel dan mempunyai format:
    
    [[row_11, row_12, ..., row_1n],
     [row_21, row_22, ..., row_2n],
     ...
     [row_m1, row_m2, ..., row_mn]]
     
    Satu cell row_mn dapat bertipe string, integer,
    atau float. Jika semua cell pada kolom n berisi
    literal integer, maka ubah semuanya dalam tipe
    data integer; jika bukan integer, maka ada dua kemungkinan,
    yaitu float atau string; jika semua nilai pada
    kolom n berupa number dan ada satu yang float, maka
    jadikan semua tipe data pada kolom n tersebut sebagai
    float; jika cell-cell pada kolom n ada yang tidak 
    bisa dikonversikan ke integer maupun float, maka 
    tipe kolom n tersebut adalah string.
     
    Selain list of lists yang berisi tabel, informasi
    nama kolom juga disimpan dalam bentuk
    'list nama kolom':
    
    [nama_kolom_1, nama_kolom_2, ..., nama_kolom_n]
    
    Elemen ketiga pada 3-tuple adalah 'list tipe data'
    pada setiap kolom. Ada tiga jenis tipe data dalam
    tugas kali ini = "str", "int", dan "float". Sebuah
    kolom bertipe "int" jika semua elemen pada kolom
    tersebut adalah literal integer; "float" jika semua
    elemen pada kolom adalah literal float (dan bukan
    literal integer); "str" jika selain kedua di atas.
    
    Fungsi ini bertugas untuk membaca sebuah file comma
    separated value, melakukan parsing, dan mengembalikan
    dataframe yang berupa 3-tuple.
    
    ASUMSI file csv:
      1. selalu ada header (nama kolom) pada baris pertama
      2. nama kolom yang diberikan sudah dijamin unik
      
    Daftar Exceptions:
      1. jika ada baris dengan jumlah kolom berbeda dari
         sebelumnya,
         
           raise Exception(f"Banyaknya kolom pada baris {x} tidak konsisten.")
           
           dengan x adalah nomor baris (1-based) yang kolomnya 
           berlebih pertama kali.
           
      2. jika tabel kosong,
            
            raise Exception("Tabel tidak boleh kosong.")
    
    parameter:
    file_name (string): nama file comma separated value
    delimiter (string): karakter pemisah antar kolom pada 
                        suatu baris.
                        
    return (list, list, list): (data, list nama kolom, list tipe data)
  """
  # TODO: Implementasi
  fileOpen = open(dir + file_name, "r", encoding='utf-8').readlines()

  if fileOpen == []:
    raise Exception("Tabel tidak boleh kosong!")
  
  # Deklarasi template list yang akan di return di akhir function
  to_return = [[], [], []]
  
  for index, line in enumerate(fileOpen):
    # Menghapus \n dan spasi di akhir line, lalu line di split berdasarkan delimeter
    lst = line.strip().split(delimiter)

    # Jika iterasi berindeks 0, maka akan terindikasi sebagai baris nama kolom
    if index == 0:
      to_return[1] = lst
    else:
      # Mengecek apakah banyak kolom konsisten untuk setiap baris
      if len(lst) == len(fileOpen[index - 1].split(delimiter)):
        to_return[0].append(lst)
      else:
        raise Exception(f"Banyaknya kolom pada baris {index} tidak konsisten.")
  

  # TODO: Mengetahui type untuk masing-masing kolom, dan type akan di store di typeList
  type_list = []
  for column_index in range(len(to_return[1])):
    # Default type adalah int
    type = 'int'

    # Mengiterasi setiap item
    for item_index, item in enumerate(to_list(to_return)):
      if get_type(item[column_index]) == 'float':
        # Jika didapati float diantara item kolom, maka kolom akan dianggap bertipe Float (sementara dan dapat berubah jika didapati string)
        type = 'float'

        # Mengkonversi elemen menjadi type float
        to_return[0][item_index][column_index] =  float(to_return[0][item_index][column_index])
      
      # Jika type column didapati, maka seluruh item dalam kolom pasti bertipe string
      elif get_type(item[column_index]) == 'str':
        type_list.append('str')

        # Program akan dibreak karena kita sudah tahu item untuk satu kolom, tidak perlu diiterasi lagi
        break
      else:
        # Jika tipe bukan float maupun str, maka akan dianggap float
        to_return[0][item_index][column_index] =  int(to_return[0][item_index][column_index])
    else:
      type_list.append(type)
  
  # Memasukkan type list ke index terakhir pada to_return list 
  to_return[2] = type_list

  return to_return
   
def to_list(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
    
    mengembalikan bagian list of lists of items atau tabel data
    pada dataframe. Gunakan fungsi ini kedepannya jika ada keperluan
    untuk akses bagian data/tabel pada dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of lists of items
  """
  return dataframe[0]

def get_column_names(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[1] adalah berisi list of column names. Gunakan fungsi ini
    kedepannya jika ada keperluan untuk akses daftar nama kolom pada
    sebuah dataframe.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of column names
  """
  return dataframe[1]
  
def get_column_types(dataframe):
  """
  
    -- DIBUKA KE PESERTA --
  
    dataframe[2] adalah berisi daftar tipe data dari
    setiap kolom tabel. Hanya ada tiga jenis tipe data,
    yaitu "str", "int", dan "float"
    
    parameter:
    dataframe (list, list, list): sebuah dataframe yang merupakan 3-tuple
    
    return (list): list of type names
  """
  return dataframe[2]

def head(dataframe, top_n = 10):
  """
  
    -- DIBUKA KE PESERTA --
  
    top_n baris pertama pada tabel!
  
    Mengembalikan string yang merupakan representasi tabel
    (top_n baris pertama) dengan format:
    
     kolom_1|     kolom_2|     kolom_3|     ...
    ------------------------------------------- 
    value_11|    value_12|    value_13|     ...
    value_21|    value_22|    value_23|     ...
    ...         ...         ...
    
    Space setiap kolom dibatasi hanya 15 karakter dan right-justified.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    top_n (int): n, untuk penampilan top-n baris saja
    
    return (string): representasi string dari penampilan tabel.
    
    Jangan pakai print()! tetapi return string!
  """
  cols = get_column_names(dataframe)
  out_str = ""
  out_str += "|".join([f"{str(col)[:15]:>15}" for col in cols]) + "\n"
  out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
  for row in to_list(dataframe)[:top_n]:
    out_str += "|".join([f"{str(col)[:15]:>15}" for col in row]) + "\n"
  return out_str
  
def info(dataframe):
  """
    Mengembalikan string yang merupakan representasi informasi
    dataframe dalam format:
    
    Total Baris = xxxxx baris
    
    Kolom          Tipe
    ------------------------------
    kolom_1        tipe_1
    kolom_2        tipe_2
    ...
    
    Space untuk kolom dan tipe adalah 15 karakter, left-justified
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    
    return (string): representasi string dari info dataframe    
  """
  # TODO: Implementasi
  # Deklarasi variable count untuk menghitung jumlah baris
  line_count = len(to_list(dataframe))
  to_return = f"Total Baris = {line_count}"
  kolom = "Kolom"
  tipe = "Tipe"
  to_return += f"\n\n{kolom:<15} {tipe:<15}\n"
  to_return += "-"*30 + "\n"

  for index, item in enumerate(get_column_names(dataframe)):
    to_return += f"{item:<15} {get_column_types(dataframe)[index]}\n"

  return to_return

def satisfy_cond(value1, condition, value2):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    value1 (tipe apapun yang comparable): nilai pertama
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value2 (tipe apapun yang comparable): nilai kedua
    
    return (boolean): hasil perbandingan value1 dan value2
    
  """
  if condition == "<":
    return value1 < value2
  elif condition == "<=":
    return value1 <= value2
  elif condition == ">":
    return value1 > value2
  elif condition == ">=":
    return value1 >= value2
  elif condition == "!=":
    return value1 != value2
  elif condition == "==":
    return value1 == value2
  else:
    raise Exception(f"Operator {condition} tidak dikenal.")

def select_rows(dataframe, col_name1, condition1, value1, col_name2 = '', condition2 = '', value2 = ''):
  """
  Mengembalikan dataframe baru dimana baris-baris sudah
  dipilih hanya yang nilai col_name memenuhi 'condition'
  terkait 'value' tertentu.
  
  Gunakan/Call fungsi satisfy_cond(value1, condition, value2) yang
  sudah didefinisikan sebelumnya!
  
  contoh:
    select_rows(dataframe, "umur", "<=", 50) akan mengembalikan
    dataframe baru dengan setiap baris memenuhi syarat merupakan
    item dengan kolom umur <= 50 tahun.
    
  Exceptions:
    1. jika col_name tidak ditemukan,
    
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
        
    2. jika condition bukan salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    
        raise Exception(f"Operator {condition} tidak dikenal.")
  
  parameter:
  dataframe (list, list, list): sebuah dataframe
  col_name (string): nama kolom sebagai basis untuk selection
  condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
  value (tipe apapun): nilai untuk basis perbandingan pada col_name
  
  return (list, list, list): dataframe baru hasil selection atau filtering
  
  """
  # Handlng Exception
  if col_name1 not in get_column_names(dataframe):
    raise Exception(f"Kolom {col_name1} tidak ditemukan")
  if condition1 not in ["<", "<=", "==", ">", ">=", "!="]:
    raise Exception(f"Operator {condition1} tidak dikenal.")
  

  column_index1 = get_column_names(dataframe).index(col_name1)
  copy_of_dataframe = dataframe[:]
  temp = []
  type1 = get_column_types(dataframe)[column_index1] 

  # raise error message jika ingin membandingkan Kolom bertipe String dengan Integer, dan sebaliknya
  if type1 == 'str' and get_type(value1) != 'str':
    raise Exception(f"Tidak bisa menyeleksi Kolom String berdasarkan Bilangan")
  elif type1 != 'str' and get_type(value1) == 'str':
    raise Exception(f"Tidak bisa menyeleksi Kolom Numerik berdasarkan String")

  for entry in to_list(dataframe):
    if  type1 == 'str' and satisfy_cond(str(entry[column_index1]), condition1, str(value1)) or \
        type1 == 'float' and satisfy_cond(float(entry[column_index1]), condition1, float(value1)) or \
        type1 == 'int' and satisfy_cond(int(entry[column_index1]), condition1, int(value1)):
          temp.append(entry)

    
  copy_of_dataframe[0] = temp

  # Jika kondisi kedua benar-benar tidak diisi oleh user
  if (col_name2 == '' and condition2 == '' and value2 == ''):
    return copy_of_dataframe
  
  # jika kondisi kedua diisi secara lengkap
  elif (col_name2 != '' and condition2 != '' and value2 != ''):
    return select_rows(copy_of_dataframe, col_name2, condition2, value2)
  
  # Jika salah satu dari col_name2, condition2, dan value2 diisi, namun tidak semuanya
  else:
    raise Exception("Parameter tidak lengkap.")

def select_cols(dataframe, selected_cols):
  """
    Mengembalikan dataframe baru dimana kolom-kolom sudah
    dipilih hanya yang terdapat pada 'selected_cols' saja.
    
    contoh:
    select_cols(dataframe, ["umur", "nama"]) akan mengembalikan
    dataframe baru yang hanya terdiri dari kolom "umur" dan "nama".
    
    Exceptions:
      1. jika ada nama kolom pada selected_cols yang tidak
         ditemukan, 
         
           raise Exception(f"Kolom {selected_col} tidak ditemukan.")
           
      2. jika select_cols adalah list kosong [],
      
           raise Exception("Parameter selected_cols tidak boleh kosong.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    selected_cols (list): list of strings, atau list yang berisi
                          daftar nama kolom
                          
    return (list, list, list): dataframe baru hasil selection pada
                               kolom, yaitu hanya mengandung kolom-
                               kolom pada selected_cols saja.
    
  """
  # TODO: Implement
  to_return = [[], [], []]
  if selected_cols == []:
    raise Exception("Parameter selected_cols tidak boleh kosong.")
  
  # Mengiterasi setiap baris dalam dataframe
  for item in to_list(dataframe):
    temp = []
    # Mengiterasi setiap kolom pada list column yang di select
    for column in selected_cols:
      if column not in get_column_names(dataframe):
        raise Exception(f"Kolom {column} tidak ditemukan.")
      else:
        column_index = get_column_names(dataframe).index(column)

        # mengappend kolom yang diinginkan pada temp list
        temp.append(item[column_index])

    # Mengappend temp list yang berisi data kolom yang di select kedalam list to_return
    to_list(to_return).append(temp)

  for column in selected_cols:
    # Mengetahui index column yang dipilih pada type list dan name list
    column_index = get_column_names(dataframe).index(column)

    # Mengappend pada to_return list
    get_column_names(to_return).append(get_column_names(dataframe)[column_index])
    get_column_types(to_return).append(get_column_types(dataframe)[column_index])

  return to_return

def count(dataframe, col_name, can_num = False):
  """
    mengembalikan dictionary yang berisi frequency count dari
    setiap nilai unik pada kolom col_name.
    
    Tipe nilai pada col_name harus string !
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah numerik (int atau float),
      
           raise Exception(f"Kolom {col_name} harus bertipe string.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")

    Peserta bisa menggunakan Set untuk mengerjakan fungsi ini.
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (dict): dictionary yang berisi informasi frequency count
                   dari setiap nilai unik.
  """
  # TODO: Implement
  if to_list(dataframe) == []:
    raise Exception("Tabel Kosong.")
  if col_name not in get_column_names(dataframe):
    raise Exception(f"Kolom {col_name} tidak ditemukan")

  column_index = list(get_column_names(dataframe)).index(col_name)
  if get_column_types(dataframe)[column_index] != 'str' and can_num == False:
    raise Exception(f"Kolom {col_name} harus bertipe string.")
  
  # Mengambil setiap elemen dalam item list dalam setiap baris dataframe berdasarkan column_index
  list_of_value = [i[column_index] for i in to_list(dataframe)]

  count_dict = {}
  for value in list_of_value:
    count_dict[value] = list_of_value.count(value)
  
  return count_dict

def mean_col(dataframe, col_name):
  """
    Mengembalikan nilai rata-rata nilai pada kolom 'col_name'
    di dataframe.
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah string,
      
           raise Exception(f"Kolom {col_name} bukan bertipe numerik.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (float): nilai rataan
  """
  # TODO: Implementasi
  if to_list(dataframe) == []:
    raise Exception("Tabel Kosong")
  if col_name not in get_column_names(dataframe):
    raise Exception(f"Kolom {col_name} tidak ditemukan")

  # Mengetahui index column yang dipilih pada column_names
  column_index = list(get_column_names(dataframe)).index(col_name)
  if get_column_types(dataframe)[column_index] != 'str':
    # Mengselect hanya satu column, jadi bisa kita implementasi fungsi select_cols()
    selected_column_dataframe = select_cols(dataframe, [col_name])
    sum = 0
    for [item] in to_list(selected_column_dataframe):
      sum += item
    
    # Mereturn rata-rata 
    return sum / len(to_list(selected_column_dataframe))
  else:
    raise Exception(f"Kolom {col_name} bukan bertipe numerik.")

def show_scatter_plot(x, y, x_label, y_label):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    x (list): list of numerical values, tidak boleh string
    y (list): list of numerical values, tidak boleh string
    x_label (string): label pada sumbu x
    y_label (string): label pada sumbu y
    
    return None, namun fungsi ini akan menampilkan scatter
    plot dari nilai pada x dan y.
    
    Apa itu scatter plot?
    https://chartio.com/learn/charts/what-is-a-scatter-plot/
  """
  plt.scatter(x, y)
  plt.title(f"{x_label} vs {y_label}")
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()

def show_scatter(dataframe, col_name_x, col_name_y):
  """
    fungsi ini akan menampilkan scatter plot antara kolom col_name_x
    dan col_name_y pada dataframe.
    
    pastikan nilai-nilai pada col_name_x dan col_name_y adalah angka!
    
    Exceptions:
      1. jika col_name_x tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
           
      2. jika col_name_y tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
           
      3. jika col_name_x BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
           
      4. jika col_name_y BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name_x (string): nama kolom yang nilai-nilainya diplot pada axis x
    col_name_y (string): nama kolom yang nilai-nilainya diplot pada axis y
    
    Call fungsi show_scatter_plot(x, y) ketika mendefinisikan fungsi
    ini!
    
    return None
  """
  # TODO: Implement
  listx = []
  listy = []  
  
  # Mengecek apakah parameter yang diber  ikan tidak menimbulkan exception
  if safe_plot_checker(dataframe, col_name_x, col_name_y):
    # Mengetahui indeks masing-masing kolom
    col_index_x = list(get_column_names(dataframe)).index(col_name_x)
    col_index_y = list(get_column_names(dataframe)).index(col_name_y)

    # Mengiterasi dan mengappend nilai value masing-masing kolom
    for i in range(len(to_list(dataframe))):
      listx.append(float(to_list(dataframe)[i][col_index_x]))
      listy.append(float(to_list(dataframe)[i][col_index_y]))

  show_scatter_plot(listx, listy, col_name_x, col_name_y)

# Extra Features
def safe_plot_checker(dataframe, col_name_x, col_name_y, col_name_z=''):
  '''
  Fungsi ini digunakan untuk mengecek apakah parameter yang diberikan sudah sesuai
  harapan. Jika sesuai, maka akan return True. 

  Fungsi ini diimplementasi pada fungsi scatter()
  '''
  if col_name_x in get_column_names(dataframe):
    col_index_x = list(get_column_names(dataframe)).index(col_name_x)
    if get_column_types(dataframe)[col_index_x] != 'str':
      if col_name_y in get_column_names(dataframe):
        col_index_y = list(get_column_names(dataframe)).index(col_name_x)
        if get_column_types(dataframe)[col_index_y] != 'str':

          if col_name_z != '':
            if col_name_z in get_column_names(dataframe):
              col_index_z = list(get_column_names(dataframe)).index(col_name_x)
              if get_column_types(dataframe)[col_index_z] != 'str':
                return True
              else:
                raise Exception(f"Kolom {col_name_z} bukan bertipe numerik.")
            else:
              raise Exception(f"Kolom {col_name_z} tidak ditemukan.")
          else:
            return True

        else:
          raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
      else:
        raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
    else:
      raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
  else:
    raise Exception(f"Kolom {col_name_x} tidak ditemukan.")

def sorted_dataframe(dataframe, base_col, reverse=False):
  '''
    Fungsi ini dapat mengsort dataframe berdasarkan kolom yang diinginkan.
    User juga dapat memberi parameter reverse jika urutan ingin sort ingin dibalik
  '''
  # Exception Handling:
  if dataframe == []:
    raise Exception("Tabel Kosong")
  if base_col not in get_column_names(dataframe):
    raise Exception(f"Kolom {base_col} tidak ditemukan.")

  copy = dataframe[:]
  column_index = get_column_names(dataframe).index(base_col)

  # Mengsort list berdasarkan kolom yg dipilih
  copy[0] = sorted(to_list(copy), key=lambda x: x[column_index], reverse=reverse)

  return copy

def custom_plot(dataframe, col_name_x, col_name_y, col_name_z = '', type='scatter-3d'):
  '''
  Custom plot
  Now we can plot to 2D plot or 3D plot

  2D plot option: plot, stem, stackplot
  3D plot option: scatter-3d, stem-3d, plot-3d

  Fungsi ini merupakan pengembangan dalam plotting matplotlib
  Fungsi meminta input berupa kolom X, kolom Y, dan kolom Z yang optional (apabila ingin 3D plotting)

  Fungsi ini dapat membuat plotting jenis-jenis lain dri matplotlib, seperti stem, plot, scatter 3d, plot 3d, etc
  '''
  listx = []
  listy = []
  listz = []

  # Mengecek apakah parameter yang diberikan tidak menimbulkan Exceptions
  if safe_plot_checker(dataframe, col_name_x, col_name_y, col_name_z):
    col_index_x = get_column_names(dataframe).index(col_name_x)
    col_index_y = get_column_names(dataframe).index(col_name_y)
    if col_name_z != '':
      col_index_z = get_column_names(dataframe).index(col_name_z)

    for i in range(len(to_list(dataframe))):
      listx.append(float(to_list(dataframe)[i][col_index_x]))
      listy.append(float(to_list(dataframe)[i][col_index_y]))
      if col_name_z != '':
        listz.append(float(to_list(dataframe)[i][col_index_z]))

    # Jika kolom ke z tidak diisi, maka dinggap hanya mengapply plot 2 dimensi
    if col_name_z == '':
      if type == 'plot':
        plt.plot(listx, listy)
      elif type == 'stem':
        plt.stem(listx, listy)
      elif type == 'stackplot':
        plt.stackplot(listx, listy)

      plt.xlabel = col_name_x
      plt.ylabel = col_name_y

      plt.show()
    
    # Jika kolom z diisi, maka dianggap akan plotting 3d
    else:
      fig = plt.figure(figsize=(12, 12))
      ax = fig.add_subplot(projection='3d')

      ax.set_xlabel(col_name_x)
      ax.set_ylabel(col_name_y)
      ax.set_zlabel(col_name_z)
      
      if type == 'scatter-3d':
        ax.scatter(listx, listy, listz)
      elif type == 'stem-3d':
        ax.stem(listx, listy, listz)
      elif type == 'plot-3d':
        ax.plot(listx, listy, listz)
      else:
        raise Exception(f"Jenis Plot {type} tidak ditemukan.")
      
      plt.show()

def median(dataframe, col_name):
  '''
    Fungsi ini mereturn median dari kolom yang dipilih.
  '''
  # Agar bisa mendapatkan median, fungsi ini harus di sort terlebih dahulu dri kecil ke besar
  # Sehingga kita bisa mendapatkan nilai pertama dan terakhir pada list sesuai urutan

  # Handling Exception
  if dataframe == []:
    raise Exception('Tabel Kosong')
  if col_name not in get_column_names(dataframe):
    raise Exception(f'Kolom {col_name} tidak ditemukan')
  
  copy = sorted_dataframe(dataframe, col_name)

  column_index = get_column_names(copy).index(col_name)
  if get_column_types(copy)[column_index] not in ['float', 'int']:
    raise Exception(f"Kolom {col_name} bukan bertipe numerik")
  data_len = len(copy[0])

  # Jika panjang list ganjil
  if data_len % 2 != 0:
    median = copy[0][int((data_len + 1) / 2) - 1][column_index]
  # Jika panjang list genap
  else:
    median = int(copy[0][(data_len / 2) - 1] + copy[0][(data_len/2 + 1) - 1]) / 2

  return f"Median Kolom {col_name}: {median}"

def mode(dataframe, col_name):
  if to_list(dataframe) == []:
    raise Exception(f"Tabel kosong.")
  if col_name not in get_column_names(dataframe):
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  
  temp_dict = count(dataframe, col_name, True)
  maxvalues = max(temp_dict.values())
  res = [k for k, v in temp_dict.items() if v==maxvalues]
  if len(res) > 1:
    # Jika ada beberapa element yang adalah modus, maka akan return list berisi element dengan count tertinggi
    return f"Modus Kolom {col_name}: {res} dengan kemunculan sebanyak {temp_dict[res[0]]} kali"
  else:  
    return f"Modus Kolom {col_name}: {res[0]} dengan kemunculan sebanyak {temp_dict[res[0]]} kali"

if __name__ == "__main__":
  # TODO: Buat program yang memanfaatkan fungsi-fungsi di atas
  dataframe = read_csv('abalone.csv')
  print(head(dataframe, top_n=10))
  print(info(dataframe))

  new_dataframe = select_rows(dataframe, "Length", ">", 0.49)
  print(head(new_dataframe, top_n=5))

  new_dataframe = select_rows(select_rows(dataframe, "Length",\
                                              ">", 0.49), \
                                              "Sex", "==", "M")
  print(head(new_dataframe, top_n=5))
  
  new_dataframe = select_cols(dataframe, ["Sex", "Length",\
                                      "Diameter", "Rings"])
  print(head(new_dataframe, top_n=5))

  print(mean_col(dataframe, "Length"))

  print(count(dataframe, 'Sex'))

  print(head(sorted_dataframe(dataframe, 'Rings', True), 50))

  print(median(dataframe, 'Rings'))

  print(mode(dataframe, 'Shucked_weight'))

  show_scatter(dataframe, "Length", "Diameter")

  custom_plot(dataframe, 'Length', 'Diameter', 'Rings', type='scatter-3d')