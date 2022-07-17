#Import third-party libraries
import numpy as np 
import matplotlib.pyplot as plt 
from decimal import *
import random
plt.style.use('dark_background')

def logistic_map(x, y):
	'''a function to calculate the next step of the discrete map.  Inputs
	x and y are transformed to x_next, y_next respectively'''
	y_next = y * x * (Decimal('1') - y)
	x_next = x + Decimal('0.00001')
	return x_next, y_next

steps = 100000

Y, X = [], []
precision = 10000
getcontext().prec = precision

Y.append(Decimal('0.5'))
X.append(Decimal('3'))


# map the equation to array step by step using the logistic_map function above
for i in range(steps):
	print (i)
	pair = logistic_map(X[-1], Y[-1])
	X.append(pair[0])
	Y.append(pair[1]) # calls the logistic_map function on X[i] as x and Y[i] as y

# print (Y)
# lt.style.use('dark_background')
# plt.figure(figsize=(10, 10))
plt.plot(X, Y, ',', color='white', alpha=0.3, markersize = 0.001)
plt.axis('on')
plt.show()
# plt.savefig('Logistic_cover3.png', bbox_inches='tight', dpi=420, pad_inches=0, transparent=True)
plt.show()
