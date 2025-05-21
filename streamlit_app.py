import streamlit as st

st.title("Nadhif Safaraz Pranggana")
st.write( "Jika ingin keinginan terwujud, perbanyaklah bersujud 🤘😝🤘")

st.image("IMG_20250313_194334_316.jpg", width=2000)

angka = st.number_input("Tulis sebuah angka:", value=0, step=1)


if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")

st.title("tes")

st.text_input("Masukan Nama:", value=0)
