import streamlit as st

# Sidebar untuk navigasi
menu = st.sidebar.selectbox("Pilih Halaman", ["Home", "Aplikasi Ganjil Genap", "To Do List", "Games"])

# Tampilkan konten berdasarkan pilihan
if menu == "Home":
    st.title("Halaman Utama")
    st.write("Selamat datang di halaman utama.")
    st.write( "Jika ingin keinginan terwujud, perbanyaklah bersujud 🤘😝🤘")
    st.write("[Coba Klik](https://youtu.be/2Iyj3CBsxTk)")
    st.image("IMG_20250421_152717_503.jpg", width=2000)
    ayang = st.text_input("nama orang diatas siapa 🫵😠")
    if ayang == "eunchae":
                          st.write("bener 🥰")
    else:
                          st.write("salah 😡")

elif menu == "Aplikasi Ganjil Genap":
    st.header("Aplikasi Ganjil Genap")
          
    angka = st.number_input("Tulis sebuah angka:", value=0, step=1)
    if (angka % 2) ==0:
      st.write(f"{angka} adalah Bilangan Genap")
    else:
      st.write(f"{angka} adalah Bilangan Ganjil")

elif menu == "To Do List":
    st.header("To Do List")
    mantap = st.checkbox("Ngerjain tugas")
    mantap = st.checkbox("ngedate sama ayang")
    mantap = st.checkbox("menyelamatkan dunia")
    mantap = st.checkbox("menjadi presiden Indonesia")

    if mantap:
              st.write("mantap")
    else:
      pass
        
elif menu == "Games":
    st.header("Gacha")

    nomor = st.number_input("Pilih angka random antara 1-100", value=0, step=1, min_value=0, max_value=100)

    sigma = ("selamat!!")
    skibidi = ("ayo coba lagi")
    slebew = ("Ayo Mulai")

    berhasil = (nomor == 26)
    idle = (nomor == 0)
    gagal = (nomor != 'berhasil' and nomor != 0)

    if berhasil:
        st.write(sigma)
    elif gagal:
        st.write(skibidi)
    elif idle:
        st.write(slebew)



