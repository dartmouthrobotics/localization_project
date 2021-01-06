# imports
from sympy import *
import os
# suppress message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as py
#---------------------------


# Variables

mode = 'idle'
mobile_nodes = []
und_node = []
areas = []
point_radius=5
radius = 120
max_speed = 2
screen_size=(500, 600)
############

# load functions
py.init()
screen = py.display.set_mode(screen_size)
white = (255, 255, 255)
black = (0, 0, 0)
screen.fill(white)
####

def create_node(table, x, y):
  curr_node = Point2D(x, y)
  table.append(curr_node)
  py.draw.circle(screen, black, (x*10, y*10), point_radius)
  py.display.flip()

  return curr_node

# Set up space
  
w = create_node(mobile_nodes, 10, 20)
z = create_node(und_node, 20, 15)
y = create_node(mobile_nodes, 20, 10)
z = create_node(mobile_nodes, 30, 20)

for node in range(len(mobile_nodes)):
  areas.append(Circle(mobile_nodes[node], radius))
  py.draw.circle(screen, black, (mobile_nodes[node].x*10, mobile_nodes[node].y*10), radius, 1)
  py.display.flip()
# CHECK TO MAKE SURE IT IS SET UP PROPERLY
#for area in range(len(areas)):
#  print(areas[area])

def grow(old_circle, sbydelta):
	new_circle = Circle(old_circle.center, old_circle.radius+sbydelta)
	#new_circle = Circle((old_circle.center.x*10, old_circle.center.y)*10, old_circle.radius+sbydelta)

	return new_circle


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
		I[k] = intersection(areas[k], grow(I[k-1], s))
		# loop from j = k - 1 to 1
		for j in range(k-1, 0, -1):
			# delta_t is j - (j-1)
			delta_t = j - (j - 1)
			# the intersction of j is Aj
			Ij[j] = intersection(areas[j], grow(I[j-1], s))
	return I[-1]

a = localize(areas)

print(a)


running = True
while running:
  for event in py.event.get():
    if event.type == py.QUIT:
      running = False


# doesn't work, maybe bc missing grow? 
