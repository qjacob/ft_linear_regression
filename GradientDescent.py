# repeat until convergence: {
# 	Theta0 = Theta0 - LearningRate * (1 / m) * Sum(Hypothesis(x_i) - y_i)
# 	Theta1 = Theta1 - LearningRate * (1 / m) * Sum(Hypothesis(x_i) - y_i)
# }

from tools import SumTheta0, SumTheta1
from GetKmPrice import get_len_dataset, getPrice, getKm
from tools import hypothesis
import matplotlib.pyplot as plt
# import numba as nb
import math
import time

# @nb.jit(nb.types.Tuple((nb.float64[:], nb.float64[:,:]))(nb.float64[:], nb.float64[:,:])(nb.float64[:], nb.float64[:,:])(nb.float64[:], nb.float64[:,:]),nopython=True)
def GradientDescent(theta0, theta1, LearningRate, LearningRate2, km, price, m):
	theta0 = 0.0
	theta1 = 0.0

	while (True):
		sum0 = SumTheta0(theta0, theta1, km, price, m) / float(m)
		sum1 = SumTheta1(theta0, theta1, km, price, m) / float(m)
		tmp_theta0 = LearningRate * sum0
		tmp_theta1 = LearningRate2 * sum1

		if abs(tmp_theta0) < float(0.000001) and abs(tmp_theta1) < float(0.000001):
			return (theta0 * 1000, theta1)

		theta0 = theta0 - tmp_theta0
		theta1 = theta1 - tmp_theta1

km = getKm()
price = getPrice()

start_time = time.time()

theta0, theta1 = GradientDescent(theta0=0.0, theta1=0.0, LearningRate=0.0001, LearningRate2=0.0001, km=km, price=price, m=get_len_dataset())

print(type(GradientDescent))

end_time = time.time()

print("Time to compute the GradientDescent: %s sec" % (end_time - start_time))

km = [x * 1000. for x in km]
price = [x * 1000. for x in price]

lineX = [0, 260000]
lineY = [hypothesis(theta0, theta1, 0), hypothesis(theta0, theta1, 260000)]

start_graph = time.time()

plt.plot(km, price, 'ro')
plt.plot(lineX, lineY, 'r-')
end_graph = time.time()

print("Time to create graph: %s" % (end_graph - start_graph))
plt.show()


if (theta0 != 0.0) and (theta1 != 0.0):
			try:
				theta_value_file = open('theta_value_file', 'w')
				theta_value_file.write('theta0={}\ntheta1={}'.format(theta0, theta1))
				theta_value_file.close()
			except Exception:
				print("message: An error happened !")