# this program get the information of our data set

import string
import re
def GetInfo():
mystr = open("data.csv")

km = []
price = []

for line in open("data.csv").readlines():
	index = line.index(',');
	tmp0 = line[:index]
	tmp1 = line[index + 1:-1]
	km.append(tmp0)
	price.append(tmp1)