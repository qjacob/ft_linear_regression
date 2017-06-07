import math
import sys
from hypothesis import hypothesis

def SumTheta0(theta0, theta1, km, price, m):
	value = 0.0
	for i in range(m):
		# print("I'th value:")
		# print(i)
		# print("theta0:")
		# print(theta0)
		# print("theta1:")
		# print(theta1)
		# print("km[i]:")
		# print(km[i])
		# print("price[i]:")
		# print(price[i])
		# if math.isinf(theta1):
		# 	print("MDR C L INFINI")
		# 	sys.exit(1)
		value += hypothesis(theta0, theta1, float(km[i])) - float(price[i])
	return (value)

def SumTheta1(theta0, theta1, km, price, m):
	value = 0.0
	for i in range(m):
		# print("I'th value:")
		# print(i)
		# print("theta0:")
		# print(theta0)
		# print("theta1:")
		# print(theta1)
		# print("km[i]:")
		# print(km[i])
		# print("price[i]:")
		# print(price[i])
		# if math.isinf(theta1):
		# 	print("MDR C L INFINI")
		# 	sys.exit(1)
		value += (hypothesis(theta0, theta1, float(km[i])) - float(price[i])) * float(km[i])
	return (value)