import sys, re, string, math
from tools import hypothesis
from GetKmPrice import get_len_dataset, getPrice, getKm
from GradientDescent import GradientDescent

def main():
	LearningRate = 0.0001
	theta0 = 0.
	theta1 = 0.
	price = []
	km = []
	mileage = raw_input("Please enter a mileage: ")
	# try:
	mileage = mileage[:-1]
	float(mileage)
	m = get_len_dataset()
	price = getPrice()
	km = getKm()
	(hypothesis(theta0, theta1, m))
	theta0, theta1 = (GradientDescent(theta0, theta1, mileage, LearningRate, km, price, m))
	print("theta0:")
	print(theta0)
	print("theta1:")
	print(theta1)
	# except ValueError as e:
	# 	print(e)
	# 	print("error: Please enter an integer.")
	# 	main()

main()

print("DONE !")