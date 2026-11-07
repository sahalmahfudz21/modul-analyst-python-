import pandas as pd

df = pd.read_excel(
    "Data Supermarket-Latihan.xlsx",
    sheet_name="Sheet1"
)

df_clean = df.copy()
# ==========================================
# STEP 6 — ANALISIS DATA
# ==========================================

print("\n===================================")
print("           ANALISIS DATA")
print("===================================")


# ==========================================
# 1. TOTAL PENJUALAN
# ==========================================

total_penjualan = df_clean["Total"].sum()

print("\n=== 1. TOTAL PENJUALAN ===")
print(f"Total penjualan : {total_penjualan:,.2f}")


# ==========================================
# 2. TOTAL PRODUK YANG TERJUAL
# ==========================================

total_produk = df_clean["Quantity"].sum()

print("\n=== 2. TOTAL PRODUK TERJUAL ===")
print(f"Jumlah produk terjual : {total_produk:,}")


# ==========================================
# 3. PRODUK PALING BANYAK TERJUAL
# ==========================================

produk_terjual = (
    df_clean.groupby("Product line")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== 3. JUMLAH PRODUK TERJUAL PER KATEGORI ===")
print(produk_terjual)

produk_terlaris = produk_terjual.idxmax()
jumlah_terlaris = produk_terjual.max()

print("\nProduk dengan jumlah terjual terbanyak :")
print(produk_terlaris)
print(f"Jumlah : {jumlah_terlaris}")


# ==========================================
# 4. PENJUALAN PER PRODUK
# ==========================================

penjualan_produk = (
    df_clean.groupby("Product line")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== 4. PENJUALAN BERDASARKAN PRODUK ===")
print(penjualan_produk)


# ==========================================
# 5. CABANG DENGAN PENJUALAN TERTINGGI
# ==========================================

penjualan_cabang = (
    df_clean.groupby("Branch")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== 5. PENJUALAN PER CABANG ===")
print(penjualan_cabang)

cabang_tertinggi = penjualan_cabang.idxmax()
nilai_cabang_tertinggi = penjualan_cabang.max()

print("\nCabang dengan penjualan tertinggi :")
print(cabang_tertinggi)
print(f"Total penjualan : {nilai_cabang_tertinggi:,.2f}")


# ==========================================
# 6. ANALISIS JENIS PELANGGAN
# ==========================================

jenis_pelanggan = df_clean["Customer type"].value_counts()

print("\n=== 6. JENIS PELANGGAN ===")
print(jenis_pelanggan)


# ==========================================
# 7. TOTAL PENJUALAN BERDASARKAN PELANGGAN
# ==========================================

penjualan_pelanggan = (
    df_clean.groupby("Customer type")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== 7. PENJUALAN BERDASARKAN JENIS PELANGGAN ===")
print(penjualan_pelanggan)


# ==========================================
# 8. METODE PEMBAYARAN
# ==========================================

metode_pembayaran = df_clean["Payment"].value_counts()

print("\n=== 8. METODE PEMBAYARAN ===")
print(metode_pembayaran)

pembayaran_terbanyak = metode_pembayaran.idxmax()
jumlah_pembayaran = metode_pembayaran.max()

print("\nMetode pembayaran paling banyak digunakan :")
print(pembayaran_terbanyak)
print(f"Jumlah transaksi : {jumlah_pembayaran}")


# ==========================================
# 9. PENJUALAN BERDASARKAN TANGGAL
# ==========================================

df_clean["Date"] = pd.to_datetime(df_clean["Date"])

penjualan_harian = (
    df_clean.groupby("Date")["Total"]
    .sum()
    .sort_index()
)

print("\n=== 9. PENJUALAN BERDASARKAN TANGGAL ===")
print(penjualan_harian)


# ==========================================
# 10. RATA-RATA TRANSAKSI
# ==========================================

rata_rata_transaksi = df_clean["Total"].mean()

print("\n=== 10. RATA-RATA TRANSAKSI ===")
print(f"Rata-rata transaksi : {rata_rata_transaksi:,.2f}")


# ==========================================
# 11. TOTAL LABA / GROSS INCOME
# ==========================================

total_laba = df_clean["gross income"].sum()

print("\n=== 11. TOTAL GROSS INCOME ===")
print(f"Total gross income : {total_laba:,.2f}")


# ==========================================
# 12. RATA-RATA RATING
# ==========================================

rata_rata_rating = df_clean["Rating"].mean()

print("\n=== 12. RATA-RATA RATING ===")
print(f"Rata-rata rating : {rata_rata_rating:.2f}")


# ==========================================
# STEP 7 — VISUALISASI DATA
# ==========================================

import matplotlib.pyplot as plt

print("\n===================================")
print("        STEP 7 — VISUALISASI")
print("===================================")

# ==========================================
# 1. PENJUALAN BERDASARKAN PRODUK
# ==========================================

penjualan_produk = (
    df_clean.groupby("Product line")["Total"]
    .sum()
    .sort_values(ascending=False)
)


# ==========================================
# 2. JUMLAH PRODUK TERJUAL
# ==========================================

jumlah_produk = (
    df_clean.groupby("Product line")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)
# ==========================================
# 3.penjualan berdasarkan cabang 
# ==========================================
penjualan_cabang = (
    df_clean.groupby("Branch")["Total"]
    .sum()
    
)
# ==========================================
# 4.Metode Pembayaran 
# ==========================================
Metode_Pembayaran = (
    df_clean.groupby("Payment").size()
)
# ==========================================
# 5.Jenis Pelanggan  
# =========================================
jenis_pelanggan = (
   df_clean.groupby("Customer type").size()
)

# ==========================================
# 6. Penjualan berdasarkan tanggal 
# =========================================
penjualan_harian = (
    df_clean.groupby("Date")["Total"]
    .sum()
    .sort_index()
)
# ==========================================
# 7. Gross income per product line 
# =========================================
gross_income_product =(
    df_clean.groupby("Product line")["gross income"]
    .sum()
    .sort_values(ascending=False)
)
# ==========================================
# 8. RATING SETIAP PRODUCT LINE
# ==========================================
rating_produk = (
    df_clean.groupby("Product line")["Rating"]
    .mean()
    .sort_values(ascending=False)
)

# ==========================================
# 3. VISUALISASI
# ==========================================

# Grafik 1
plt.figure(figsize=(10, 6))

penjualan_produk.plot(kind="bar", color="orange")

plt.title("Total Penjualan Berdasarkan Product Line")
plt.xlabel("Product Line")
plt.ylabel("Total Penjualan")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Grafik 2
plt.figure(figsize=(10, 6))

jumlah_produk.plot(kind="bar", color="orange")

plt.title("Jumlah Produk Terjual Berdasarkan Product Line")
plt.xlabel("Product Line")
plt.ylabel("Jumlah Produk Terjual")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
 
#Grafik 3 
plt.figure(figsize=(10, 6))
penjualan_cabang.plot(kind="bar", color="orange")

plt.title("Total penjualan Berdasarkan Cabang")
plt.xlabel("Cabang")
plt.ylabel("Total Penjualan")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Grafik 4 
plt.figure(figsize=(8,5))
Metode_Pembayaran.plot(kind="bar", color="orange")
plt.title("Metode Pembayaran")
plt.xlabel("Metode Pembayaran")
plt.ylabel("Jumlah Transaksi")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#Grafik 5
plt.figure(figsize=(8,5))
jenis_pelanggan.plot(kind="bar", color="orange")
plt.title("jumlah pelanggan berdasarkan customer type")
plt.xlabel("customer type")
plt.ylabel("Jumlah transaksi")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
 
#Grafik 6
plt.figure(figsize=(10, 6))

penjualan_harian.plot(kind="line",)

plt.title("Penjualan Berdasarkan Tanggal")
plt.xlabel("Tanggal")
plt.ylabel("Total Penjualan")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Grafik 7 
plt.figure(figsize=(10, 6))
gross_income_product.plot(kind="bar", color="orange")
plt.title("Gross Income Berdasarkan Product Line")
plt.xlabel("Product Line")
plt.ylabel("Gross Income")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Grafik 8 
plt.figure(figsize=(10, 6))
rating_produk.plot(kind="bar", color= "orange")
plt.title("Rata-rata Rating Berdasarkan Product Line")
plt.xlabel("Product Line")
plt.ylabel("Rata-rata Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ==========================================
# STEP 8 — MENCARI INSIGHT
# ==========================================

print("\n===================================")
print("          STEP 8 — INSIGHT")
print("===================================")

# 1.product line dengan jumlah tertinggi 
penjualan_produk = (
    df_clean.groupby("Product line")["Total"]
    .sum()
    .sort_values(ascending=False)
)


print("\n=== Product dengan penjualan tertinggi ===")
print("produuct line:", penjualan_produk.idxmax())
print("Total Penjualan:", penjualan_produk.max())

# 2. Product line dengan jumlah produk terbanyak terjual
produk_quantity_tertinggi = (
    df_clean.groupby("Product line")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== PRODUK DENGAN JUMLAH TERJUAL TERTINGGI ===")
print("Product line :", produk_quantity_tertinggi.idxmax())
print("Jumlah terjual :", produk_quantity_tertinggi.max())

# 3. Cabang dengan penjualan tertinggi
cabang_tertinggi = (
    df_clean.groupby("Branch")["Total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n=== CABANG DENGAN PENJUALAN TERTINGGI ===")
print("Cabang :", cabang_tertinggi.idxmax())
print("Total penjualan :", cabang_tertinggi.max())
# 4. Metode pembayaran terbanyak
pembayaran_terbanyak = df_clean["Payment"].value_counts()

print("\n=== METODE PEMBAYARAN TERBANYAK ===")
print("Metode :", pembayaran_terbanyak.idxmax())
print("Jumlah transaksi :", pembayaran_terbanyak.max())


# 5. Customer type terbanyak
customer_terbanyak = df_clean["Customer type"].value_counts()

print("\n=== CUSTOMER TYPE TERBANYAK ===")
print("Customer type :", customer_terbanyak.idxmax())
print("Jumlah transaksi :", customer_terbanyak.max())


# 6. Total gross income
total_gross_income = df_clean["gross income"].sum()

print("\n=== TOTAL GROSS INCOME ===")
print("Gross income :", total_gross_income)


# 7. Rata-rata rating
rata_rating = df_clean["Rating"].mean()

print("\n=== RATA-RATA RATING ===")
print("Rating :", round(rata_rating, 2))

# ==========================================
# STEP 9 — DASHBOARD
# ==========================================
fig = plt.figure(figsize=(16, 10))

fig.suptitle(
    "SUPERMARKET SALES DASHBOARD",
    fontsize=20,
    fontweight="bold"
)
