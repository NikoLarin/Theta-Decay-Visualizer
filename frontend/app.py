import plotly.express as px
import numpy as np
import pandas as pd
import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))# Make Python find the theta_decay folder

from theta_decay.calculator import calculate_theta_decay

st.set_page_config(layout="wide")
st.title(body="Theta Decay Visualizer")

col1, col2 = st.columns([3,1]) # 3,1 being the % of the screen each col takes 75/25

with col2: # user inputs
    extrinsic_value = float(st.text_input("Extrinsic Value", value="10"))
    dte = st.slider("Days to Expiry", min_value=1, max_value=365, value=30)
    time_passed = st.slider("Days Passed", min_value=0, max_value=dte, value=0)

# Call the calculation from the other file
dates, theta_decay, current_value, theta = calculate_theta_decay(extrinsic_value, dte, time_passed)

df = pd.DataFrame()
df["Option_Value"] = np.round(theta_decay, 3) #create Option_Value in dataframe
df["Dates"] = dates[1:] #exclude the current hour, its useless
df.index = df["Dates"] #index by date
df.drop(columns=["Dates"], inplace=True)

with col2:
    st.write(f"Extrinsic Value: {current_value:.2f}")
    st.write(f"Daily Rate of Decay: {theta:.2f}")

with col1:
    fig = px.line(df)
    st.plotly_chart(fig, use_container_width=True)

multi = '''

## Theta Decay Visualizer

**Theta decay** often called "time decay" is the relentless enemy of option buyers and best friend of option sellers.

As time passes, the **extrinsic value** (the part of an option's price not explained by intrinsic value) naturally erodes, accelerating dramatically in the final weeks and days before expiration. This phenomenon is **exponential**.

### How Our Model Works

Our visualizer uses a **square-root decay model**, which closely mirrors real-world theta behavior:

- The remaining extrinsic value follows a **√(remaining time)** curve
- Decay is slow at first, then **explodes** as expiration approaches

### What You're Seeing

- **Blue Line**: The projected remaining extrinsic value over time
- **Steep drop near the end**: The aggressive acceleration of theta decay in the final days
- **Daily Rate of Decay**: How much extrinsic value is expected to vanish each day

'''

st.markdown(multi)
