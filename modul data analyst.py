# ==========================================
# 1.Kenali dataset
# ==========================================
import pandas as pd

# Membaca file Excel
df = pd.read_excel("Data Supermarket-Latihan.xlsx")

file = file = "Data Supermarket-Latihan.xlsx"
print("=== NAMA KOLOM EXCEL ===")
print(df.head(15).to_string())

# Menampilkan 5 data pertama
print("=== DATA EXCEL ===")
print(df.head())

# Menampilkan nama kolom
print("\n=== NAMA KOLOM ===")
for kolom in df.columns:
    print(kolom)
    
# Menampilkan ukuran data
print("\n=== UKURAN DATA ===")
print(df.shape)

# ==========================================
#STEP 2 — Cari data kosong
# ==========================================
print("\n === DATA KOSONG ===")
print(df.isnull().sum())

# ==========================================
# STEP 3 — Cari data duplikat
# ==========================================

print("\n === Data Duplikat ===")
print(df.duplicated().sum())

# ==========================================
#STEP 4 — Lihat statistik
# ==========================================
print("\n === STATISTIK DATA ===")
print(df.describe())


print("=== UKURAN DATA ===")
print(df.shape)

print("\n=== 5 DATA PERTAMA ===")
print(df.head())

print("\n=== NAMA KOLOM ===")
print(df.columns.tolist())

# ==========================================
# STEP 5 — DATA CLEANING
# ==========================================

# 1. Membuat salinan dataset
df_clean = df.copy()
print("=== DATA SEBELUM CLEANING ===")
print(df_clean.shape)

# 2. Menghapus data duplikat
df_clean = df_clean.drop_duplicates()
print("\n=== SETELAH MENGHAPUS DUPLIKAT ===")
print("Jumlah baris :", df_clean.shape[0])
print("Jumlah kolom :", df_clean.shape[1])

# 3. Mengecek data kosong
print("\n=== DATA KOSONG ===")
print(df_clean.isnull().sum())

#untuk membersihkan data yang ada 
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 1'], errors='ignore')
print(df_clean.isnull().sum())

# 4. Mengisi data kosong

# Untuk kolom numerik → isi dengan nilai median
kolom_numerik = df_clean.select_dtypes(include='number').columns
for kolom in kolom_numerik:
    df_clean[kolom] = df_clean[kolom].fillna(df_clean[kolom].median())
    
# Untuk kolom teks → isi dengan nilai yang paling sering muncul
kolom_teks = df_clean.select_dtypes(include='object').columns
for kolom in kolom_teks:
    df_clean[kolom] = df_clean[kolom].fillna(df_clean[kolom].mode()[0])
    
# 5. Mengecek kembali data kosong :
print("\n === DATA KOSONG SETELAH CLEANING ===")
print(df_clean.isnull().sum)

#6. Mengecek tipe data
print("\n=== TIPE DATA ===")
print(df_clean.dtypes)

# 8. Melihat ukuran dataset akhir
print("\n === UKURAN DATASET AKHIR ===")
print(df_clean.shape)

#cari nama kolam dataset 
print("=== NAMA KOLOM ===")
print(df_clean.columns.tolist())


