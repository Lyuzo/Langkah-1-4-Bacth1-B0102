# ==========================================
# LANGKAH 1: DEKLARASI DATA DIRI & NILAI MENTAH
# ==========================================
nim = "23010199"
nama_mahasiswa = "Ahmad Rian"
semester = 3
is_aktif = True

str_nilai_algoritma = "85.5"
str_nilai_basis_data = "78.0"
str_nilai_pemrograman_web = "90.2"
sks_per_matkul = 3

print(f"Data Mahasiswa: {nama_mahasiswa} (NIM: {nim})")
print("Status Aktif  :", is_aktif)


# ==========================================
# LANGKAH 2: KONVERSI TIPE DATA (Type Casting)
# ==========================================
nilai_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_nilai_pemrograman_web)


# ==========================================
# LANGKAH 3: KALKULASI MENGGUNAKAN VARIABEL
# ==========================================
total_nilai = nilai_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul


# ==========================================
# LANGKAH 4: PENENTUAN STATUS KELULUSAN
# ==========================================
# Lulus jika rata-rata >= 75.0 dan status mahasiswa aktif
is_lulus_semester = (rata_rata_nilai >= 75.0) and is_aktif

print("\n=== HASIL EVALUASI AWAL ===")
print("Total Nilai       :", total_nilai)
print("Rata-Rata Nilai   :", round(rata_rata_nilai, 2))
print("Total SKS         :", total_sks_diambil)
print("Status Lulus      :", is_lulus_semester)


# ==========================================
# LANGKAH 5: TIPE DATA KOLEKSI (List & Dictionary)
# ==========================================
daftar_matkul = ["Algoritma dan Pemrograman", "Basis Data", "Pemrograman Web"]
transkrip_nilai = {
    "Algoritma dan Pemrograman": 4.0, 
    "Basis Data": 3.0,                
    "Pemrograman Web": 4.0             
}

print("\nDaftar Mata Kuliah Diambil:", daftar_matkul)
print("Detail Transkrip Mutu :", transkrip_nilai)


# ==========================================
# LANGKAH 6: LUARAN AKHIR (Tampilan Rapi)
# ==========================================
print("\n" + "="*40)
print("      SISTEM INFORMASI AKADEMIK (SIAKAD)      ")
print("="*40)
print(f"NIM Mahasiswa    : {nim}")
print(f"Nama Mahasiswa   : {nama_mahasiswa}")
print(f"Semester         : {semester}")
print(f"Status Aktif     : {is_aktif}")
print("-" * 40)
print("Daftar Mata Kuliah:")
for mk in daftar_matkul:
    print(f" - {mk} (Mutu: {transkrip_nilai[mk]})")
print("-" * 40)
print(f"Total Nilai      : {total_nilai}")
print(f"Rata-rata Nilai  : {round(rata_rata_nilai, 2)}")
print(f"Total SKS        : {total_sks_diambil}")
print(f"Status Kelulusan : {'LULUS' if is_lulus_semester else 'TIDAK LULUS'}")
print("="*40)