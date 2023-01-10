from math import pi , acos , sin , cos
from heapq import heapify, heappush, heappop
from time import perf_counter
import sys

def calcd(node1, node2):
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees
   y1, x1 = node1
   y2, x2 = node2

   R   = 3958.76 # miles = 6371 km
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0

   # approximate great circle distance with law of cosines
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R

edges = "rrEdges.txt"
names = "rrNodeCity.txt"
coords = "rrNodes.txt"

dict_start = perf_counter()

#dict for name to id
name_dict = {}
with open(names) as f:
   for line in f:
      temp_list = line.split()
      name_dict[" ".join(temp_list[1:])] = temp_list[0]

#dict for id to coord
coord_dict = {}
with open(coords) as f:
   for line in f:
      temp_list = line.split()
      coord_dict[temp_list[0]] = (float(temp_list[1]), float(temp_list[2]))

#tuple dict
backing_dict = {}
with open(edges) as f:
   for line in f:
      id1, id2 = line.split()
      #need to calculate the distance between two points
         #can only do that when i pull the points from existing coord dict
      #id1 = (id2, distance)
      if id1 not in backing_dict:
         backing_dict[id1] = set()
         backing_dict[id1].add((id2, calcd(coord_dict[id1], coord_dict[id2])))
      else:
         backing_dict[id1].add((id2, calcd(coord_dict[id1], coord_dict[id2])))
      
      if id2 not in backing_dict:
         backing_dict[id2] = set()
         backing_dict[id2].add((id1, calcd(coord_dict[id2], coord_dict[id1])))
      else:
         backing_dict[id2].add((id1, calcd(coord_dict[id2], coord_dict[id1])))

dict_end = perf_counter()

def taxicab(node1, node2):
   return calcd(coord_dict[node1], coord_dict[node2])

def dijkstra(start, end):
   closed = set()
   start_node = ((0, start))
   fringe = []
   heapify(fringe)
   heappush(fringe, start_node)

   while len(fringe) > 0:
      v = heappop(fringe)

      if v[1] == end:
         return v[0]
      if v[1] not in closed:
         closed.add(v[1])
         for c in backing_dict[v[1]]:
            if c not in closed:
               temp = ((v[0] + c[1], c[0]))
               heappush(fringe, temp)
   
   return None

def a_star(start, end):
    closed = {start: (0, [start])}
    start_node = (taxicab(start, end), start, [start])
    fringe = []
    heapify(fringe)
    heappush(fringe, start_node)

    while len(fringe) > 0:
      v = heappop(fringe)

      if v[1] == end:
         distance = v[0]
         return distance
      
      #need to add the for loop
      for c in backing_dict[v[1]]:
        actual_dist = closed[v[1]][0] + taxicab(v[1], c[0])
        if c[0] not in closed or closed[c[0]][0] > actual_dist:
            estimated_dist = taxicab(c[0], end)
            heappush(fringe, (actual_dist + estimated_dist, c[0], v[2] + [c]))
            closed[c[0]] = (actual_dist, v[2] + [c])

    return None, None

print("Time to create data structure: " + str(dict_end - dict_start))

#sys.argv[1]
city1 = sys.argv[1]
city2 = sys.argv[2]

city_id1 = name_dict[city1]
city_id2 = name_dict[city2]

print(city_id1)
print(city_id2)

dij_start = perf_counter()
dij_distance = dijkstra(city_id1, city_id2)
dij_end = perf_counter()

astar_start = perf_counter()
astar_distance = a_star(city_id1, city_id2)
astar_end = perf_counter()

print(city1 + " to " + city2 + " with Dijkstra: " + str(dij_distance) + " in " + str(dij_end - dij_start))
print(city1 + " to " + city2 + " with A*: " + str(astar_distance) + " in " + str(astar_end - astar_start))