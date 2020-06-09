#! Python3
# A program to generate a series for .png images of increasing magnification
# of the logistic map.  Shows the self-similar fractal nature of the chaotic portion
# of this map.


#Import libraries
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('dark_background')

def logistic_map(x, y, t, steps):
	'''a function to calculate the next step of the discrete map.  Inputs
	x and y are transformed to x_next, y_next respectively.  Returning a 
	generator is not strictly beneficial in this instance, as the function 
	returns only two values rather than a long list.'''
	y_next = x * np.cos(y-x)
	x_next = x + (0.0000015 / (2**(t/30))) / (steps / 500000)
	yield x_next, y_next

for t in range(1, 500):
	# initialization of 2 dimensional numpy array, starting coordinates, and number of steps, and
	# care is necessary to not exceed an X value of 4, or the logistic map diverges to infinity
	steps = 500000 + np.int(500000 * t/60)

	Y = np.zeros(steps + 1)
	X = np.zeros(steps + 1)

	X[0], Y[0] = -0.2 / (2**(t/30)) + 3.56995, 0.5 +(0.3925 * t)/600
	print (X[0])

	# map the equation to array step by step using the logistic_map function above
	for i in range(steps):
		x_next, y_next = next(logistic_map(X[i], Y[i], t, steps)) # calls the logistic_map function on X[i] as x and Y[i] as y
		X[i+1] = x_next
		Y[i+1] = y_next

	# matplotlib figure setup with light points on a dark background aesthetics
	# plt.xlim(-2 / (2**(t/30)) + 3.56995, 1 / (2**(t/30)) + 3.56995)
	plt.ylim(-1.8925 / (2**(t/30)) + 0.892481, 1 / (2**(t/30))  + 0.892481)

	plt.plot(X, Y, ',', color='white', alpha=0.55, markersize = 0.013)
	plt.axis('off')
	plt.savefig('{}.png'.format(t), dpi=300)
	plt.close()
