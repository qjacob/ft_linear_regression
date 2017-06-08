# repeat until convergence: {
# 	Theta0 = Theta0 - LearningRate * (1 / m) * Sum(Hypothesis(x_i) - y_i)
# 	Theta1 = Theta1 - LearningRate * (1 / m) * Sum(Hypothesis(x_i) - y_i)
# }

from compute import SumTheta0, SumTheta1
import math
import sys

def GradientDescent(theta0, theta1, mileage, LearningRate, km, price, m):
	theta0 = 0.0
	theta1 = 0.0
	i = 0
	while (True):
		print("theta1:")
		print(theta1)
		print("theta0:")
		print(theta0)
		if math.isnan(theta1) or math.isnan(theta0):
			print("OGINB !")
			sys.exit(1)
		tmp_theta0 = LearningRate * (SumTheta0(theta0, theta1, km, price, m) / m)
		tmp_theta1 = LearningRate * (SumTheta1(theta0, theta1, km, price, m) / m)
		print("tmp_theta0:")
		print(tmp_theta0)
		print("tmp_theta1:")
		print(tmp_theta1)
		if math.isnan(tmp_theta1) or math.isnan(tmp_theta0):
			print("BINGO !")
		if abs(tmp_theta0) < float(0.00001) and abs(tmp_theta1) < float(0.00001):
			return (tmp_theta0, tmp_theta1)
		theta0 = theta0 - abs(tmp_theta0)
		theta1 = theta1 - abs(tmp_theta1)