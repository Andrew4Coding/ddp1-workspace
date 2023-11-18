class Hotel():
    def __init__(self, name, available_room, room_price, list_of_user = []):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.list_of_user = list_of_user
        self.profit = 0
    def booking(self, other, jumlah_kamar):
        pass
    def add_user(self, user_name):
        self.list_of_user.append(user_name)
    def __str__(self):
        pass
class User():
    def __init__(self, name, money, list_of_hotel = []):
        self.name = name
        self.money = money
        self.list_of_hotel = list_of_hotel
    def topup(self, jumlah_topup):
        self.money += jumlah_topup
    def add_hotel(self, hotel_name):
        self.list_of_hotel.append(hotel_name)
    def __str__(self):
        pass

def main():
    banyak_hotel = int(input("Masukkan banyak hotel: "))
    banyak_user = int(input("Masukkan banyak user: "))

    dict_hotel = dict()
    dict_user = dict()
    
    for i in range(1, banyak_hotel + 1):
        nama_hotel = input(f"\nMasukkan nama hotel ke-{i}: ")
        banyak_kamar_hotel = int(input(f"Masukkan banyak kamar hotel ke-{i}: "))
        harga_kamar_hotel = int(input(f"Masukkan harga satu kamar hotel ke-{i}: "))
        
        dict_hotel.update({nama_hotel: Hotel(nama_hotel, banyak_kamar_hotel, harga_kamar_hotel)})

    for i in range(1, banyak_user + 1):
        nama_user = input(f"\nMasukkan nama user ke-{i}: ")
        saldo_user = int(input(f"Masukkan saldo user ke-{i}: "))

        dict_user.update({nama_user: User(nama_user, saldo_user)})

    while True:
        print('''\n=============Welcome to Paciloka!=============\n''')
        perintah = int(input("Masukkan perintah: "))
        if perintah == 1:
            print("\nDaftar Hotel:")
            indexing = 1
            for keys in dict_hotel:
                print(f"{indexing}. {keys}")
                indexing += 1

            print("\nDaftar User:")
            indexing = 1
            for keys in dict_user:
                print(f"{indexing}. {keys}")
                indexing += 1

        elif perintah == 2:
            nama_hotel = input("Masukkan nama hotel: ")
            if nama_hotel not in dict_hotel:
                print("Nama hotel tidak ditemukan di sistem!")
                continue
            print(f"Hotel dengan nama {nama_hotel} mempunyai profit sebesar {dict_hotel[nama_hotel].profit}")
        elif perintah == 3:
            nama_user = input("Masukkan nama user: ")
            if nama_user not in dict_user:
                print("Nama user tidak ditemukan di sistem!")
                continue
            print(f"User dengan nama {nama_user} mempunyai saldo sebesar {dict_user[nama_user].money}")

        elif perintah == 4:
            nama_user = input("Masukkan nama user: ")
            saldo_yang_ditambahkan = int(input("Masukkan jumlah uang yang akan ditambahkan ke user: "))
            if saldo_yang_ditambahkan < 0:
                print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
            dict_user[nama_user].topup(saldo_yang_ditambahkan)
            print(f"Berhasil menambahkan {saldo_yang_ditambahkan} ke user {nama_user}. Saldo User menjadi {dict_user[nama_user].money}")

        elif perintah == 5:
            nama_user = input("Masukkan nama user: ")
            nama_hotel = input("Masukkan nama hotel: ")
            jumlah_kamar = int(input("Masukkan jumlah kamar yang akan dibooking: "))

            if nama_user not in dict_user:
                print("Nama user tidak ditemukan di sistem!")
                continue
            if nama_hotel not in dict_hotel:
                print("Nama hotel tidak ditemukan di sistem!")
                continue
            if jumlah_kamar < 0:
                print("Jumlah kamar yang akan di pesan harus lebih dari 0!")
                continue
            if jumlah_kamar > dict_hotel[nama_hotel].available_room:
                print("Booking tidak berhasil!")
                continue
            dict_hotel[nama_hotel].profit += jumlah_kamar*dict_hotel[nama_hotel].room_price
            dict_user[nama_user].money -= jumlah_kamar*dict_hotel[nama_hotel].room_price
            dict_hotel[nama_hotel].available_room -= jumlah_kamar

            if nama_hotel not in dict_hotel[nama_hotel].list_of_user:
                dict_hotel[nama_hotel].list_of_user.append(nama_user)
            if nama_user not in dict_user[nama_user].list_of_hotel:
                dict_user[nama_user].list_of_hotel.append(nama_hotel)

            print(f"User dengan nama {nama_user} berhasil melakukan booking di hotel {nama_hotel} dengan jumlah {jumlah_kamar} kamar!")

        elif perintah == 6:
            nama_hotel = input("Masukkan nama hotel: ")
            if dict_hotel[nama_hotel].list_of_user == []:
                print(f"Hotel {nama_hotel} tidak memiliki pelanggan")
                continue
            for user in dict_hotel[nama_hotel].list_of_user:
                print(f"{nama_hotel} | {user}")
        elif perintah == 7:
            nama_user = input("Masukkan nama user: ")
            if dict_user[nama_user].list_of_hotel == []:
                print(f"User {nama_user} tidak pernah melakukan booking!")
                continue
            for hotel in dict_user[nama_user].list_of_hotel:
                print(f"{nama_hotel} | {hotel}")

        elif perintah == 8:
            print("Terima kasih sudah mengunjungi Paciloka!")
            break
        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")
            break


if __name__ == '__main__':
    main()