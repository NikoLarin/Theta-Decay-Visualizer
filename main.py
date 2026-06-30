import numpy as np
import pandas as pd
import math
import plotly.express as px
from datetime import datetime, timedelta
from shared import extrinsic_value, dte, time_passed


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

# Current value
current_value = np.sqrt((dte - time_passed) / dte) * extrinsic_value

# Estimate theta
theta = -extrinsic_value / (2 * dte * np.sqrt(1 - time_passed/dte))
