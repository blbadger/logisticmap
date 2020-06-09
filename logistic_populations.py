#! Python3
# Logistic population over time: displays the population
# (in proportion of maximum) over time, with r values slowly 
# increasing from 3.5 to 4.  Saves .png images of the population 
# graphs for each value of r.


from matplotlib import pyplot as plt 
import numpy as np 

steps = 50

for t in range(500):
	r = 3.5 + t/1000
	x = np.zeros(steps + 1)
	y = np.zeros(steps + 1)

	x[0], y[0] = 0, 0.30000

	for i in range(steps):
		y[i+1] = r * y[i] * (1 - y[i])
		x[i+1] = x[i] + 1

	X2 = np.zeros(steps + 1)
	Y2 = np.zeros(steps + 1)

	X2[0], Y2[0] = 0, 0.300005

	for i in range(steps):
		Y2[i+1] = r * Y2[i] * (1 - Y2[i])
		X2[i+1] = X2[i] + 1

	fig, ax = plt.subplots()
	ax.plot(x, y, alpha=0.5)
	ax.plot(X2, Y2, alpha=0.5)
	ax.set(xlabel='Time (years)', ylabel='Population (fraction of max)')
	plt.savefig('{}.png'.format(t), dpi=300)
	plt.close()


