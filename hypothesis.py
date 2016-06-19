# this program use the gradient descent to predict the price of a car.

import sys

theta0 = 0.
theta1 = 0.

print "please enter a milaeage: "
milaeage = raw_input();

estimatePrice = theta0 + (theta1 * float(milaeage))

print "estimate price -> ", estimatePrice