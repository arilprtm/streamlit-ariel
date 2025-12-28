import streamlit as st
 
st.title('Pemerograman Dasar')

import streamlit as st
 
st.header('Pembelajaran Pengenalan Streamlit dan Cara Membuat Web dengan Streamlit')

import streamlit as st
 
st.subheader('Ariel Akdes Pratama 4232401038')

import streamlit as st
 
st.caption('Dibuat oleh Ariel')

import streamlit as st
 
def jurusan():
        prit("Teknik Elektro")

import streamlit as st
 
st.text('Halo semuanya, perkenalkan saya ariel akdes pratama saya merupakan mahasiswa politeknik negeri batam semester 3, jurusan saya adalah teknik elektro sedangkan prodi saya adalah teknologi rekayasa pembangkit energi dan sebagai mahasiswa saya belajar salah satunya tentang pemoragraman dasar yaitu pengenalan streamlit dan cara membuat web dengan streamlit,  ini adalah Web analisis menggunakan library Streamlit dan menggunakan bahasa pemerograman Python')



import streamlit as st
 
st.text('Ini adalah table untuk analisis')

import pandas as pd
import streamlit as st 
 
df = pd.DataFrame({
    'Negara': ["Indonesia", "Thailand", "Malaysia", "Singapura", "Vietnam", "Philipina"],
    'Jumlah Medali': [20, 16, 15, 12, 9, 7],
})
st.table(data=df) 

import streamlit as st
 
st.subheader('Grafik 6 Negara Dengan Medali Terbanyak')


import streamlit as st
import pandas as pd
 
st.bar_chart(df.set_index("Negara")["Jumlah Medali"])


