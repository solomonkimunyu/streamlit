import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber pickups in New York")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text('Loading data... Done!')
data_load_state.text('Done! (using st.cache')

# st.subheader('Raw data')
# st.write(data)
if st.checkbox('show raw data'):
    st.subheader('Raw data')
    st.write(data)
hour = st.slider('hr', 0, 24, 4)
st.header("Number of pickups by hour")
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

if st.checkbox('Show hist values'):
    st.subheader("Histogram data")
    data[DATE_COLUMN].dt.hour
# st.subheader('Map of all pickups')
# st.map(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# hour_to_filter = 17
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)