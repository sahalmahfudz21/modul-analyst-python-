
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Konfigurasi halaman
st.set_page_config(
    page_title="Dashboard Data Analyst",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Data Analyst")
st.write("Dashboard Analisis Data Menggunakan Python")

# Upload dataset
file = st.file_uploader(
    "Masukkan dataset CSV atau Excel",
    type=["csv", "xlsx"]
)

if file is not None:

    # Membaca dataset
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    # Membersihkan nama kolom
    df.columns = df.columns.str.strip()

    st.subheader("1. Informasi Dataset")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Baris", len(df))

    with col2:
        st.metric("Total Kolom", len(df.columns))

    with col3:
        st.metric(
            "Data Kosong",
            int(df.isnull().sum().sum())
        )

    # Menampilkan data
    st.subheader("2. Preview Dataset")
    st.dataframe(df.head(20), use_container_width=True)

    # Statistik
    st.subheader("3. Statistik Data")
    st.dataframe(
        df.describe(),
        use_container_width=True
    )

    # Memilih kolom numerik
    numeric_columns = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if numeric_columns:

        st.subheader("4. Analisis Visualisasi")

        selected_column = st.selectbox(
            "Pilih kolom yang ingin dianalisis",
            numeric_columns
        )

        col4, col5 = st.columns(2)

        with col4:
            st.metric(
                "Total",
                f"{df[selected_column].sum():,.2f}"
            )

        with col5:
            st.metric(
                "Rata-rata",
                f"{df[selected_column].mean():,.2f}"
            )

        # Grafik batang
        st.subheader("5. Grafik Distribusi")

        fig, ax = plt.subplots(figsize=(10, 5))

        df[selected_column].dropna().plot(
            kind="hist",
            bins=15,
            ax=ax
        )

        ax.set_title(
            f"Distribusi {selected_column}"
        )
        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frekuensi")

        st.pyplot(fig)

        # Korelasi
        st.subheader("6. Korelasi Antarvariabel")

        if len(numeric_columns) >= 2:
            correlation = df[numeric_columns].corr()

            fig2, ax2 = plt.subplots(figsize=(9, 5))

            import seaborn as sns

            sns.heatmap(
                correlation,
                annot=True,
                cmap="coolwarm",
                ax=ax2
            )

            st.pyplot(fig2)

    else:
        st.warning("Dataset tidak memiliki kolom numerik.")

else:
    st.info("Silakan upload dataset terlebih dahulu.")

