import math
import sys

def hypothesis(theta0, theta1, x):
	return (theta0 + (theta1 * x))

def SumTheta0(theta0, theta1, km, price, m):
	value = 0.0
	for i in range(m):
		value += hypothesis(theta0, theta1, float(km[i])) - float(price[i])
	return (value)

def SumTheta1(theta0, theta1, km, price, m):
	value = 0.0
	for i in range(m):
		value += (hypothesis(theta0, theta1, float(km[i])) - float(price[i])) * float(km[i])
	return (value)