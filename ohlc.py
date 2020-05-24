import random
import pandas as pd
import datetime
from datetime import timedelta
import requests
import json
import mplfinance as mpf
import matplotlib.pyplot as plt

open=[1]
high =[1]
volume=[0]
low=[1]
close=[1]
dates=[datetime.datetime(1900,1,1)]

n=200

#Generates n day length series with a  +/- daily % variation.
for x in range(1,n):
	dates.append(dates[-1]+timedelta(days=1))
	
	open_value=(open[-1]+open[-1]*random.uniform(-3.0,3.0)/100)
	open.append(open_value)
	
	close_value=(open[-2]+open[-2]*random.uniform(-3.0,3.0)/100)
	close.append(close_value)
	
	high.append(max(open_value,close_value,open_value+open_value*random.uniform(0.1,2.5)/100))
	
	low.append(min(open_value, close_value,open_value+open_value*random.uniform(-2.5,-0.1)/100))
	
	volume.append(0)
	#print("open {a}, high {b}, low {c},  {d}\n".format(a=open[-1],b=high[-1],c= low[-1],d=close[-1]))

quotes_dict={'Date':dates,'Open':open,'High':high, 'Low':low,'Close':close,'Volume':volume}
#print((quotes_dict))
seriedati=pd.DataFrame(quotes_dict)
#print(seriedati)
seriedati.set_index('Date', inplace=True)
mpf.plot(seriedati[1:])
