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
        faktor_aktivitas = 1.25
elif pilihan == 2 :
        faktor_aktivitas = 1.36
elif pilihan == 3 :
        faktor_aktivitas = 1.72
else:
    print("Pilihan tidak valid.")
    
tdee = bmr * faktor_aktivitas
    
print(f"BMR Anda adalah: {bmr:.2f} kalori/hari")
print(f"Kebutuhan Kalori Harian (TDEE) Anda adalah: {tdee:.2f} kalori/hari")