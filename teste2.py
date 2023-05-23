import streamlit as st 
import pandas as pd 
import numpy as np

st.title('teste ECMI 2')

st.write("tabela")

dataframe = pd.DataFrame({
'Nome' : ['churrin' , 'ch' , 'bruno'],
'salário': [100, 200, 300]
})
dataframe.style.highlight_max(axis=0)

st.write(dataframe)

chart_data = pd.DataFrame(
np.random.randn(20, 3),
columns = ['a', 'b','c'])

st.line_chart(chart_data)

st.bar_chart(chart_data)
