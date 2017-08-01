# ft_linear_regression
42 machine learning project. (on going)

# formula that we need for this project

1. Hypothesis(H theta(x)) -> theta0 + (theta1 * x)

2. Cost function -> (1 / 2m) sum(m, i=1) * (hypothesis(x(i)) - y(i))

3. Gradient Descent -> theta(j) - LearningRate * Cost function

# Definition of the therme

- 'x & y' are a value of our data set

- x are our input value, y are output value

- 'm' is the size of our data set

- 'i' is the index of where we are in our data set

- LearningRate is the coefficient of the learning.

# Lets' see all of that with a simple schema

							--------------------
							|   km   |  Price  |
							|--------|---------|
						i = 1	| 240000 |  3650   |
						i = 2	| 139800 |  3800   |
						i = 3	| 150500 |  4400   |
						i = 4	| 185530 |  4450   |
						i = ...	|  ...	 |  ...    |
							--------------------

						X <=> km			Y <=> Price
						M <=> 24 you can understand that with data.csv
						Who contain all the value of our data set
