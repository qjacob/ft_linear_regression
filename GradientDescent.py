# repeat until convergence: {
# 	Theta0 = Theta0 - LearningRate * (1 / m) * Sum(Hypothesis(x_i) - y_i)
# 	Theta1 = Theta1 - LearningRate * (1 / m) * Sum(Hypothesis(x_i) - y_i)
# }

from tools import SumTheta0, SumTheta1
import math
import sys

def GradientDescent(theta0, theta1, LearningRate, LearningRate2, km, price, m):
	theta0 = 0.0
	theta1 = 0.0

	while (True):
		sum0 = SumTheta0(theta0, theta1, km, price, m) / float(m)
		sum1 = SumTheta1(theta0, theta1, km, price, m) / float(m)
		tmp_theta0 = LearningRate * sum0
		tmp_theta1 = LearningRate2 * sum1

		if abs(tmp_theta0) < float(0.000001) and abs(tmp_theta1) < float(0.000001):
			return (theta0 * 1000, theta1)

		theta0 = theta0 - tmp_theta0
		theta1 = theta1 - tmp_theta1
