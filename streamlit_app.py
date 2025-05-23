import streamlit as st

tab1, tab2, tab3, tab4 = st.tabs(["Home", "Ganjil/Genap", "TDL", "Games"])

with tab1:
    st.title("Halaman Utama")
    st.write("Selamat datang di halaman utama.")
    st.write( "Jika ingin keinginan terwujud, perbanyaklah bersujud 🤘😝🤘")
    st.write("[Coba Klik](https://youtu.be/2Iyj3CBsxTk)")
    st.image("IMG_20250421_152717_503.jpg", width=2000)
    ayang = st.text_input("nama orang diatas siapa 🫵😠")
    if ayang == "Eunchae":
                          st.write("bener 🥰")
    elif ayang == "":
        st.write("Tebak")
    else:
                          st.write("salah 😡")

with tab2:
    st.header("Aplikasi Ganjil Genap")
          
    angka = st.number_input("Tulis sebuah angka:", value=0, step=1)
    if (angka % 2) ==0:
      st.write(f"{angka} adalah Bilangan Genap")
    else:
      st.write(f"{angka} adalah Bilangan Ganjil")

with tab3:
    st.header("To Do List")
    mantap = (
        st.checkbox("Ngerjain tugas"),
        st.checkbox("ngedate sama ayang"),
        st.checkbox("menyelamatkan dunia"),
        st.checkbox("menjadi presiden Indonesia")
    )
    
    if mantap:
              st.write("mantap")
    else:
      pass
        
with tab4:
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
        st.image("31284410-3d-rendering-of-business-person-standing-with-correct-right-check-tick-mark-3d-illustration-of-human.jpg", width=2500)
    elif gagal:
        st.write(skibidi)
        st.image("d-sad-depressed-person-rendering-frustrated-man-sitting-plastic-stool-white-people-man-character-51186816.webp", width=2500)
    elif idle:
        st.write(slebew)
