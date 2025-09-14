bobot_tugas = 0.30
bobot_uts = 0.30
bobot_uas = 0.40

nilai_tugas = 85
nilai_uts = 75
nilai_uas = 90

jumlah_tugas =  nilai_tugas * bobot_tugas
jumlah_uts =   nilai_uts * bobot_uts
jumlah_uas =  nilai_uas * bobot_uas

nilai_akhir = jumlah_tugas + jumlah_uts + jumlah_uas

print ("====Nilai yang andi peroleh====")
print ("nilai tugas", nilai_tugas)
print ("nilai uts", nilai_uts)
print ("nilai uas", nilai_uas)

print("=====================")

print ("Jumlah nilai akhir tugas andi (30%): ", jumlah_tugas)
print ("Jumlah nilai akhir uts andi (30%): ", jumlah_uts)
print ("Jumlah nilai akhir uas andi (30%): ", jumlah_uas)

print("=====================")

print("Total nilai akhir andi: ", nilai_akhir)