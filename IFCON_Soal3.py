print("*" * 60)
print("  🎓 SISTEM PENILAIAN UJIAN DAN KEHADIRAN 🎓  ")
print("*" * 60)

nilai_ujian = float(input("🔷 Masukkan nilai ujian Anda: "))
kehadiran = float(input("🔷 Masukkan persentase kehadiran Anda (%): "))

print("\n" + "~" * 60)

if nilai_ujian >= 80 and kehadiran >= 75:
    grade = "🌟 A (Excellent)"
elif nilai_ujian >= 70 and kehadiran >= 50:
    grade = "👍 B (Good)"
elif nilai_ujian < 70:
    grade = "🔔 C (Perlu peningkatan)"
elif kehadiran < 50:
    grade = "🚫 D (Kehadiran kurang dari 50%)"

print("📋 Hasil Penilaian 📋")
print(f"Nilai Ujian           : {nilai_ujian}")
print(f"Persentase Kehadiran  : {kehadiran}%")
print("~" * 60)
print(f"📢 Grade Akhir Anda    : {grade}")

print("\n" + "*" * 60)
print("  🌟 Terima kasih telah menggunakan sistem ini! 🌟  ")
print("*" * 60)