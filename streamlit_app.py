import streamlit as st

st.title("Hello World")

import streamlit as st
import pandas as pd
 
st.write(pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
}))

import streamlit as st 
 
st.markdown(
    """
    # My Ariel
    Hello, para calon praktisi data masa depan!
    """
)

import streamlit as st
 
st.title('Belajar Analisis Data')

import streamlit as st
 
st.header('Pengembangan Dashboard')

import streamlit as st
 
st.subheader('Pengembangan Dashboard')

import streamlit as st
 
st.caption('Copyright (c) 2023')

import streamlit as st
 
code = """def hello():
    print("Hello, Streamlit!")"""
st.code(code, language='python')

import streamlit as st
 
st.text('Halo, calon praktisi data masa depan.')

import streamlit as st
 
st.latex(r"""
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
""")

import pandas as pd
import streamlit as st 
 
df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [10, 20, 30, 40],
})
st.table(data=df)
