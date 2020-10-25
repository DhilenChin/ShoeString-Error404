import pandas as pd 
import numpy as np
import datetime
import matplotlib
from matplotlib.dates import date2num

def frequency_addition(nodes):
    now = datetime.now()
    now = matplotlib.dates.date2num(now)
    for i in len(nodes.date_list):
        a_week_ago = now - 7
        if nodes.date_list[i] >= a_week_ago:
            time_int = now - nodes.date_list[i]
            frequency = len(nodes.date_list[i:])/time_int
            break
    if frequency > 4/7:
        nodes.points = maximum_nodes_point + 1

    return None

