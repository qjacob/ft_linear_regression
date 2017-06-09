import sys, re, string, math
from tools import hypothesis
from GetKmPrice import get_len_dataset, getPrice, getKm
from GradientDescent import GradientDescent

def main():
	LearningRate = 0.0001
	LearningRate2 = 0.0001
	theta0 = 0.
	theta1 = 0.
	price = []
	km = []
	mileage = raw_input("Please enter a mileage: ")
	try:
		mileage = mileage[:-1]
		float(mileage)
		m = get_len_dataset()
		price = getPrice()
		km = getKm()
		(hypothesis(float(theta0), float(theta1), float(m)))
		theta0, theta1 = (GradientDescent(float(theta0), float(theta1), float(LearningRate), float(LearningRate2), km, price, m))
		print("theta0:")
		print(theta0)
		print("theta1:")
		print(theta1)
		print("Result of hypothesis:")
		print(hypothesis(theta0, theta1, float(mileage)))
	except ValueError as e:
		print(e)
		print("error: Please enter an integer.")
		main()

main()

print("DONE !")