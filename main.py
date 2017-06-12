import sys, re, string, math
from tools import hypothesis
from GetKmPrice import get_len_dataset

def main():
	LearningRate = 0.0001
	LearningRate2 = 0.0001
	theta0 = 0.
	theta1 = 0.
	price = []
	km = []
	mileage = raw_input("Please enter a mileage: ")
	try:
		mileage = float(mileage)
		m = get_len_dataset()
		try:
			with open('theta_value_file', 'r') as f:
				 value = f.readlines()
				 index = value[0].index('=')
				 theta0 = value[0][index+1:]
				 theta1 = value[1][index+1:]
		except Exception as e:
			print("message: {}".format(e))
		print("Estimate price:")
		print(hypothesis(float(theta0), float(theta1), mileage))
	except ValueError as e:
		print(e)
		print("error: Please enter a number.")
		main()

main()

print("DONE !")