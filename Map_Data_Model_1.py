import pandas as pd
import streamlit as st
import numpy as np



#Mapping
my_dataset = 'journey_locations.csv'
DATE_TIME = "date/time"


def load_data(nrows):
    data = pd.read_csv(my_dataset, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data


data = load_data(100000)

hour = st.slider('selected hour')
data = data[data[DATE_TIME].dt.hour == hour]

if st.checkbox('view_data'):
    st.subheader('Raw Data at %sh' % hour)
    st.write(data)

st.subheader('Data by minute at %sh' % hour)
st.bar_chart(np.histogram(data[DATE_TIME].dt.minute, bins=360, range=(0,360))[0])

st.subheader('Geo Data at %sh' % hour)
st.map(data)