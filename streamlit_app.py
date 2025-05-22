import streamlit as st

st.title("Nadhif Safaraz Pranggana")
st.write( "Jika ingin keinginan terwujud, perbanyaklah bersujud 🤘😝🤘")

st.image("IMG_20250421_152717_503.jpg", width=2000)
st.markdown("---")
st.header("Aplikasi Ganjil Genap")
          
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)
if (angka % 2) ==0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
