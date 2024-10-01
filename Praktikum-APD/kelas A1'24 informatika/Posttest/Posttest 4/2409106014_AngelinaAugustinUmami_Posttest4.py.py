nama = input("Buat username anda: ")
password = int(input("Buat password anda berupa 3 angka nim terakhir: "))
salah = 0

while salah < 3:
    username = input("Masukkan username anda : ")
    pw = int(input("Masukkan password anda : "))
    if nama == username and pw == password :
        print("selamat datang gess")
        break
    else:
        print("gagal login")
        salah += 1
        if salah == 3: 
           print("gagal login 3 kali, programnya di hentikan ")
           exit()
while True:
    print("Pilih Jenis Kelamin:")
    print("1. Pria")
    print("2. Wanita")
    jenis_kelamin = int(input("Pilihan (1/2): "))
    
    berat = float(input("Masukkan berat (gram): ")) / 1000
    tinggi = float(input("Masukkan tinggi (km): ")) * 100000
    umur = int(input("Masukkan umur (tahun): "))

    if jenis_kelamin == 1 :  # Pria
        bmr = (10 * berat ) + (6.25 * tinggi) - (5 * umur) + 5
    elif jenis_kelamin == 2 :  # Wanita
        bmr = (10 * berat) + (6.25 * tinggi) - (5 * umur) - 161
    else:
        ("Jenis kelamin tidak valid.")

    print("Level Aktivitas Harian:")
    print("1. Aktivitas Minimal (jarang bergerak) ")
    print("2. Aktivitas Sedang (olahraga 1-3 kali seminggu) ")
    print("3. Aktivitas Tinggi (olahraga 4-7 kali seminggu) ")
    pilihan = int(input("Pilihan (1/2/3): "))
    
    if pilihan == 1 :
        tdee = bmr * 1.25
    elif pilihan == 2 :
        tdee = bmr * 1.36
    elif pilihan == 3 :
        tdee = bmr * 1.72
    else:
        print("Pilihan tidak valid.")
    
    
    print(f"BMR Anda adalah: {bmr:.2f} kalori/hari")
    print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah: {tdee:.2f} kalori/hari")

    lagi = input("apakah anda ingin mencoba lagi? (iya/tidak): ").lower()
    if lagi != 'iya':
        exit()