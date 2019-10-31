import pandas as pd
import numpy as np
import streamlit as st

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.header('DataFrame HighLight')
st.dataframe(df.style.highlight_max(axis=0))

df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5)))

st.header('Table')
st.table(df)