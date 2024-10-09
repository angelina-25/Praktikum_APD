# Daftar_Buku ={
#     "Buku1" : "Harry Poter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twilight"
# }
# # print(Daftar_BUku["Buku2"])
# print(Daftar_Buku['Buku1'])

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }

# games = dict(Sekiro = "Action", POkemon = "Adventure", Valorant = "FPS")
# print(games)

# print(Biodata["KRS"][1])
# print(Biodata.get("Nama"))
# print(Biodata.get("Alamat"))
# print(Biodata.get("Alamat", "Kosong bang"))

# for i,j in Biodata.items():
#     print(f"Key = {1} dan Value = {j}")

# Film = {
#   "Avenger Endgame" : "Action",
#   "Sherlock Holmes" : "Mystery",
#   "The Conjuring" : "Horror"
#  }
# print(Film)
# # del Film["The Conjuring"]
# # hapus = Film.pop("The Conjuring")

# Film.clear()
# print(Film)
# print(f"Key yang di hapus = {hapus}")


# # Film["ZombieLand"] = "Comedy"
# Film.update({"Hour" : "Thriller"})
# print(Film)


# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079,
#     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" :True,
#     "Social Media" : {
#         "Instagram" : "@aldyrmdhns_",
#         "Discord" : "\'Izanami#6848"
#         }
# }

# # print("Jumlah data dalam dict Biodata = ", len(Biodata))
# pinjamdict = Biodata.copy()
# print(pinjamdict)

# key = "Apel", "Jeruk", "Mangga"
# value = 1, 2, 3

# buah = dict.fromkeys(key, value)
# print(buah)

# Film = {
#   "Avenger Endgame" : "Action",
#   "Sherlock Holmes" : "Mystery",
#   "The Conjuring" : "Horror"
#  }

# print(Film)
# print("Film : ", Film.setdefault("Oldbook", "Horror"))
# print(Film)

# for i in Film.values():
#     print(i, end=" ")

# Musik = {
#       "The Chainsmoker" : ["All we Know", "The Paris"],
#       "Alan Walker" : ["Alone", "Lily"],
#       "Neffex" : ["Best of Me", "Memories"]
#  }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for lagu in j:
#         print(lagu)
#         print("")

# mahasiswa = {
#   101 : {"Nama" : "Aldy", "Umur" : 19},
#   111 : {"Nama" : "Abdul", "Umur" : 18}
#  }
# # print(f"sebelum : {mahasiswa}")
# # mahasiswa[101]["Angkatan"] = 2023
# # print(f"sesudah : {mahasiswa}")

# print(f"sebelum : {mahasiswa}")
# del mahasiswa[111]["Umur"]
# print(f"sesudah : {mahasiswa}")

# for i, j in mahasiswa.items():
#     print(f"ID : {i}")
#     # for i_a, j_a in j.items():
#     #     print(f"{i_a} : {j_a}")

#     for keynested, valuenested in j.items():
#         print(f"{keynested} : {valuenested}")

# #study kasus
# data = {
#     "Nama" : "Angel",
#     "Umur" : "19",
#     "NIM"  : "2409106014",
#     "Jurusan Angkatan" : "informatika"
#     "Angkatan"   "2024"
# }
# print(data.get("NIM"))
# data.update({"Umur" : "20"})
# print(data)

 