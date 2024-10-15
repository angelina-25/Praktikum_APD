users = {
    "angel": {"password": "angel123", "role": "admin"},
    "augustin1": {"password": "augustin123", "role": "user"}
}

jadwal_event = {}  # Dictionary untuk menyimpan event

nama_event_list = {
    "bazar makanan": {
        "tanggal": "19-12-2023",
        "waktu": "12:00",
        "deskripsi": "Bazar makanan yang menyediakan berbagai kuliner khas daerah."
    },
    "pameran seni": {
        "tanggal": "24-10-2023",
        "waktu": "13:00",
        "deskripsi": "Pameran seni lukis dan patung dari seniman lokal."
    },
    "festival musik": {
        "tanggal": "25-09-2023",
        "waktu": "14:00",
        "deskripsi": "Festival musik yang menampilkan band lokal dan internasional."
    },
    "event lari": {
        "tanggal": "26-09-2024",
        "waktu": "16:00",
        "deskripsi": "Event lari marathon 10K untuk masyarakat umum."
    }
}

while True:
    print(
    """
    ===============================
    |       MANAJEMEN EVENT       |
    ===============================
    | 1. REGISTRASI PENGGUNA BARU |        
    | 2. LOGIN                    |          
    | 3. KELUAR                   |     
    ===============================
    """
    )
    pilihan = input("Pilih opsi (1/2/3): ")
    
    if pilihan == '1':
        print("--- Registrasi Pengguna Baru ---")
        username = input("Masukkan username baru: ")
        password = input("Masukkan password baru: ")
        users[username] = {"password": password, "role": "user"}
        print(f"Users '{username}' berhasil didaftarkan.\n")
    
    elif pilihan == '2':
        print("--- Login ---")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        
        if username in users and users[username]["password"] == password:
            user_login = users[username]
            print(f"Login berhasil, {username} ({user_login['role']}).")
        else:
            print("Login gagal!")
            continue
        
        if user_login["role"] == "admin":
            while True:
                print(
                """
                ===============================
                |         MENU ADMIN          |
                ===============================
                |  1. TAMPILKAN SEMUA EVENT   |        
                |  2. HAPUS EVENT PENGGUNA    |          
                |  3. LOGOUT                  |     
                ===============================
                """
                )
                admin_pilihan = input("Pilih opsi (1/2/3): ")
                    
                if admin_pilihan == '1':
                    print("--- Semua Event yang Ditambahkan Pengguna ---")
                    if jadwal_event:
                        for user, events in jadwal_event.items():
                            print(f"Event dari pengguna '{user}':")
                            for event in events:
                                print(f"Nama: {event['nama']}, Tanggal: {event['tanggal']}, Waktu: {event['waktu']}, Deskripsi: {event['deskripsi']}")
                    else:
                        print("Tidak ada event yang ditambahkan oleh pengguna.")
                    
                    print("\n--- Event yang Sudah Ada di Sistem ---")
                    for nama_event, detail_event in nama_event_list.items():
                        print(f"Nama: {nama_event}, Tanggal: {detail_event['tanggal']}, Waktu: {detail_event['waktu']}, Deskripsi: {detail_event['deskripsi']}")
                    
                elif admin_pilihan == '2':
                    print("--- Hapus Event Pengguna ---")
                    nama_event = input("Masukkan nama event yang ingin dihapus: ")
                    event_ditemukan = False
                    for user, events in jadwal_event.items():
                        for event in events:
                            if event["nama"] == nama_event:
                                jadwal_event[user].remove(event)
                                print(f"Jadwal '{nama_event}' dari pengguna '{user}' berhasil dihapus.")
                                event_ditemukan = True
                                break
                        if event_ditemukan:
                            break
                    if not event_ditemukan:
                        print(f"Event dengan nama '{nama_event}' tidak ditemukan.")
                    
                elif admin_pilihan == '3':
                    print("Logout berhasil.")
                    break
                    
                else:
                    print("Pilihan tidak valid.")
                

        else:
            while True:
                print(
                """
                ===========================
                |       MENU EVENT        |
                ===========================
                |    1. TAMBAH EVENT      |           
                |    2. TAMPILKAN EVENT   |          
                |    3. UBAH EVENT        |     
                |    4. HAPUS EVENT       |      
                |    5. LOGOUT            |  
                ===========================
                """
                )
                user_pilihan = input("Pilih opsi (1/2/3/4/5): ")
                    
                if user_pilihan == '1':
                    print("--- Tambah Event ---")
                    nama_event = input("Masukkan nama event: ")
                    tanggal = input("Masukkan tanggal (dd-mm-yyyy): ")
                    waktu = input("Masukkan waktu (HH:MM): ")
                    deskripsi = input("Masukkan deskripsi: ")
                    
                    event_baru = {
                        "nama": nama_event,
                        "tanggal": tanggal,
                        "waktu": waktu,
                        "deskripsi": deskripsi
                    }
                    
                    if username not in jadwal_event:
                        jadwal_event[username] = []
                    jadwal_event[username].append(event_baru)
                    print(f"Event '{nama_event}' berhasil ditambahkan.")
                    
                elif user_pilihan == '2':
                    print(f"--- Event untuk {username} ---")
                    if username in jadwal_event and jadwal_event[username]:
                        for event in jadwal_event[username]:
                            print(f"Nama: {event['nama']}, Tanggal: {event['tanggal']}, Waktu: {event['waktu']}, Deskripsi: {event['deskripsi']}")
                    else:
                        print("Tidak ada event yang tersedia.\n")
                    
                elif user_pilihan == '3':
                    print("--- Perbarui Event ---")
                    nama_event = input("Masukkan nama event yang ingin diperbarui: ")
                    event_ditemukan = False
                    if username in jadwal_event:
                        for event in jadwal_event[username]:
                            if event["nama"] == nama_event:
                                tanggal_baru = input("Masukkan tanggal baru (dd-mm-yyyy): ")
                                waktu_baru = input("Masukkan waktu baru (HH:MM): ")
                                deskripsi_baru = input("Masukkan deskripsi baru: ")
                                event["tanggal"] = tanggal_baru
                                event["waktu"] = waktu_baru
                                event["deskripsi"] = deskripsi_baru
                                print(f"Event '{nama_event}' berhasil diperbarui.")
                                event_ditemukan = True
                                break
                    if not event_ditemukan:
                        print(f"Event dengan nama '{nama_event}' tidak ditemukan.")
                    
                elif user_pilihan == '4':
                    print("--- Hapus Event ---")
                    nama_event = input("Masukkan nama event yang ingin dihapus: ")
                    event_ditemukan = False
                    if username in jadwal_event:
                        for event in jadwal_event[username]:
                            if event["nama"] == nama_event:
                                jadwal_event[username].remove(event)
                                print(f"Event '{nama_event}' berhasil dihapus.")
                                event_ditemukan = True
                                break
                    if not event_ditemukan:
                        print(f"Event dengan nama '{nama_event}' tidak ditemukan.")
                    
                elif user_pilihan == '5':
                    print("Logout berhasil.")
                    break
                    
                else:
                    print("Pilihan tidak valid.")
    
    elif pilihan == '3':
        print("Terima kasih telah menggunakan sistem.")
        break
    
    else:
        print("Pilihan tidak valid.")
