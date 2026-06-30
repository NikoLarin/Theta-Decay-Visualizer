import numpy as np
import pandas as pd
import math
from datetime import datetime, timedelta

def calculate_theta_decay(extrinsic_value, dte, time_passed):
    """All your calculation logic"""
    
    dates = []
    now = datetime.now().replace(minute = 0, second = 0, microsecond = 0)
    exp = (now + timedelta(hours= dte * 24)).replace(hour = 16, minute = 0, second = 0, microsecond = 0)
    hours = math.ceil((exp - now).total_seconds() / 3600)
    current_time = now
    while current_time <= exp:
        dates.append(current_time)
        current_time += timedelta(hours=1)

    # Full time range (0 to expiry)
    time_range = np.linspace(0, dte, hours)

    # Square root decay model
    theta_decay = np.sqrt((dte - time_range) / dte) * extrinsic_value

    # Current value
    current_value = np.sqrt((dte - time_passed) / dte) * extrinsic_value

    # Estimate theta
    theta = -extrinsic_value / (2 * dte * np.sqrt(1 - time_passed/dte))

    return dates, theta_decay, current_value, theta