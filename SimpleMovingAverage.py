import matplotlib.pyplot as plt
import numpy as np
import random

random_nbr_series=[1]
for x in range(1,1000):
	random_nbr_series.append(random_nbr_series[-1]+random_nbr_series[-1]*random.randint(-4,4)/100)
	
	
randomseries=random_nbr_series
period=50
#funzione che restituisce media mobile di una serie
def sma(numbers,days):
	mm=[]
	
#initialize list, with a x number of zeroes equal to the number of period just to let the First movin avarege data, sfart at the right place 	
	for num in range(0,days-1):
		mm.append(0)
# for each number in the list, calculate a x period moving avarage.	
	for x in range (days,len(numbers)+1):
		media=sum(numbers[(x-days):x])/days
		mm.append(media)
	return mm

a =sma(randomseries,period)

plt.figure()
plt.plot(a[period:])
plt.plot(random_nbr_series[period:])
plt.show()

