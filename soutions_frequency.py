import pandas as pd 
import numpy as np
from datetime import date
import matplotlib
from matplotlib.dates import date2num

def frequency_addition(nodes):
    now = date.today()
    now = matplotlib.dates.date2num(now)
    for i in range(len(nodes.datelist)):
        a_week_ago = now - 7
        if nodes.datelist[i] >= a_week_ago:
            time_int = now - nodes.datelist[i]
            frequency = len(nodes.datelist[i:])/time_int
            break
    if frequency > 4/7:
        nodes.score += 2

    return None

