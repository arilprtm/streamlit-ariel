import streamlit as st
 
st.title('Pemerograman Dasar Menggunakan Bahasa Python')

import streamlit as st
 
st.header('Belajar Membuat Web Dengan Streamlit dan Bahasa Python')

import streamlit as st
 
st.subheader('Ariel Akdes Pratama 4232401038')

import streamlit as st
 
st.caption('Dibuat oleh Ariel')

import streamlit as st
 
def jurusan():
        prit("Teknik Elektro")

import streamlit as st
 
st.text('Hallo semuanya!! Perkenalkan nama saya Ariel Akdes Pratama umur saya 20 tahun, saya sekarang sedang berkuliah di Politeknik Negeri Batam, dengan jurusan Teknik Elektro, Prodi D4 Teknologi Rekayasa Pembangkit Energi, dengan kelas B Pagi, ini adalah Web analisis menggunakan library Streamlit dan menggunakan bahasa pemerograman Python.')



import streamlit as st
 
st.text('Ini adalah table untuk analisis')

import pandas as pd
import streamlit as st 
 
df = pd.DataFrame({
    'Team': ["Indonesia", "Thailand", "Malaysia", "Singapura", "Vietnam", "Philipina"],
    'Juara': [20, 16, 15, 12, 9, 7],
})
st.table(data=df) 

import streamlit as st
 
st.subheader('Grafik 5 Negara Dengan Juara Terbanyak')


import streamlit as st
import pandas as pd
 
st.bar_chart(df.set_index("Team")["Juara"])


