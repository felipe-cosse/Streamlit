import streamlit as st
import datetime

st.header('Button')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

st.header('Checkbox')
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')

st.header('Radio')
genre = st.radio(
    'Whats your favorite movie genre',
    ('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write('You didnt select comedy.')


st.header('SelectBox')
option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)


st.header('Multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ('Green', 'Yellow', 'Red', 'Blue'))
st.write('You selected:', options)

st.header('Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.header('Slider Range')
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


st.header('Text Input')
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)


st.header('Number Input')
number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.header('Text Area')
txt = st.text_area('Text to analyze', '''
     It was the best of times, it was the worst of times, it was
     the age of wisdom, it was the age of foolishness, it was
     the epoch of belief, it was the epoch of incredulity, it
     was the season of Light, it was the season of Darkness, it
     was the spring of hope, it was the winter of despair, (...)
     ''')
st.write('Sentiment:', txt)

st.header('Date Input')
d = st.date_input(
    'Whens your birthday',
    datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


st.header('Time Input')
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)