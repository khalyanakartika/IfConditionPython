print("="*10)
print("  SOAL 1  ")
print("="*10)

# variabel Harga makanan utama dan makanan penutup
harga_makanan_utama = 100000
harga_makanan_penutup = 30000

# Untuk tampilan awal
print("="*40)
print("              TOTAL HARGA            ")
print("="*40)


jenis_makanan = input("Masukkan jenis makanan (Makanan Utama/Makanan Penutup): ").title() #menggunakan title() untuk membuat huruf pertama setiap kata menjadi huruf besar
jumlah_makanan = int(input("Masukkan jumlah makanan: "))
anggota_loyal = input("Apakah pelanggan anggota loyal (True/False)?:  ").lower() == "true" #menggunakan lower() untuk mengubah setiap huruf menjadi huruf kecil, kemudian di periksa apakah input sama dengan "true", jika sama dengan string "true" maka hasilnya True jika tidak maka False


print("\n" + "-"*40)    #pemisah

# Logika perhitungan harga
if jenis_makanan == "Makanan Utama" or jenis_makanan == "Makanan Penutup": #memeriksa apakah input jenis makanan sama dengan "Makanan Utama" atau "Makanan Penutup
    if jenis_makanan == "Makanan Utama":                                   #jika makanan utama maka  harga makanan utama yang digunakan
        harga_awal = harga_makanan_utama * jumlah_makanan                  #kemudian pada variabel harga_awal akan di isi hasil perkalian harga makanan utama dan jumlah makanan
    else:
        harga_awal = harga_makanan_penutup * jumlah_makanan                #jika makanan penutup maka harga makanan penutup yang akan digunakan
        
    # jika makanan lebih dari 2 maka di kenakan biaya tambahan 15%
    if jumlah_makanan > 2:                  
        harga_awal += harga_awal * 0.15     # Biaya tambahan 15% dari harga awal yang akan ditambahkan paad variabel harga_awal

    # Jika anggota loyal maka akan di beri diskon 10%
    if anggota_loyal:    
        harga_awal -= harga_awal * 0.10  # Diskon 10%  dari harga awal yang akan dikurangi pada variabel harga_awal
 

    # Tampilkan total harga
    print(f"Jenis makanan        : {jenis_makanan}")
    print(f"Jumlah makanan       : {jumlah_makanan}")
    print(f"Anggota loyal        : {'Ya' if anggota_loyal else 'Tidak'}") #jika variabel anggota_loyal bernilai True, maka akan mencetak "Ya", jika False, akan mencetak "Tidak"
    print("-"*40)
    print(f"Total harga          : Rp{harga_awal:,.0f}")
else:
    print("Jenis makanan tidak valid")

# Akhiri tampilan
print("="*40)
print("        Terima kasih telah berbelanja        ")
print("="*40)