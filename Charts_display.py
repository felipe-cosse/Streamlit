import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
from bokeh.plotting import figure
import graphviz as graphviz

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
st.deck_gl_chart(
     viewport={
         'latitude': 37.76,
         'longitude': -122.4,
         'zoom': 11,
         'pitch': 50,
     },
     layers=[{
         'type': 'HexagonLayer',
         'data': df,
         'radius': 200,
         'elevationScale': 4,
         'elevationRange': [0, 1000],
         'pickable': True,
         'extruded': True,
     }, {
         'type': 'ScatterplotLayer',
         'data': df,
     }])

# Create a graphlib graph object
st.header('Graphviz Chart')

st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

chart_data_line = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.header('Line Chart')
st.line_chart(chart_data_line)

chart_data_area = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.header('Area Chart')
st.area_chart(chart_data_area)


chart_data_bar = pd.DataFrame(
     [[20, 30, 50]],
     columns=['a', 'b', 'c'])
st.header('Bar Chart')
st.bar_chart(chart_data_bar)


df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
     columns=['lat', 'lon'])
st.header('Map')
st.map(df)