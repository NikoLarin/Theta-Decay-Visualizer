import numpy as np
import pandas as pd
import math
from datetime import datetime, timedelta

def calculate_theta_decay(extrinsic_value :float, dte :str, time_passed :int):
    """All calculation logic
    This will create variables for
        now - the current date and hour, setting the minutes/seconds to 0
        exp - the expiration date and hour, setting the miunites/seconds to 0
        hours - the amount of hours until expiry
        dates - every date and hour from now until expiry
    
        theta_decay - create exponential decay values
        current_value - extrinsic value - theta_decay
        
    """
    
    dates = []
    now = datetime.now().replace(minute = 0, second = 0, microsecond = 0) # create var for current hour
    exp = (now + timedelta(hours= dte * 24)).replace(hour = 16, minute = 0, second = 0, microsecond = 0) # create var for expiration date
    hours = math.ceil((exp - now).total_seconds() / 3600) # find amount of hours until expiry
    
    current_time = now # stage current_time for loop
    
    while current_time <= exp: # loop increments time by hour until expiry hour is met
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