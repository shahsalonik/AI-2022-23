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

edges = "Unit 4/Train Routes Files/rrEdges.txt"
names = "Unit 4/Train Routes Files/rrNodeCity.txt"
coords = "Unit 4/Train Routes Files/rrNodes.txt"

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

def a_star(start, end, graph):
    closed = {start: (0, [start])}
    total_dist = taxicab(start, end)
    fringe = []
    heapify(fringe)
    heappush(fringe, total_dist)

    while len(fringe) > 0:
      v = heappop(fringe)

      if v[1] == end:
         path, distance = closed[v[1]][1], v[0]
         return path, distance
      
      #need to add the for loop

    return None, None

print("Time to create data structure: " + str(dict_end - dict_start))

city1 = sys.argv[1]
city2 = sys.argv[2]

city_id1 = name_dict[city1]
city_id2 = name_dict[city2]

dij_start = perf_counter()
distance = dijkstra(city_id1, city_id2)
dij_end = perf_counter()

print(city1 + " to " + city2 + " with Dijkstra: " + str(distance) + " in " + str(dij_end - dij_start))
print(city1 + " to " + city2 + " with A*: ")
