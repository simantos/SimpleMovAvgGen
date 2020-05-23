import requests
import json
import pandas as pd
import datetime
import mplfinance as mpf
import matplotlib.pyplot as plt

reformatted_data = dict()
reformatted_data =  {'Date': [datetime.datetime(2020, 5, 12, 22, 0), datetime.datetime(2020, 5, 12, 21, 55), datetime.datetime(2020, 5, 12, 21, 50)], 'Open': [8790.89, 8858.39, 8858.16], 'High': [8822.88, 8862.0, 8862.83], 'Low': [8784.21, 8771.49, 8842.95], 'Close': [8785.81, 8791.05, 8858.39], 'Volume': [2088885.6625679892, 2593074.0121658784, 848033.7015745327]}
pdata = pd.DataFrame(reformatted_data) 
pdata.set_index('Date', inplace=True)
mpf.plot(pdata)
