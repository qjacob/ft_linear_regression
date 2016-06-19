# this program use the gradient descent to predict the price of a car.

import sys, re, string, math

theta0 = 0.
theta1 = 0.

LearningRate = 0.5

print "please enter a milaeage: "
milaeage = raw_input();

mystr = open("data.csv")

km = []
price = []

for line in open("data.csv").readlines():
	index = line.index(',');
	tmp0 = line[:index]
	tmp1 = line[index + 1:-1]
	km.append(tmp0)
	price.append(tmp1)

m0 = len(km) - 1
m1 = len(price) - 1

if (m0 != m1):
	print "Error: Your data set is incorrect"
	sys.exit(0)

for value in range(m0):
	if (value == 0):
		continue
	else:
		m = km[value]
		sqrterr = math.sqrt(theta0 + (theta1 * float(m)))
		
		print sqrterr

estimatePrice = theta0 + (theta1 * float(milaeage))

print "estimate price -> ", estimatePrice