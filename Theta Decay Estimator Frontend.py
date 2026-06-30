import streamlit as st
import numpy as np
import pandas as pd
import math
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(layout="wide")
st.title(body="Theta Decay Visualizer")

col1, col2 = st.columns([3,1])

with col2:
    extrinsic_value = float(st.text_input("Extrinsic Value", value="10"))
    dte = st.slider("Days to Expiry", min_value=1, max_value=365, value=30)
    time_passed = st.slider("Days Passed", min_value=0, max_value=dte, value=0)

    
dates = []
now = datetime.now().replace(minute = 0, second = 0, microsecond = 0)
exp = (now + timedelta(hours= dte * 24)).replace(hour = 16, minute = 0, second = 0, microsecond = 0)
hours = math.ceil((exp - now).total_seconds() / 3600)
current_time = now
while current_time <= exp:
    dates.append(current_time)
    current_time += timedelta(hours=1)
    #print(current_time)


# Full time range (0 to expiry)
time_range = np.linspace(0, dte, hours)

# Square root decay model
theta_decay = np.sqrt((dte - time_range) / dte) * extrinsic_value

# Current value
current_value = np.sqrt((dte - time_passed) / dte) * extrinsic_value

# Estimate theta
theta = -extrinsic_value / (2 * dte * np.sqrt(1 - time_passed/dte))

with col2:
    st.write(f"Extrinsic Value: {current_value:.2f}")
    st.write(f"Daily Rate of Decay: {theta:.2f}")

df = pd.DataFrame()
df["Option_Value"] = np.round(theta_decay,3)
df["Dates"] = dates[1:]
df.index=df["Dates"]
df.drop(columns=["Dates"], inplace=True)

print(df)
with col1:

    fig = px.line(df)
    st.plotly_chart(fig, use_container_width=True)
