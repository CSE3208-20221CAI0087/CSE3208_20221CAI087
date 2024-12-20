# -*- coding: utf-8 -*-
"""Lab3_AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1whprB7vCSjZHABB8QQjNX7pitFJVACsU
"""

from queue import Queue

RomaniaMap = dict()
vertices = ['A','B','C','D','E','F','G','H','I','L','M','N','O','P','R','S','T','U','V','Z']
RomaniaMap['A'] = [('S',140),('T',118),('Z',75)]
RomaniaMap['B'] = [('F',211),('P',101),('G',90),('U',85)]
RomaniaMap['C'] = [('D',120),('R',146),('P',138)]
RomaniaMap['D'] = [('C',120),('M',75)]
RomaniaMap['E'] = [('H',86)]
RomaniaMap['F'] = [('B',211),('S',99)]
RomaniaMap['G'] = [('B',90)]
RomaniaMap['H'] = [('E',86),('U',98)]
RomaniaMap['I'] = [('N',87),('V',92)]
RomaniaMap['L'] = [('M',70),('T',111)]
RomaniaMap['M'] = [('L',70),('D',75)]
RomaniaMap['N'] = [('I',87)]
RomaniaMap['O'] = [('Z',71),('S',151)]
RomaniaMap['P'] = [('B',101),('C',138),('R',97)]
RomaniaMap['R'] = [('P',97),('C',146),('S',80)]
RomaniaMap['S'] = [('A',140),('R',80),('F',99),('O',151)]
RomaniaMap['T'] = [('A',118),('L',1)]
RomaniaMap['U'] = [('H',98),('V',142),('B',85)]
RomaniaMap['V'] = [('I',92),('U',142)]
RomaniaMap['Z'] = [('O',71),('A',75)]

def bfs(RomaniaMap,startingNode, destinationNode):
    visited = {}
    distance = {}
    parent = {}
    bfs_traversal_output = []
    queue = Queue()
    for city in RomaniaMap.keys():
        visited[city] = False
        parent[city] = None
        distance[city] = -1

    startingCity = startingNode
    visited[startingCity] = True
    distance[startingCity] = 0
    queue.put(startingCity)

    while not queue.empty():
        u = queue.get()
        bfs_traversal_output.append(u)

        for (v,d) in RomaniaMap[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                distance[v] = distance[u] + d
                queue.put(v)

    g = destinationNode
    path = []
    if not visited[destinationNode]:
        print("Path not reachable")
        return
    while g is not None:
        path.append(g)
        g = parent[g]


    path.reverse()
    print("Path :",path)
    print("Distance :",distance[destinationNode])

bfs(RomaniaMap,'A','B')

from collections import deque

def dfs(RomaniaMap,startingNode, destinationNode):
  visited = {}
  distance = {}
  parent = {}
  dfs_traversal_output = []
  stack = deque()
  for city in RomaniaMap.keys():
    visited[city] = False
    parent[city] = None
    distance[city] = -1

  startingCity = startingNode
  visited[startingCity] = True
  distance[startingCity] = 0
  stack.append(startingCity)

  while len(stack) > 0:
    u = stack.pop()
    dfs_traversal_output.append(u)

    for (v,d) in RomaniaMap[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        distance[v] = distance[u] + d
        stack.append(v)

  g = destinationNode
  path = []
  if not visited[destinationNode]:
    print("Path not reachable")
    return
  while g is not None:
    path.append(g)
    g = parent[g]



  path.reverse()
  print("Path :",path)
  print("Distance :",distance[destinationNode])

dfs(RomaniaMap,'A','B')

RomaniaMapFile = dict()
filename = "Graph.txt"
fl = open(filename, "r")
lines = fl.readlines()
for line in lines:
    parts = line.strip().split("->")
    key = parts[0]
    neighbours = parts[1].split(",")
    value = []
    for neighbour in neighbours:
        neighbouringVertex = neighbour.split(",")[0]
        distance = neighbour.split(",")[1]
        if distance.isdigit():
          pair = (neighbouringVertex,int(distance))
          value.append(pair)
    RomaniaMapFile[key] = value
print(RomaniaMapFile)

line = key

from queue import PriorityQueue
f1=open('/content/sample_data/graph.txt',"r")
lines=f1.readlines()
graph=dict()
for line in lines:
  if(len(line.split("\t"))!=2):
    continue
  parts=line.split("\t")
  key=parts[0].upper()
  neighbours=parts[1].split(" ")
  value=[]
  for neighbour in neighbours:
    neighbouringvertex=neighbour.split(",")[0]
    distance=int(neighbour.split(",")[1])
    pair=(neighbouringvertex,distance)
    value.append(pair)
  graph[key]=value
for key in graph.keys():
  line=key+"->"+str(graph[key])
  print(line)

from queue import PriorityQueue

def ucs(graph, start, goal):
  visited = set()
  frontier = PriorityQueue()
  frontier.put((0, start))
  parent = {}

  cost = {start:0}

  while not frontier.empty():
    current_cost, current_node = frontier.get()
    if current_node == goal:
      break
    visited.add(current_node)

    for nextNode, distance in graph[current_node]:
      newDistance = cost[current_node] + distance

      if nextNode not in cost or newDistance < cost[nextNode]:
        cost[nextNode] = newDistance
        priority = newDistance
        frontier.put((priority, nextNode))
        parent[nextNode] = current_node

  path = []
  #totalCost = 0
  if goal in parent:
    current = goal
    while current != start:
      path.append(current)
      #totalCost += graph[parent[current]][current]
      current = parent[current]
    path.append(start)
    path.reverse()
  return path #,totalCost

print((graph,'A','B'))

def ucs_c(graph, start, goal):
  visited = set()
  frontier = PriorityQueue()
  frontier.put((0, start))
  parent = {}

  cost = {start:0}

  while not frontier.empty():
    current_cost, current_node = frontier.get()
    if current_node == goal:
      break
      visited.add(current_node)

      for nextNode, distance in graph[current_node]:
        newDistance = cost[current_node] + distance

        if nextNode not in cost or newDistance < cost[nextNode]:
          cost[nextNode] = newDistance
          priority = newDistance
          frontier.put((priority, nextNode))
          parent[nextNode] = current_node

    path = []
    totalCost = 0
    if goal in parent:
      current = goal
      while current != start:
        path.append(current)
        totalCost += graph[parent[current]][current]
        current = parent[current]
      path.append(start)
      path.reverse()
    return path
    return cost

print(ucs_c(graph,'A','B'))

