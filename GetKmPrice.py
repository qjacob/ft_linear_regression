# this program get the information of our data set

import string
import re

def getKm():
	km = []

	for line in open("data.csv").readlines():
		index = line.index(',')
		tmp = line[:index]
		try:
			tmp = float(tmp) / 1000
		except ValueError:
			tmp = tmp
		km.append(tmp)
	km = km[1:]
	return (km)

def getPrice():
	price = []

	for line in open("data.csv").readlines():
		index = line.index(',')
		tmp = line[index + 1: -1]
		try:
			tmp = float(tmp) / 1000
		except ValueError:
			tmp = tmp
		price.append(tmp)
	price = price[1:]
	return (price)

def get_len_dataset():
	km = []
	price = []
	km = getKm()
	price = getPrice()
	if (len(km) != len(price)):
		print("Error: Your data set is incorrect")
		sys.exit(0)
	m = len(km)
	return(int(m))
