#Import libraries
import numpy as np 
import matplotlib.pyplot as plt 

def logistic_map(x, y):
	'''a function to calculate the next step of the discrete map.  Inputs
	x and y are transformed to x_next, y_next respectively.  Returning a 
	generator is not strictly beneficial in this instance, as the function 
	returns only two values rather than a long list.'''
	y_next = y * x * (1 - y)
	x_next = x + 0.000001
	yield x_next, y_next

# initialization of 2 dimensional numpy array, starting coordinates, and number of steps, and
# care is necessary to not exceed an X value of 4, or the logistic map diverges to infinity
steps = 1000000

Y = np.zeros(steps + 1)
X = np.zeros(steps + 1)

X[0], Y[0] = 3, 0.5

# map the equation to array step by step using the logistic_map function above
for i in range(steps):
	x_next, y_next = next(logistic_map(X[i], Y[i])) # calls the logistic_map function on X[i] as x and Y[i] as y
	X[i+1] = x_next
	Y[i+1] = y_next

# matplotlib figure setup with light points on a dark background aesthetics
plt.style.use('dark_background')
plt.figure(figsize=(30, 30))
plt.plot(X, Y, '.', color='white', alpha=0.4, markersize = 0.3)
plt.axis('on')

plt.show()
plt.close() # only really important if many plots are made in rapid succession