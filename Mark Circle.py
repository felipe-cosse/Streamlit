import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['X', 'Y', 'Size'])

c = alt.Chart(df).mark_circle().encode(
     x='X', y='Y', size='Size', color='Size')

st.write(c)