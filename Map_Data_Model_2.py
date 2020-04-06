import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image
import pandas as pd
import streamlit as st
import graphviz as graphviz
import numpy as np
import pydeck as pdk
import altair as alt


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
'data', data

hour = st.slider("Hour to look at", 0, 23)

data = data[data[DATE_TIME].dt.hour == hour]

st.subheader("Geo data between %i:00 and %i:00" % (hour, (hour + 1) % 24))
midpoint = (np.average(data["lat"]), np.average(data["lon"]))

st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
    },
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=data,
            get_position=["lon", "lat"],
            radius=100,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
))


if st.checkbox("Show raw data", False):
    st.subheader("Raw data by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))
    st.write(data)






# Title/text
st.title("Data_Aggregation")


# Headers and Subheader
st.header("text to be updated")
st.subheader("text to be updated")

#DataFrame

my_dataset = 'journey_locations01.csv'
    
#Function to explore the dataset
@st.cache(persist=True)
def explore_data(dataset):
    df = pd.read_csv(os.path.join(my_dataset))
    return df
data = explore_data(my_dataset)

if st.checkbox("Preview Dataset"):
    #data = explore_data(my_dataset)
    if st.button("Head"):
        st.write(data.head())
    elif st.button("Tail"):
        st.write(data.tail())
    else: 
        st.write(data.head(2))

# Show the entire dataset
if st.checkbox("Show all the dataset"):
    #data = explore_data(my_dataset)
    #st.write(data)
    st.dataframe(data)


#Show Column Name
if st.checkbox("Show columns of the dataset"):
    st.write(data.columns)

#Show Dimensions
data_dim = st.radio("Select your preffered dimensions",("Rows","Columns","All"))
if data_dim == 'Rows':
    st.text("Showing Rows")
    st.write(data.shape[0])
elif data_dim == 'Columns':
    st.text("Showing Columns")
    st.write(data.shape[1])
else:
    st.text("Showing Shape of Dataset")
    st.write(data.shape)



#Show Summary
if st.checkbox("Show summary of the dataset"):
    st.write(data.describe())
    
#Select a columns

col_option = st.selectbox("Select Column", ("id","journey_id","lat","lng","created_at","updated_at"))
if col_option == 'id':
    st.write(data['id'])
elif col_option == 'journey_id':
    st.write(data['journey_id'])
elif col_option == 'lat':
    st.write(data['lat'])
elif col_option == 'lng':
    st.write(data['lng'])
elif col_option == 'created_at':
    st.write(data['created_at'])
elif col_option == 'id':
    st.write(data['id'])
else:
    st.write("Select Column")
#Plot
#Show Summary

if st.checkbox("Show Bar Plot with Matplotlib"):
    st.write(data.plot(kind='bar'))
    st.pyplot()


#Correlation
if st.checkbox("Show Correlation with Matplotlib"):
    plt.matshow(data.corr())
    st.pyplot()


#Correlation
if st.checkbox("Show Correlation Plot with Seaborn"):
    st.write(sns.heatmap(data.corr()))
    st.pyplot()
    


#Group
if st.checkbox("Show Bar Chart Plot by default"):
    v_group = data.groupby('date/time')
    st.bar_chart(v_group)

#Group
if st.checkbox("Show Line Plot by default"):
    #v_group = data.groupby('journey_id')
    st.line_chart(v_group)

#Group
if st.checkbox("Show Area Chart Plot by default"):
    v_group = data.groupby('journey_id')
    st.area_chart(v_group)