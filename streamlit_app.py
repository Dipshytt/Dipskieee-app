import streamlit as st

st.title("Nadhif Safaraz Pranggana")
st.write( "Jika ingin keinginan terwujud, perbanyaklah bersujud 🤘😝🤘")
st.write("[Coba Klik](https://youtu.be/2Iyj3CBsxTk)")
st.image("IMG_20250421_152717_503.jpg", width=2000)
st.write("ayang aku 🥰🥰")
st.write("---")
st.header("Aplikasi Ganjil Genap")
          
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)
if (angka % 2) ==0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")

st.write("---")

st.header("To Do List")
mantap = st.checkbox("Ngerjain tugas")
mantap = st.checkbox("ngedate sama ayang")
mantap = st.checkbox("menyelamatkan dunia")
mantap = st.checkbox("menjadi presiden Indonesia")

if mantap:
          st.write("mantap")
else:
  pass

st.write("---")
st.header("gacha")

nomor = st.number_input("Pilih angka random", value=0, step=1)

sigma = ("selamat!!")
skibidi = ("ayo coba lagi")
slebew = ("Ayo Mulai")

berhasil = (nomor == 261008)
idle = (nomor == 0)
gagal = (nomor != 261008)
gagal = (nomor !=0)

if berhasil:
          st.write(sigma)
if gagal:
          st.write(skibidi)
if idle:
          st.write(slebew)

