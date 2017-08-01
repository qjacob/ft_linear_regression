# repeat until convergence: {
# 	Theta0 = Theta0 - LearningRate * (1 / m) * Sum(Hypothesis(x_i) - y_i)
# 	Theta1 = Theta1 - LearningRate * (1 / m) * Sum(Hypothesis(x_i) - y_i)
# }

from tools import SumTheta0, SumTheta1
from GetKmPrice import get_len_dataset, getPrice, getKm
from tools import hypothesis
import matplotlib.pyplot as plt
import math
import sys

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def displayGraph(t0, t1, km, price, clear=False):

	km = [x * 1000. for x in km]
	price = [x * 1000. for x in price]
	
	if clear:
		ax.clear()

	ax.plot(km, price, 'o', color='#008080')

	lineX = [0, 260000]
	lineY = [hypothesis(t0, t1, 0), hypothesis(t0, t1, 260000)]

	ax.plot(lineX, lineY, linestyle='dashed', color='#ff6600', linewidth=3.0)
	plt.pause(0.001)

def GradientDescent(theta0, theta1, LearningRate, LearningRate2, km, price, m, graph):
	theta0 = 0.0
	theta1 = 0.0

	i = 0

	while (True):
		sum0 = SumTheta0(theta0, theta1, km, price, m) / float(m)
		sum1 = SumTheta1(theta0, theta1, km, price, m) / float(m)
		tmp_theta0 = LearningRate * sum0
		tmp_theta1 = LearningRate2 * sum1

		if abs(tmp_theta0) < float(0.000001) and abs(tmp_theta1) < float(0.000001):
			return (theta0 * 1000, theta1)

		if graph:
			if i == 2000:
				i = 0
				displayGraph(theta0 * 1000, theta1, km, price, True)
			else:
				i += 1

		theta0 = theta0 - tmp_theta0
		theta1 = theta1 - tmp_theta1



graph = 'graph' in sys.argv

km = getKm()
price = getPrice()

theta0, theta1 = GradientDescent(theta0=0.0, theta1=0.0, LearningRate=0.0001, LearningRate2=0.0001, km=km, price=price, m=get_len_dataset(), graph=graph)

if graph:
	plt.ioff()
	plt.show()


if (theta0 != 0.0) and (theta1 != 0.0):
			try:
				theta_value_file = open('theta_value_file', 'w')
				theta_value_file.write('theta0={}\ntheta1={}'.format(theta0, theta1))
				theta_value_file.close()
			except Exception:
				print("message: An error happened !")