import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from shared import dates, get_data

theta_decay, time_range, theta = get_data()

df = pd.DataFrame()
df["Option_Value"] = np.round(theta_decay,3)
df["Dates"] = dates[1:]
df.index=df["Dates"]
df.drop(columns=["Dates"], inplace=True)


st.set_page_config(layout="wide")
st.title(body="Theta Decay Visualizer")

col1, col2 = st.columns([3,1])

with col2:
    extrinsic_value = float(st.text_input("Extrinsic Value", value="10"))
    dte = st.slider("Days to Expiry", min_value=1, max_value=365, value=30)
    time_passed = st.slider("Days Passed", min_value=0, max_value=dte, value=0)

    current_value = np.sqrt((dte - time_passed) / dte) * extrinsic_value


with col1:
    fig = px.line(df)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.write(f"Extrinsic Value: {current_value:.2f}")
    st.write(f"Daily Rate of Decay: {theta:.2f}")

