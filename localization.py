# imports
from sympy import *
#---------------------------


# Variables

mode = 'idle'
mobile_nodes = []
und_node = []
areas = []
point_radius=2
radius = 12
max_speed = 2
############

def create_node(table, x, y):
  curr_node = Point2D(x, y)
  table.append(curr_node)


  return curr_node

# Set up space
  
w = create_node(mobile_nodes, 10, 20)
z = create_node(und_node, 20, 15)
y = create_node(mobile_nodes, 20, 10)
z = create_node(mobile_nodes, 30, 20)

for node in range(len(mobile_nodes)):
  areas.append(Circle(mobile_nodes[node], radius))

# CHECK TO MAKE SURE IT IS SET UP PROPERLY
#for area in range(len(areas)):
#  print(areas[area])

def grow(b):
	# b is an area
	return b 


# Algorithm
def localize(areas):
	# max speed
	s = max_speed
	# set the first intersection equal to the first area
	I = [areas[0], areas[1], areas[2]]
	Ij = [areas[0], areas[1], areas[2]]
	# loop from 2 to number of intersections
	for k in range(2, len(I), 1):
		# set delta_t
		delta_t = k - (k-1)
		# the intersection of k is Ak
		I[k] = intersection(areas[k], grow(I[k-1]))
		# loop from j = k - 1 to 1
		for j in range(k-1, 0, -1):
			# delta_t is j - (j-1)
			delta_t = j - (j - 1)
			# the intersction of j is Aj
			Ij[j] = intersection(areas[j], grow(I[j-1]))
	return I[-1]

a = localize(areas)



# doesn't work, maybe bc missing grow? 
