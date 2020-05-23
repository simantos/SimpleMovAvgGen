#Simple Random Moving Average Line Chart.
#Line chart is randomly generated in accordance with  the given desidered lenght of the series (n) and the desidered Max % daily variation  on the the previous  value (daily_upper_range_max_perc and daily_lower_ran).
#once the line chart has been plotted, three different Simple moving averages are calculated and added to the chart.

import matplotlib.pyplot as plt
import numpy as np
import random

n=500
daily_upper_range_perc=2
daily_lower_range_perc=-2
SMA1=25
SMA2=50
SMA3=100


#initialise the series with a fiction value of 1 
random_nbr_series=[1]

#Generates n length series with thendesaity max daily % variation.
for x in range(1,n):
	random_nbr_series.append(random_nbr_series[-1]+random_nbr_series[-1]*random.randint(daily_lower_range_perc,daily_upper_range_perc)/100)
	
	
randomseries=random_nbr_series
period=50
#funzione che restituisce media mobile di una serie
def sma(numbers,days):
	mm=[]
	
#initialize list, with a x number of zeroes equal to the number of period just to let the First movin avarege data, sfart at the right place 	
	#for num in range(0,days-1):
	#	mm.append(0)
# for each number in the list, calculate a x period moving avarage.	
	for x in range (days,len(numbers)+1):
		media=sum(numbers[(x-days):x])/days
		mm.append(media)
	return mm

a =sma(randomseries,period)
b =sma(randomseries,period-30)

plt.figure()
plt.plot(np.arange(0,len(random_nbr_series),1), random_nbr_series, color='g')
plt.plot(np.arange(period,len(a)+period,1), a, color='r')
plt.plot(np.arange(period-30,len(b)+period-30,1), b, color='b')

plt.show()

