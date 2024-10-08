users = [["angel", "angel123", "admin"], ["augustin1", "augustin123", "user"]]
print(f"username admin : {users[0][0]} ")
print(f"username user : {users[1][0]} ")
jadwal_event = []  

nama_event_list = [
    "bazar makanan" , 
    "pameran seni" ,
    "festival musik" , 
    "event lari" , 
    ]

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
        users.append([username, password, "user"])
        print(f"Users '{username}' berhasil didaftarkan.\n")
    
    elif pilihan == '2':
        print("--- Login ---")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")        
        user_login = None
        for user in users:
            if username == user[0] and password == user[1]:
                user_login = user
                print(f"Login berhasil, {username} ({user[2]}).")
                break
        if not user_login:
            print("Login gagal !")    
            continue

        if user_login[2] == "admin":
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
                    print("--- Semua Event ---")
                    print(jadwal_event)
                    
                elif admin_pilihan == '2':
                    print("--- Hapus Event Pengguna ---")
                    nama_event = input("Masukkan nama event yang ingin dihapus: ")
                    event_ditemukan = False
                    for event in jadwal_event:
                        if event[1] == nama_event:
                            jadwal_event.remove(event)
                            print(f"Jadwal '{nama_event}' dari pengguna '{event[0]}' berhasil dihapus.")
                            event_ditemukan = True
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
                        
                    event_baru = [user_login[0], nama_event, tanggal, waktu, deskripsi]
                    jadwal_event.append(event_baru)
                    print(f"Event '{nama_event}' berhasil ditambahkan.")
                    
                elif user_pilihan == '2':
                    print(f"--- Event untuk {user_login[0]} ---")
                    ada_event = False
                    for event in jadwal_event:
                        if event[0] == user_login[0]:
                            print(f"Nama: {event[1]}, Tanggal: {event[2]}, Waktu: {event[3]}, Deskripsi: {event[4]}")
                            ada_event = True
                    if not ada_event:
                        print("Tidak ada event yang tersedia.\n")
                    
                elif user_pilihan == '3':
                    print("--- Perbarui Event ---")
                    nama_event = input("Masukkan nama event yang ingin diperbarui: ")
                    event_ditemukan = False
                    for event in jadwal_event:
                        if event[0] == user_login[0] and event[1] == nama_event:
                            tanggal_baru = input("Masukkan tanggal baru (dd-mm-yyyy): ")
                            waktu_baru = input("Masukkan waktu baru (HH:MM): ")
                            deskripsi_baru = input("Masukkan deskripsi baru: ")
                            event[2] = tanggal_baru
                            event[3] = waktu_baru
                            event[4] = deskripsi_baru
                            print(f"Event '{nama_event}' berhasil diperbarui.")
                            event_ditemukan = True
                            break
                    if not event_ditemukan:
                        print(f"Event dengan nama '{nama_event}' tidak ditemukan.")
                    
                elif user_pilihan == '4':
                    print("--- Hapus Event ---")
                    nama_event = input("Masukkan nama event yang ingin dihapus: ")
                    event_ditemukan = False
                    for event in jadwal_event:
                        if event[0] == user_login[0] and event[1] == nama_event:
                            jadwal_event.remove(event)
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
