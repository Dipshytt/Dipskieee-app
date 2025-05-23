import streamlit as st

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")


    tab1.title("Halaman Utama")
    tab1.write("Selamat datang di halaman utama.")
    tab1.write( "Jika ingin keinginan terwujud, perbanyaklah bersujud 🤘😝🤘")
    tab1.write("[Coba Klik](https://youtu.be/2Iyj3CBsxTk)")
    tab1.image("IMG_20250421_152717_503.jpg", width=2000)
    ayang = tab1.text_input("nama orang diatas siapa 🫵😠")
    if ayang == "Eunchae":
                          tab1.write("bener 🥰")
    elif ayang == "":
        tab1.write("Tebak")
    else:
                          tab1.write("salah 😡")

    tab1.image_input
    
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



