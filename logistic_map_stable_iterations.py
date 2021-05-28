#! logistic_map_iterations.py
# 

# import third-party libraries
from matplotlib import pyplot as plt 
import numpy as np 
from decimal import *

# plt.style.use('dark_background')

def informational_map()
	# initialize an array of 0s and specify starting values and r constant
	steps = 99
	x = np.zeros(steps + 1)
	y = np.zeros(steps + 1)
	x[0], y[0] = 0, 0.299162102453

	r = 3.83

	# loop over the steps and replace array values with calculations
	# for i in range(steps):
	# 	y[i+1] = r * y[i] * (1 - y[i])
	# 	x[i+1] = x[i] + 1

	# information map 
	for i in range(steps):
		y[i+1] = -(y[i]*np.log2(y[i]) + (1-y[i])*np.log2(1-y[i]))
		x[i+1] = x[i] + 1

	y_array = y
	print (y)
	# plot the figure!
	fig, ax = plt.subplots()
	ax.plot(x, y, alpha=0.5)
	ax.set(xlabel='Iteration', ylabel='Entropy')
	plt.show()



def r4_solution()
	# non-recursive solution where r=4
	y = np.sin((2**n)*pi/(pi*x**0.5))
	x = 0.3
	x2 = 0.300000001
	y_ls = []
	x_ls = []
	y2_ls = []
	for i in range(100):
		n = i
		y = np.sin((2**n)*np.pi * np.arcsin(x**0.5)/np.pi)**2
		y2 = np.sin((2**n)*np.pi * np.arcsin(x2**0.5)/np.pi)**2
		x_ls.append(i)
		y_ls.append(y)
		y2_ls.append(y2)

	for i in range(len(y_array)):
		if y_ls[i] - y_array[i] > 0.00001:
			break

	plot the figure!
	fig, ax = plt.subplots()
	ax.plot(x_ls, y_ls, alpha=0.5)
	ax.plot(x_ls, y2_ls, alpha=0.5, color='red')
	ax.set(xlabel='Time (years)', ylabel='Population (fraction of max)')
	plt.show()



def test_precision()
	# test the effects of increased presicion on the logistic map shape
	getcontext().prec = 1000
	n = 1000

	y = Decimal(np.sin((2**n)*np.pi * np.arcsin(x**0.5)/np.pi)**2)
	print (y)

	def logistic_map(x, y):
		'''a function to calculate the next step of the discrete map.  Inputs
		x and y are transformed to x_next, y_next respectively'''
		y_next = y * x * (1 - y)
		x_next = x + 0.000000001
		yield x_next, y_next


	steps = 10000000

	Y = np.zeros(steps + 1)
	X = np.zeros(steps + 1)

	X[0], Y[0] = 3.82, 0.2991621

	# map the equation to array step by step using the logistic_map function above
	for i in range(steps):
		x_next, y_next = next(logistic_map(X[i], Y[i])) # calls the logistic_map function on X[i] as x and Y[i] as y
		X[i+1] = x_next
		Y[i+1] = y_next

	print (X)

	lt.style.use('dark_background')
	plt.figure(figsize=(10, 10))
	plt.plot(X, Y, ',', color='white', alpha=0.05, markersize = 0.001)
	plt.axis('on')
	# plt.show(transparent=True)
	plt.savefig('Logistic_cover3.png', bbox_inches='tight', dpi=420, pad_inches=0, transparent=True)
	plt.show()


def observe_stable_points()
	# observe f^k(1/2), the more-stable points
	x = []
	y_ls = [[], [], [], [], [], [], [], []]

	def logistic_map(x, r):
		return r*x*(1-x)

	def triple_logistic_map(x, r):
		# iterate logistic map thrice
		for i in range(3):
			x = r*x*(1-x)
		return x

	x_0 = 3.8
	y_0 = 0.5


	for i in range(5001):
		# val_ls = [logistic_map(y_0, x_0 + i/100000)]
		val_ls = [y_0]

		for j in range(8):
			val_ls.append(triple_logistic_map(val_ls[-1], x_0 + i/100000))

		x.append(x_0 + i/100000)
		for k in range(len(y_ls)):
			y_ls[k].append(val_ls[k])

		# if i % 10 == 0:
		print (i)

	fig, ax = plt.subplots()
	# ax.set_aspect(0.3)
	ax.plot(x, y_ls[1], alpha=0.5, color='red', markersize=0.01)
	ax.plot(x, y_ls[2], alpha=0.5, color='orange', markersize=0.01)
	ax.plot(x, y_ls[3], alpha=0.5, color='yellow', markersize=0.01)
	ax.plot(x, y_ls[4], alpha=0.5, color='green', markersize=0.01)
	ax.plot(x, y_ls[5], alpha=0.5, color='blue', markersize=0.01)
	ax.plot(x, y_ls[6], alpha=0.5, color='indigo', markersize=0.01)
	ax.plot(x, y_ls[7], alpha=0.5, color='violet', markersize=0.01)
	ax.plot(X, Y, ',', alpha=0.06, color='white', markersize=0.0001)
	plt.axis('on')
	plt.show()
	# plt.savefig('logistic_trace{0:04d}.png'.format((i//10)), dpi=400, bbox_inches='tight')
	plt.close()

	# ax.plot(x, y_ls[1], alpha=0.5, color='red')
	# ax.plot(x, y_ls[2], alpha=0.5, color='orange')
	# ax.plot(x, y_ls[3], alpha=0.5, color='green')
	# ax.plot(x, y_ls[4], alpha=0.5, color='blue')

	# plt.ylim(-0.1, 1.1)
	# ax.set(xlabel='r value', ylabel='x value')
	# plt.show()
	# plt.savefig('logistic_trace{}.png'.format(i), dpi=400)

observe_stable_points()




























