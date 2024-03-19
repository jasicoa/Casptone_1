from tabulate import tabulate

list_buku = [
    {"id": 101, "judul": "Harry Potter and the Philosopher's Stone", "penulis": "J.K. Rowling", "tahun_terbit": 1997, "penerbit": "Bloomsbury"},
    {"id": 102, "judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "tahun_terbit": 1960, "penerbit": "J.B. Lippincott & Co."},
    {"id": 103, "judul": "The Great Gatsby", "penulis": "F. Scott Fitzgerald", "tahun_terbit": 1925, "penerbit": "Charles Scribner's Sons"},
    {"id": 104, "judul": "1984", "penulis": "George Orwell", "tahun_terbit": 1949, "penerbit": "Secker & Warburg"},
    {"id": 105, "judul": "Pride and Prejudice", "penulis": "Jane Austen", "tahun_terbit": 1813, "penerbit": "T. Egerton, Whitehall"},
    {"id": 106, "judul": "The Catcher in the Rye", "penulis": "J.D. Salinger", "tahun_terbit": 1951, "penerbit": "Little, Brown and Company"}
]

def konfirmasi_simpan_buku():
    while True:
        konfirmasi = input("Apakah Anda yakin ingin menyimpan buku? (y/n): ").lower()
        if konfirmasi == 'y':
            return True
        elif konfirmasi == 'n':
            return False
        else:
            print("Masukan tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")

def tambah_buku():
    while True:
        id_buku = input("Masukkan ID buku: ")
        if id_buku.isdigit():
            id_buku = int(id_buku)
            if any(buku['id'] == id_buku for buku in list_buku):
                print("ID sudah digunakan. Masukkan ID lain.")
            else:
                break
        else:
            print("ID buku harus berupa angka.")

    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    penerbit = input("Masukkan nama penerbit: ")
    while True:
        tahun_terbit = input("Masukkan tahun terbit buku: ")
        if not tahun_terbit.isdigit():
            print("Masukkan tahun terbit harus berupa angka.")
        else:
            break

    # Menambahkan buku ke daftar
    if konfirmasi_simpan_buku():
        buku = {"id": id_buku, "judul": judul, "penulis": penulis, "tahun_terbit": int(tahun_terbit), "penerbit": penerbit}
        list_buku.append(buku)
        print("Buku berhasil ditambahkan.")
    else:
        print("Buku tidak disimpan.")

    while True:
        tambah_lagi = input("Apakah Anda ingin menambahkan buku lagi? (y/n): ").lower()
        if tambah_lagi == 'n':
            return
        elif tambah_lagi == 'y':
            break
        else:
            print("Masukan tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")

def print_book_list(list_buku):
    headers = ["ID", "Judul", "Penulis", "Tahun Terbit", "Penerbit"]
    rows = [[buku['id'], buku['judul'], buku['penulis'], buku['tahun_terbit'], buku['penerbit']] for buku in list_buku]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def tampil_buku():
    while True:
        print("\n=== Tampilkan Buku ===")
        print("1. Tampilkan semua data")
        print("2. Cari data berdasarkan ID")
        print("3. Kembali ke menu utama")

        choice = input("Pilih tindakan: ")
        
        if choice == "1":
            if not list_buku:
                print("Tidak ada buku dalam perpustakaan.")
            else:
                print_book_list(list_buku)
        elif choice == "2":
            id_cari = input("Masukkan ID buku yang ingin dicari: ")
            found = False
            for buku in list_buku:
                if str(buku['id']) == id_cari:
                    print("Data buku yang Anda cari:")
                    data = [[buku['id'], buku['judul'], buku['penulis'], buku['tahun_terbit'], buku['penerbit']]]
                    headers = ["ID", "Judul", "Penulis", "Tahun Terbit", "Penerbit"]
                    print(tabulate(data, headers=headers, tablefmt="grid"))
                    found = True
                    break
            if not found:
                print("Buku dengan ID tersebut tidak ditemukan.")
        elif choice == "3":
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def kelola_buku():
    while True:
        print("\n=== Kelola Buku ===")
        print("1. Perbarui Informasi Buku")
        print("0. Kembali")

        manage_choice = input("Pilih tindakan: ")

        if manage_choice == "1":
            print_book_list(list_buku)
            perbarui_info_buku()
        elif manage_choice == "0":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def perbarui_info_buku():
    id_buku = input("Masukkan ID buku yang ingin diperbarui: ")
    for buku in list_buku:
        if str(buku['id']) == id_buku:
            print("Informasi buku yang saat ini ada:")
            data = [[buku['judul'], buku['penulis'], buku['tahun_terbit'], buku['penerbit']]]
            headers = ["Judul", "Penulis", "Tahun Terbit", "Penerbit"]
            print(tabulate(data, headers=headers, tablefmt="grid"))
            
            while True:
                print("\nPilih informasi yang ingin diperbarui:")
                print("1. Judul")
                print("2. Penulis")
                print("3. Tahun Terbit")
                print("4. Penerbit")
                print("0. Kembali")
                
                choice = input("Masukkan pilihan: ")
                
                if choice == "1":
                    judul_baru = input("Masukkan judul baru: ")
                    buku['judul'] = judul_baru
                    print("Judul buku berhasil diperbarui.")
                    print_book_list(list_buku)
                    break
                elif choice == "2":
                    penulis_baru = input("Masukkan nama penulis baru: ")
                    buku['penulis'] = penulis_baru
                    print("Penulis buku berhasil diperbarui.")
                    print_book_list(list_buku)
                    break
                elif choice == "3":
                    tahun_terbit_baru = input("Masukkan tahun terbit baru: ")
                    while not tahun_terbit_baru.isdigit():
                        print("Masukkan tahun terbit harus berupa angka.")
                        tahun_terbit_baru = input("Masukkan tahun terbit baru: ")
                    buku['tahun_terbit'] = int(tahun_terbit_baru)
                    print("Tahun terbit buku berhasil diperbarui.")
                    print_book_list(list_buku)
                    break
                elif choice == "4":
                    penerbit_baru = input("Masukkan nama penerbit baru: ")
                    buku['penerbit'] = penerbit_baru
                    print("Penerbit buku berhasil diperbarui.")
                    print_book_list(list_buku)
                    break
                elif choice == "0":
                    return
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            return
    print("Buku tidak ditemukan.")

def hapus_buku():
    while True:
        print("\n=== Hapus Buku ===")
        print("1. Hapus buku berdasarkan ID")
        print("2. Hapus semua buku")
        print("3. Kembali ke menu utama")

        choice = input("Pilih tindakan: ")

        if choice == "1":
            print_book_list(list_buku)
            hapus_berdasarkan_id()
        elif choice == "2":
            hapus_semua_buku()
            return
        elif choice == "3":
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def hapus_berdasarkan_id():
    id_buku = input("Masukkan ID buku yang ingin dihapus: ")
    found = False
    for buku in list_buku:
        if str(buku['id']) == id_buku:
            print("Informasi buku yang akan dihapus:")
            data = [[buku['id'], buku['judul'], buku['penulis'], buku['tahun_terbit'], buku['penerbit']]]
            headers = ["ID", "Judul", "Penulis", "Tahun Terbit", "Penerbit"]
            print(tabulate(data, headers=headers, tablefmt="grid"))

            konfirmasi = input("Apakah Anda yakin ingin menghapus buku ini? (y/n): ").lower()
            if konfirmasi == 'y':
                list_buku.remove(buku)
                print("Buku berhasil dihapus.")
            found = True
            break

    if not found:
        print("Buku dengan ID tersebut tidak ditemukan.")

def hapus_semua_buku():
    konfirmasi = input("Apakah Anda yakin ingin menghapus semua buku? (y/n): ").lower()
    if konfirmasi == 'y':
        list_buku.clear()
        print("Semua buku berhasil dihapus.")
    else:
        print("Penghapusan semua buku dibatalkan.")

# Menjalankan program
while True:
    print("\n=== Sistem Perpustakaan ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Buku")
    print("3. Update Buku")
    print("4. Hapus Buku")
    print("0. Keluar")
    
    choice = input("Pilih tindakan: ")

    if choice == "1":
        tambah_buku()
    elif choice == "2":
        tampil_buku()
    elif choice == "3":
        kelola_buku()
    elif choice == "4":
        hapus_buku()
    elif choice == "0":
        print("Terima kasih telah menggunakan sistem perpustakaan.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

while True:
    print("\n=== Sistem Perpustakaan ===")
    print("1. Tambah Buku")
    print("2. Tampilkan Buku")
    print("3. Update Buku")
    print("4. Hapus Buku")
    print("0. Keluar")
    
    choice = input("Pilih tindakan: ")

    if choice == "1":
        tambah_buku()
    elif choice == "2":
        tampil_buku()
    elif choice == "3":
        kelola_buku()
    elif choice == "4":
        hapus_buku()
    elif choice == "0":
        print("Terima kasih telah menggunakan sistem perpustakaan.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
