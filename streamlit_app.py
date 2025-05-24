import streamlit as st
import random

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Ganjil/Genap", "TDL", "Games", "TESTING"])

with tab1:
    st.title("Halaman Utama")
    st.write("Selamat datang di halaman utama.")
    st.write( "Jika ingin keinginan terwujud, perbanyaklah bersujud 🤘😝🤘")
    st.write("[Coba Klik](https://youtu.be/2Iyj3CBsxTk)")
    st.image("IMG_20250522_091017.jpg", width=2000)
    Botak = st.text_input("nama orang diatas siapa 🫵😠")
    if Botak == "GANIBOTAK":
                          st.write("bener 🥰")
    elif Botak == "":
        st.write("Tebak")
    else:
                          st.write("salah 😡")

with tab2:
    st.title("Aplikasi Ganjil Genap")
          
    angka = st.number_input("Tulis sebuah angka:", value=0, step=1)
    if (angka % 2) ==0:
      st.write(f"{angka} adalah Bilangan Genap")
    else:
      st.write(f"{angka} adalah Bilangan Ganjil")

with tab3:
    st.title("To Do List")
    mantap1 = st.checkbox("Ngerjain tugas")
    mantap2 = st.checkbox("ngedate sama ayang")
    mantap3 = st.checkbox("menyelamatkan dunia")
    mantap4 = st.checkbox("menjadi presiden Indonesia")

    
    if mantap1 and mantap2 and mantap3 and mantap4:
              st.write("mantap")
    else:
      pass
        
with tab4:
    st.title("Gacha")

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

with tab5:
    st.title("TESTING")

    gambar = st.camera_input("jepret")

   
if 'button' not in st.session_state:
    st.session_state.button = False

def click_button():
    st.session_state.button = not st.session_state.button

st.button('tes', on_click=click_button)

if st.session_state.button:
    st.write('mantap')
else:
    st.write('Button is off!')

