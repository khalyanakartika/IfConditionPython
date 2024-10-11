print("="*10)
print("  SOAL 2  ")
print("="*10)


print("="*50)
print("     SISTEM PENENTUAN STATUS BEASISWA MAHASISWA     ")
print("="*50)

ipk = float(input(">> Masukkan IPK Anda: "))
jumlah_kegiatan = int(input(">> Masukkan jumlah kegiatan ekstrakurikuler: "))

print("\n" + "-"*50)

if ipk >= 3.5:
    status_beasiswa = "✅ Berhak mendapatkan Beasiswa Penuh"
elif 3.0 <= ipk < 3.5:
    if jumlah_kegiatan > 2:
        status_beasiswa =  "✅ Berhak mendapatkan Beasiswa Sebagian"
    else:
        status_beasiswa = "❌ Tidak berhak mendapatkan Beasiswa"
else:
    status_beasiswa = "❌ Tidak berhak mendapatkan Beasiswa"

print("📊 Hasil Penentuan Beasiswa 📊")
print(f"IPK Anda              : {ipk}")
print(f"Jumlah Kegiatan       : {jumlah_kegiatan}")
print("-"*50)
print(f"📢 Status Beasiswa     : {status_beasiswa}")