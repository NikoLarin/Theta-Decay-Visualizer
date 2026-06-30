import numpy as np
import streamlit as st
import plotly.express as px
from datetime import datetime, timedelta
import math

def get_data():
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

    theta = -extrinsic_value / (2 * dte * np.sqrt(1 - time_passed/dte))

    theta_decay = np.sqrt((dte - time_range) / dte) * extrinsic_value

    return theta_decay, time_range, theta

