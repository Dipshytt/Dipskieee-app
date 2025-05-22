import streamlit as st

# Sidebar untuk navigasi
menu = st.sidebar.selectbox("Pilih Halaman", ["Home", "Halaman 1", "Halaman 2"])

# Tampilkan konten berdasarkan pilihan
if menu == "Home":
    st.title("Halaman Utama")
    st.write("Selamat datang di halaman utama.")

elif menu == "Halaman 1":
    st.title("Halaman 1")
    st.write("Ini konten halaman pertama.")

elif menu == "Halaman 2":
    st.title("Halaman 2")
    st.write("Ini konten halaman kedua.")

