print("===================================")
print("=========Program Jam Kerja=========")
print("===================================")

jam_masuk = int(input("\nMasukan jam masuk [1-23] : "))
jam_pulang = int(input("Masukan jam pulang [1-23] : "))

jam_kerja = jam_pulang - jam_masuk
print(f"Total jam kerja : {jam_kerja} jam")
