# the plan
# write random walk function
# V1) simple
# V2) short
# if you are more than 4 blocks away from home you will pay for a transport back home, otherwise you will just walk

# what is the longest random walk you can take so that on average you will end up 4 blocks or fewer from home? 

import random
def random_walk(n):
	"""Return coordinates after 'n' block random walk"""
	x = 0
	y = 0
	for i in range(n):
		step = random.choice(["N", "S", "E", "W"])
		if step == "N":
			y = y+1
		elif step == "S":
			y -= 1
		elif step == "E":
			x += 1
		else:
			x -= 1
	return (x, y)

for i in range(25):
	walk = random_walk(10)
	print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1])) # sum of absolute values of x and y coordinates 

def random_walk2(n):
	"""Return coordinates after 'n' block random walk"""
	x, y = 0, 0
	for i in range(n):
		(dx, dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])  # dx = difference in x, dy = difference in y
		x += dx
		y += dy
	return (x,y)

for i in range(25):
	walk = random_walk2(10)
	print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

# what is the longest random walk you can take so that on average you will end up 4 blocks or fewer from home?
# in other words there is less than a 50 percent chance you'll pay for transport home

# we will use the monte carlo method
# instead of solving the problem mathematically, we will conduct thousands of random trials and compute the percentage of random walks that end in a hort walk home

# to get an accurate number, we will take 10,000 random walks for each walk size

def random_walk3(n):
        """Return coordinates after 'n' block random walk"""
        x, y = 0, 0
        for i in range(n):
                (dx, dy) = random.choice([(0,1), (0,-1), (1,0), (-1,0)])  # dx = difference in x, dy = difference in y
                x += dx
                y += dy
        return (x,y)

number_of_walks = 10000

for walk_length in range(1, 31): # walk length for 1 to 30 blocks
	no_transport = 0 # number of walks 4 or fewer blocks from home
	for i in range(number_of_walks): # the monte carlo loop for 10,000 walks
		(x,y) = random_walk3(walk_length)
		distance = abs(x) + abs(y)
		if distance <= 4:
			no_transport += 1
	no_transport_percentage = float(no_transport) / number_of_walks
	print("Walk size = ", walk_length, " / % of no transport = ", 100*no_transport_percentage)
	

# monte carlo method uses random samples and different simulations give slightly different results.




 
