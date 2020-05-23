import random
import pandas as pd
open=[1]
high =[1]
low=[1]
close=[1]
n=30

#Generates n day length series with a  +/- daily % variation.
for x in range(1,n):
	open.append(open[-1]+open[-1]*random.randint(-3,3)/100)
	high.append((open[-1]+open[-1]*random.randint(0,4)/100))
	low.append((open[-1]+open[-1]*random.randint(-4,0)/100))
	close.append((open[-1]+open[-1]*random.randint(-3,3)/100))
	print("open {a}, high {b}, low {c},  {d}\n".format(a=open[-1],b=high[-1],c= low[-1],d=close[-1]))