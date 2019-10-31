import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.figure_factory as ff
from bokeh.plotting import figure

arr = np.random.normal(1, 1, size=100)
plt.hist(arr, bins=20)

st.header('Hist')
st.pyplot()

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
         hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.header('PyPlot')
st.plotly_chart(fig)


x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend='Trend', line_width=2)

st.header('Bokeh Charts')
st.bokeh_chart(p)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.header('')
st.deck_gl_chart(layers = [{
        'data': df,
        'type': 'ScatterplotLayer'
    }])
