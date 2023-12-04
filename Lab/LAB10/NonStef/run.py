
import tkinter as tk
from tkinter import messagebox

class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        self.dict_hotel = {
            'hotel1': [10, 250000,  'kode_hotel_1'], 
            'hotel2': [12, 500000,  'kode_hotel_2'], 
            'hotel3': [10, 7500000, 'kode_hotel_3'], 
            'hotel4': [1, 1000000,  'kode_hotel_4'], 
            'hotel5': [10, 900000,  'kode_hotel_5'], 
            'hotel6': [10, 6000000, 'kode_hotel_6']
        }
        
        self.frame1 = tk.Frame(self.master)
        self.frame2 = tk.Frame(self.master)
        self.frame1.grid(row=1, column=1, padx=50, pady=50)
        self.frame2.grid(row=1, column=2, padx=50, pady=50)

        self.load_hotel_data()

        # TODO : tambahkan title dan ukuran windows
        self.homepage()
        
    # TODO : tambahkan label, field, dan button yang dibutuhkan
    def homepage(self):
        # Meminta input
        tk.Label(self.frame2, text='Nama Pengguna').pack()
        self.user_name = tk.StringVar()
        user_name_entry = tk.Entry(self.frame2, textvariable=self.user_name)
        user_name_entry.pack()

        tk.Label(self.frame2, text='Nama Hotel').pack()
        self.hotel_name = tk.StringVar()
        hotel_name_entry = tk.Entry(self.frame2, textvariable=self.hotel_name)
        hotel_name_entry.pack()

        tk.Label(self.frame2, text='Jumlah Kamar').pack()
        self.jumlah_kamar = tk.StringVar()
        jumlah_kamar_hotel = tk.Entry(self.frame2, textvariable=self.jumlah_kamar)
        jumlah_kamar_hotel.pack()

        pesan_kamar_button = tk.Button(self.frame2, text='Pesan Kamar', command=self.booking)
        pesan_kamar_button.pack()
        
        exit_button = tk.Button(self.frame2, text='Exit')
        exit_button.pack()
    
    def load_hotel_data(self):
        for item in self.frame1.winfo_children():
            item.destroy()

        for item in self.dict_hotel:
            text_to_load = f"Nama Hotel: {item}\nJumlah Kamar Tersedia: {self.dict_hotel[item][0]}\nHarga per Kamar: {self.dict_hotel[item][1]}\n"

            tk.Label(self.frame1, text=text_to_load, anchor='nw', justify='left', font='Helvetica 9').pack()


    def reset(self):
        self.jumlah_kamar.set('')
        self.hotel_name.set('')
        self.user_name.set('')
        self.load_hotel_data()

    # TODO : tambahkan logic untuk validasi proses booking
    def booking(self):
        # Jika input yang diberikan tidak benar
        try:
            if int(self.jumlah_kamar.get()) <= 0:
                messagebox.showerror('Error', 'Maaf, kamar yang dipesan harus lebih dari 0')
                self.reset()
            else:
                if self.hotel_name.get() in self.dict_hotel:
                    if self.dict_hotel[self.hotel_name.get()][0] > int(self.jumlah_kamar.get()):
                        user_name = self.user_name.get()
                        hotel_name = self.hotel_name.get()
                        room_count = int(self.jumlah_kamar.get())
                        total_price = self.dict_hotel[hotel_name][1]
                        ticket_number = f"{self.dict_hotel[hotel_name][2]}/{room_count}/{user_name[:3]}"

                        messagebox.showinfo('Booking Berhasil', f'Booking berhasil!\nPesanan untuk {user_name} di hotel {hotel_name} sebanyak {room_count}!\nTotal biaya: {total_price} Nomor Tiket: {ticket_number}')
                        self.dict_hotel[self.hotel_name.get()][0] -= int(self.jumlah_kamar.get())
                        self.reset()
                    else:
                        messagebox.showerror('Error', f'Tidak bisa memesan kamar sebanyak {self.jumlah_kamar.get()} di hotel {self.hotel_name.get()}')
                        self.reset()
                else:
                    messagebox.showerror('Error', f'Hotel {self.hotel_name.get()} tidak ditemukan!')
                    self.reset()

        except:
            messagebox.showerror('Error', 'Jumlah Kamar harus integer')
            self.reset()

        

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x600')
    root.title('LAB 10')
    root.resizable(False, False)
    app = PacilokaApp(master=root)
    root.mainloop()