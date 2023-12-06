print("=====================================")
print("===Program Penghitung Biaya Parkir===")
print("=====================================")

jam_masuk = int(input("\nMasukan jam masuk [1-12] : "))
jam_keluar = int(input("Masukan jam keluar [1-12] : "))

lama_parkir = 0

if jam_masuk <= jam_keluar:
    lama_parkir += jam_keluar - jam_masuk
else:
    lama_parkir += 12 - 10
    lama_parkir += jam_keluar

biaya_parkir = 0

if lama_parkir > 0:
    biaya_parkir += 2000
    lama_parkir -= 2

if lama_parkir < 0:
    lama_parkir = 0

biaya_parkir += lama_parkir * 500

print(f"Biaya parkir : Rp.{biaya_parkir}")
