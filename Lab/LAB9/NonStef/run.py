class Person():
    def __init__(self, nama, payment, stamina):
        self.__nama = nama
        self.__payment = payment
        self.__stamina = stamina
        self.__total_work = 0
    
    # Getter and Setter
    def setStamina(self, stamina):
        self.__stamina = stamina
    def setTotalWork(self, total_work):
        self.__total_work = total_work
    
    def getNama(self):
        return self.__nama
    def getPayment(self):
        return self.__payment
    def getStamina(self):
        return self.__stamina
    def getTotalWork(self):
        return self.__total_work
    
    # Method
    def pay_day(self):
        return self.__payment * self.__total_work
    def is_available(self, cost_stamina):
        if self.__stamina >= cost_stamina:
            return True
        else:
            return False
    def work(self, cost_stamina):
        self.__stamina -= cost_stamina
        self.__total_work += 1

    def __str__(self, add_bonus = 0):
        # TODO
        return f"{self.__class__.__name__:20} | {self.__nama:20} | Total kerja:{self.__total_work:20} | Stamina:{self.__stamina:20} | Gaji:{self.pay_day() + add_bonus:20}"

class Worker(Person):
    def __init__(self, nama, payment, stamina):
        super().__init__(nama, payment, stamina)
        self.__bonus = 0
    def work(self, bonus, cost_stamina):
        self.__bonus += bonus
        self.setStamina(self.getStamina() - cost_stamina)
        self.setTotalWork(self.getTotalWork() + 1)
    def getBonus(self):
        return self.__bonus
    def setBonus(self, new_bonus):
        self.__bonus = new_bonus

    def __str__(self):
        return super().__str__(self.__bonus)
    
class Manager(Person):
    def __init__(self, name, payment, stamina):
        super().__init__(name, payment, stamina)
        self.__list_worker = []

    def getListWorker(self):
        return self.__list_worker
    
    def Hire_worker(self, name):
        self.work(10)
        for worker in self.__list_worker:
            if name in worker[0]:
                print("Sudah ada!")
                break
        else:
            print("Berhasil mendapat pegawai baru")
            self.__list_worker.append((name, Worker(name, 5000, 100)))
    
    def Fire_worker(self, name):
        for item in self.__list_worker:
            if name in item[0]:
                self.work(10)
                self.__list_worker.remove(item)
                print(f"Berhasil memecat {name}")
                break
        else:
            print("Nama tidak ditemukan")

    def Give_work(self, name, bonus, cost_stamina):
        self.work(10)        
        for item in self.__list_worker:
            if name == item[0]:
                item[1].work(bonus, cost_stamina)
                break
    def __str__(self):
        return super().__str__()
def main():
    nama_manager = input("Masukkan nama manager: ")
    jumlah_pembayaran = int(input("Masukkan jumlah pembayaran: "))
    stamina_manager = int(input("Masukkan stamina manager: "))

    # Main Menu Start Here
    # TODO: Inisialisasi Manager
    manager = Manager(nama_manager, jumlah_pembayaran, stamina_manager)

    while manager.is_available(1):
        print("""
PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
        """)
        action = int(input("Masukkan pilihan: "))
        
        # TODO
        if action == 1:
            print(manager)
            for worker in manager.getListWorker():
                print(worker[1])
        elif action == 2:
            kepada = input("Tugas akan diberikan kepada: ")

            worker_object = None
            for worker_tuple in manager.getListWorker():
                if worker_tuple[0] == kepada:
                    bonus_pekerjaan = int(input("Bonus pekerjaan: "))
                    beban_stamina = int(input("Beban stamina: "))
                    
                    worker_object = worker_tuple[1]
                    if worker_object.is_available(beban_stamina):
                        manager.Give_work(kepada, bonus_pekerjaan, beban_stamina)
                        print("Hasil cek ketersediaan pegawai: ")
                        print("Pegawai dapat menerima pekerjaan")
                        print("========================================")
                        print(f"Berhasil memberi pekerjaan kepada {kepada}")
                    else:
                        print("Pegawai tidak dapat menerima pekerjaan. Stamina pegawai tidak cukup.")
                    break
            else:
                print("Nama tidak ditemukan!")

            

        elif action == 3:
            nama_pegawai = input('Nama pegawai baru: ')

            manager.Hire_worker(nama_pegawai)

        elif action == 4:
            nama_pegawai = input("Nama pegawai yang akan dipecat: ")
            manager.Fire_worker(nama_pegawai)

        elif action == 5:
            print("""
----------------------------------------
Berhenti mengawasi hotel, sampai jumpa !
----------------------------------------""")
            return
    print("""
----------------------------------------
Stamina manajer sudah habis, sampai jumpa !
----------------------------------------""")
    
if __name__ == '__main__':
    main()