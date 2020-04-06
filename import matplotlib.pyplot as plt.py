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

w = st.file_uploader("Upload a CSV file", type="csv")
if w:
    import pandas as pd

    data = pd.read_csv(w)
    st.write(data)

# Load data from csv file
data = pd.read_csv('journey_locations.csv')

# How many rows in the dataset
print('How many rows the dataset: ', data['id'].count() )


# How many updates are there for each journey_id?
print('How many updates are there for each journey_id: ')
print( data['journey_id'].value_counts() )


# Tip: Take the data from the first entry and the last entry
# Tip: Plot them into ____.gl to have a visual of the trips.

# Get the first entry for each journey_id
sys.stdout=open("testfirst.txt","w")
print( data.groupby('journey_id').first() )
sys.stdout.close()

# Get the last entry for each journey_id
sys.stdout=open("testlast.txt","w")
print( data.groupby('journey_id').last() )
sys.stdout.close()


