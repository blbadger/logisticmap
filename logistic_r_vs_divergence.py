#! python3
# Logistic_r_vs_divergence: a program to display the number of iterations until divergence
# bewteen two initially close points over a range of r values to generate a single images 
# of iterations until divergence vs. r value.  This is then repeated as the two initial points
# X1 and X2 approach each other.


from matplotlib import pyplot as plt 
import numpy as np 

for t in range(1, 300):

	steps = 500
	y = np.zeros(steps + 1)
	r = np.zeros(steps + 1)
	r[0] = 3.5
	y[0] = 100

	for i in range(500):
		X1 = 0.3
		X2 = 0.3 + 0.3**(t/30)

		for j in range(100):
			X1 = r[i] * X1 * (1-X1)
			X2 = r[i] * X2 * (1-X2)

			if np.abs(X1 - X2) > 0.15:
				break

		y[i+1] = j + 1
		r[i+1] = r[i] + 0.001

	fig, ax = plt.subplots()
	ax.plot(r, y)
	ax.set(xlabel='r value', ylabel='First iteration of divergence')
	plt.savefig('{}.png'.format(t), dpi=300)
	plt.close()


