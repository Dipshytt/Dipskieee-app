import streamlit as st

st.title("Nadhif Safaraz Pranggana")
st.write( "Jika ingin keinginan terwujud, perbanyaklah bersujud 🤘😝🤘")
st.write("[Coba Klik](https://youtu.be/2Iyj3CBsxTk)")
st.image("IMG_20250421_152717_503.jpg", width=2000)
st.write("bubub aku 🥰🥰")
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
mantap = st.checkbox("ngedate sama bubub")
mantap = st.checkbox("menyelamatkan dunia")
mantap = st.checkbox("menjadi presiden Indonesia")


if mantap:
          st.write("mantap")
else:
  pass

st.write("---")
st.header("gacha")
gacor = st.number_input("Pilih angka random", value=0, step=1)
st.write("ayo mulai")
status = "ayo mulai"
if gacor == 275:
  status = st.status.replace("ayo mulai", "gacor kang")

else:
  status = st.status.replace("ayo mulai" or "gacor kang", "coba lagi")

