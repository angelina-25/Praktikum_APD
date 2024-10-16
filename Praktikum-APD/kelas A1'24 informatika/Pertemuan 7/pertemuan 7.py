# def salam():  
#      print ("Selamat datang mahasiswa baru")

# salam()


# def salam(salam):
#     print(salam)

# iso = "salam iso"
# salam(iso)


# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# print(luas_persegi(3))
# print(luas)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# luas = luas_persegi(2)
# print(luas)


# membuat variabel global  
# Nama = "Informatika"   
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"  
 
# # membuat variabel  lokal 
# def info(): 
#      Nama = "Teknik Elektro" 
#      Mata_Kuliah = "Pengantar Teknik ELektro" 
#      # mengakses variabel lokal 
#      print("Prodi:", Nama) 
#      print("Mata Kuliah:", Mata_Kuliah) 

# def info2():
#     print("Prodi:", Nama) 
#     print("Mata Kuliah:", Mata_Kuliah) 

# # mengakses variabel global 
# print("Prodi:", Nama) 
# print("Mata Kuliah:", Mata_Kuliah) 
 
# # memanggil fungsi info 
# info()         


# buku =[]  
# def show_data(): 
#      if len(buku) <= 0:  
#           print ("Belum Ada data") 
#      else:  
#           print("ID", "Nama Buku") 
#           for indeks in range(len(buku)):  
#                print (indeks, buku[indeks]) 
 
# # fungsi untuk menambah data   
# def insert_data():  
#      buku_baru = input("Judul Buku : ")   
#      buku.append(buku_baru)  
 
# # fungsi untuk edit data   
# def edit_data():  
#      show_data()  
#      indeks = int(input("Inputkan ID buku: ")) 
#      if(indeks >= len(buku) or indeks < 0):  
#           print ("ID salah")   
#      else:  
#           judul_baru = input("Judul baru: ")   
#           buku[indeks] = judul_baru  
 
# # fungsi untuk menhapus data   
# def delete_data():  
#      show_data()  
#      indeks = int(input("Inputkan ID buku: ")) 
#      if(indeks >= len(buku) or indeks < 0):  
#           print ("ID salah")   
#      else:  
#           buku.remove(buku[indeks])  
 
# # fungsi untuk menampilkan menu   
# def show_menu():  
#      print ("\n")  
#      print ("----------- MENU---------- ")  
#      print ("[1] Show Data")   
#      print ("[2] Insert Data")   
#      print ("[3] Edit Data")   
#      print ("[4] Delete Data")   
#      print ("[5] Exit")         
#      menu = input("PILIH MENU> ")   
#      print ("\n")  
#      if menu == "1":   
#           show_data()  
#      elif menu == "2":   
#           insert_data()  
#      elif menu == "3":   
#           edit_data()  
#      elif menu == "4":   
#           delete_data()  
#      elif menu == "5":   
#           exit()  
#      else:  
#           print ("Salah pilih!")  
# while (True): 
#      show_menu()


# def square_root(num):
#     precision=0.00001
#     if num < 0:
#         return "angka negtif tidak memiliki akar yang tidak teridentifikasi"
#     guess = num / 2.0
#     while abs(guess * guess / num) > precision:
#         guess = (guess + num / guess) / 2.0
#     return guess

# number = float(input("input angka: "))   
# result = square_root(number)
# print(f"akar dari {number} adalah {result}")

# import math
# angka = 49
# print(math.sqrt(angka))

# def luas_segitiga (alas, tinggi):
#     luas = 0.5 * alas * tinggi
#     return luas

# alas = float(input("Masukkan panjang alas segitiga: "))
# tinggi = float(input("Masukkan tinggi segitiga: "))

# luas = luas_segitiga(alas, tinggi)
# print(f"luas segitiga dengan a;as {alas} dan tinggi {tinggi} adalah: {luas}")


def luas_persegi_panjang (panjang, lebar):
    luas =  panjang * lebar
    return luas

alas = float(input("Masukkan panjang persegi panjang: "))
tinggi = float(input("Masukkan lebar persegi panjang: "))

luas = luas_persegi_panjang (panjang, lebar)
print(f"luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah: {luas}")