import requests

import streamlit as st

from settings import API_URL, TITLE
from components import build_data_plot
label_area="Select the price areas: DK1 and DK2."
label_consumer_type="Select the code used by  energy companies."


st.set_page_config(page_title=TITLE)
st.title(TITLE)


# Create dropdown for area selection.
area_response = requests.get(API_URL / "area_values")

area = st.sidebar.selectbox(
    label=label_area,
    options=area_response.json().get("values", []),
)

# Create dropdown for consumer type selection.
consumer_type_response = requests.get(API_URL / "consumer_type_values")

consumer_type = st.sidebar.selectbox(
    label=label_consumer_type,
    options=consumer_type_response.json().get("values", []),
)


# Check if both area and consumer type have values listed, then create plot for data.
if area and consumer_type:
    st.plotly_chart(build_data_plot(area, consumer_type))
