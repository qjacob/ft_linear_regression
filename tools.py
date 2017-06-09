import math
import sys

def hypothesis(theta0, theta1, x):
	return (theta0 + (theta1 * x))

def SumTheta0(theta0, theta1, km, price, m):
	value = 0.
	for i in range(0, m):
		value += hypothesis(theta0, theta1, km[i]) - price[i]
	return (value)

def SumTheta1(theta0, theta1, km, price, m):
	value = 0.
	for i in range(0, m):
		value += (hypothesis(theta0, theta1, km[i]) - price[i]) * km[i]
	return (value)