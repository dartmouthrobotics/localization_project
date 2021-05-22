# imports
import os
from shapely.geometry import Point
import matplotlib.pyplot as plt
from ipywidgets import interactive

# suppress message
#---------------------------

# --- Creates node --- #
def create_node(table, x, y):
	curr_node = Point(x, y)
	table.append(curr_node)
	plt.plot(x, y, 'o')

	return curr_node

def setup_space(mobile_nodes, areas, radius, axes):
	# Set up space  
	w = create_node(mobile_nodes, 10, 20)
	y = create_node(mobile_nodes, 30, 10)
	x = create_node(mobile_nodes, 30, 20)

	for node in range(len(mobile_nodes)):
		areas.append(mobile_nodes[node].buffer(radius))
		axes.add_patch(plt.Circle((mobile_nodes[node].x, mobile_nodes[node].y), radius, color='black', fill=False))
	#############


# --- For now, returns old circle --- #
def grow(old_circle, sbydelta):
	#new_circle = Circle((old_circle.center.x*10, old_circle.center.y)*10, old_circle.radius+sbydelta)
	return old_circle


# Algorithm
def localize(areas, max_speed):
	# max speed
	s = max_speed
	# set the first intersection equal to the first area
	I = [areas[0], areas[1], areas[2]]
	Ij = [areas[0], areas[1], areas[2]]
	# loop from 2 to number of intersections
	for k in range(1, len(I), 1): # only goes once
	
		# set delta_t
		delta_t = k - (k-1)
		# the intersection of k is Ak
		#I[k] = intersection(areas[k], grow(I[k-1], s))
		I[k] = areas[k].intersection(grow(I[k-1], s))
		# loop from j = k - 1 to 1
		for j in range(k-1, 0, -1):
			# delta_t is j - (j-1)
			delta_t = j - (j - 1)
			# the intersction of j is Aj
			#Ij[j] = intersection(areas[j], grow(I[j-1], s))
			Ij[j] = areas[j].intersection(grow(I[j-1], s))
	return I[-1]

def main(radius=20):

	# Variables

	mode = 'idle'
	mobile_nodes = []
	und_node = []
	areas = []
	point_radius=5
	max_speed = 2
	screen_size=(1000, 1000)
	############

	# load functions
	figure, axes = plt.subplots()
	axes.axis("equal")
	####

	setup_space(mobile_nodes, areas, radius, axes)

	a = localize(areas, max_speed)

	# plotting
	x,y = a.exterior.xy
	plt.plot(x,y)
	plt.fill_between(x, y, 0, color="red", alpha=0.2)
	plt.show()


interactive_plot = interactive(main, radius=(0, 50, 5))
interactive_plot

