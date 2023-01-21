from math import pi , acos , sin , cos
from heapq import heapify, heappush, heappop
from time import perf_counter
import tkinter as tk
from tkinter import simpledialog
import time
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

dict_start = perf_counter()

#dict for name to id
name_dict = {}
with open("rrNodeCity.txt") as f:
   for line in f:
      temp_list = line.split()
      name_dict[" ".join(temp_list[1:])] = temp_list[0]

#dict for id to coord
coord_dict = {}
with open("rrNodes.txt") as f:
   for line in f:
      temp_list = line.split()
      coord_dict[temp_list[0]] = (float(temp_list[1]), float(temp_list[2]))

#tuple dict
backing_dict = {}
with open("rrEdges.txt") as f:
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

#dict that stores things like {(id1, id2): canvas line object}
canvas_dict_draw = {}
canvas_dict_access = {}
root = tk.Tk()
canvas = tk.Canvas(root, height=800, width=800, bg='white')

with open("rrEdges.txt") as f:
   for line in f:
      id1, id2 = line.split()
      lat1, long1 = coord_dict[id1]
      lat2, long2 = coord_dict[id2]
      new_lat1 = 800 - (((lat1 - 10) / 60) * 800)
      new_long1 = (((long1 + 130) / 70) * 800)
      new_lat2 = 800 - (((lat2 - 10) / 60) * 800)
      new_long2 = (((long2 + 130) / 70) * 800)
      line = canvas.create_line([(new_long1, new_lat1), (new_long2, new_lat2)], tag='grid_line')
      canvas_dict_draw[(id1, id2)] = line
      canvas_dict_access[(id1, id2)] = line
      canvas_dict_access[(id2, id1)] = line

dict_end = perf_counter()

def draw_general_path(r, c):
    for key in canvas_dict_draw.keys():
        c.itemconfig(canvas_dict_draw[key])
        r.update()
   #time.sleep(10)

def draw_dijkstra_path(r, c, edge1, edge2):
   c.itemconfig(canvas_dict_access[(edge1, edge2)], fill = "red", width = 2)
   #r.update()

def draw_dijkstra_final_path(r, c, p):
   for n in range(len(p) - 1): 
      c.itemconfig(canvas_dict_access[(p[n], p[n+1])], fill = "green", width = 5)
      r.update()

def draw_a_star_path(r, c, edge1, edge2):
   c.itemconfig(canvas_dict_access[(edge1, edge2)], fill = "blue", width = 2)

def draw_astar_final_path(r, c, p, start):
   for n in range(len(p) - 1): 
      if p[n] == start:
         c.itemconfig(canvas_dict_access[(p[n], p[n+1][0])], fill = "green", width = 5)
         r.update()
      else:
         c.itemconfig(canvas_dict_access[(p[n][0], p[n+1][0])], fill = "green", width = 5)
         r.update()
   #r.mainloop()

def taxicab(node1, node2):
   return calcd(coord_dict[node1], coord_dict[node2])

def dijkstra(start, end):
   update_count = 0

   closed = {start: (0, [start])}
   start_node = (0, start)
   fringe = []
   heapify(fringe)
   heappush(fringe, start_node)
   closed_set = set()

   while len(fringe) > 0:
      v = heappop(fringe)

      if v[1] == end:
         path, distance = closed[v[1]][1], v[0]
         draw_dijkstra_final_path(root, canvas, path)
         return path, distance
      if v[1] not in closed_set:
        closed_set.add(v[1])
        for c in backing_dict[v[1]]:
            if c[0] not in closed_set:
                temp = (v[0] + c[1], c[0])
                closed[c[0]] = (v[0] + c[1], closed[v[1]][1] + [c[0]])
                heappush(fringe, temp)
                draw_dijkstra_path(root, canvas, v[1], c[0])
        update_count += 1
        if update_count % 2500 == 0:
            root.update()
   return None, None

def a_star(start, end):
   update_count = 0

   closed = {start: (0, [start])}
   start_node = (taxicab(start, end), start, [start])
   fringe = []
   heapify(fringe)
   heappush(fringe, start_node)

   while len(fringe) > 0:
      v = heappop(fringe)

      if v[1] == end:
         path, distance = closed[v[1]][1], v[0]
         draw_astar_final_path(root, canvas, path, start)
         return path, distance
      
      for c in backing_dict[v[1]]:
         draw_a_star_path(root, canvas, v[1], c[0])
         actual_dist = closed[v[1]][0] + taxicab(v[1], c[0])
         if c[0] not in closed or closed[c[0]][0] > actual_dist:
            estimated_dist = taxicab(c[0], end)
            heappush(fringe, (actual_dist + estimated_dist, c[0], v[2] + [c]))
            closed[c[0]] = (actual_dist, v[2] + [c])
            draw_a_star_path(root, canvas, v[1], c[0])
      update_count += 1
      if update_count % 2500 == 0:
         root.update()

   return None, None

print("Time to create data structure: " + str(dict_end - dict_start))

canvas.pack(expand=True)
#sys.argv[1]
city1 = sys.argv[1]
city2 = sys.argv[2]

city_id1 = name_dict[city1]
city_id2 = name_dict[city2]

'''
options:
0: Dijkstra
1: A*
2: DFS
3: ID-DFS
4: Bidirectional Dijkstra
5: Reverse A*
6: BFS ?? Something else?? we'll see
'''

#code to make a pop-up window with text input
entry = tk.Tk()

entry.withdraw()
algorithm = simpledialog.askstring(title="Algorithm Choice", 
prompt="Pick an algorithm to run:\n0: Dijkstra\n1: A*\n2: DFS\n3: ID-DFS\n4: Bidirectional Dijkstra\n5: Reverse A*\n6: BFS ?? Something else?? we'll see")

if int(algorithm) == 0:
   #run dijkstra
   start = perf_counter()
   path, dijkstra_distance = dijkstra(city_id1, city_id2)
   end = perf_counter()
   print(city1 + " to " + city2 + " with Dijkstra: " + str(dijkstra_distance) + " in " + str(end - start))
elif int(algorithm) == 1:
   #run a*
   print()
elif int(algorithm) == 2:
   #run dfs
   print()
elif int(algorithm) == 3:
   #run id_dfs
   print()
elif int(algorithm) == 4:
   #run bidir dijkstra
   print()
elif int(algorithm) == 5:
   #run rev a*
   print()
elif int(algorithm) == 6:
   #run [SOMETHING]
   print()
else:
   algorithm = simpledialog.askstring(title="INVALID INOUT", prompt="Sorry, that's not a valid algorithm. Please try again:")
