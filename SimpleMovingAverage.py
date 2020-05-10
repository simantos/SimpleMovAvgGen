import numpy as np
import random
random_nbr_series=[]
for x in range(1000):
	random_nbr_series.append(random.randint(10,400))
	
randomseries=random_nbr_series
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

a =sma(randomseries,2)

print (a)

