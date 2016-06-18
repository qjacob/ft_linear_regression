#	fromule for linear regression:
# hypothesis: theta(x) = theta(0) + (theta(1) * x).					'x' is a value of ou data set.
# Cost Function: (1 / 2m) sum(m, i=1) (hypothesis(x(i)) - y(i))^2.		'm' is the size of our data set. 'y' is an other value of our data set
#	for exemple in this exercice we have this Data set:
#														--------------------
#														|   km   |  Price  |
#														|--------|---------|
#						  		i = 1	| 240000 |  3650   |
#				    			i = 2	| 139800 |  3800   |
#			    				i = 3	| 150500 |  4400   |
# 		    				i = 4	| 185530 |  4450   |
#						    				i = ...	|  ...	 |  ...    |
#			  			 							--------------------
#
#																	'x' is the price. 'y' is the km. And 'i' is the index where we are in our data set.
#  Gradient descent function: theta(0) - alpha * (1 / m) sum(m, i=1) (hypothesis(x(i)) - y(i))
#							  theta(1) - alpha * (1 / m) sum(m, i=1) (hypothesis(x(i)) - y(i)) . x(i)
#
#																	'alpha' is the "learning rate" (He must be not too small and not too big)
