from hypothesis import hypothesis

def cost_function(theta0, theta1, m):
	res = 1 / (2 * m)
# 1 / (2 * m) * sum(hypothesis(x(i)) - y(i)) ^ 2