import pandas as pd

file = "Data Supermarket-Latihan.xlsx"

# Membaca nama semua sheet
excel = pd.ExcelFile(file)

print("=== DAFTAR SHEET ===")
print(excel.sheet_names)


# ==========================================
# CEK SHEET 1
# ==========================================

df_sheet1 = pd.read_excel(file, sheet_name="Sheet1")

print("\n===================================")
print("           SHEET 1")
print("===================================")

print("\n=== NAMA KOLOM SHEET 1 ===")
print(df_sheet1.columns.tolist())

print("\n=== 10 DATA PERTAMA SHEET 1 ===")
print(df_sheet1.head(10).to_string())

print("\n=== UKURAN SHEET 1 ===")
print(df_sheet1.shape)


# ==========================================
# CEK SHEET 3
# ==========================================

df_sheet3 = pd.read_excel(file, sheet_name="Sheet3 ")

print("\n===================================")
print("           SHEET 3")
print("===================================")

print("\n=== NAMA KOLOM SHEET 3 ===")
print(df_sheet3.columns.tolist())

print("\n=== 10 DATA PERTAMA SHEET 3 ===")
print(df_sheet3.head(10).to_string())

print("\n=== UKURAN SHEET 3 ===")
print(df_sheet3.shape)

import pandas as pd

df = pd.read_excel(
    "Data Supermarket-Latihan.xlsx",
    sheet_name="Sheet1"
)
df_clean = df.copy()