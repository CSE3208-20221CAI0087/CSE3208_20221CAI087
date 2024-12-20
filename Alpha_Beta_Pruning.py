# -*- coding: utf-8 -*-
"""Lab_4_AI

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lp-yBr-cm2jqn-cXGMh5q94jGBiSRmX4
"""

MAX, MIN = 1000, -1000

#(Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta, branching, maxDepth):
  if depth == maxDepth:
    return values[nodeIndex]
  if maximizingPlayer:
    best = MIN
    for i in range(0, branching):
      val = minimax(depth + 1, nodeIndex * branching + i, False, values, alpha, beta, branching, maxDepth)
      best = max(best, val)
      alpha = max(alpha, best)
      if beta <= alpha:
        break
    return best
  else:
    best = MAX
    for i in range(0, branching):
      val = minimax(depth + 1, nodeIndex * branching + i, True, values, alpha, beta, branching, maxDepth)
      best = min(best, val)
      beta = min(beta, best)
      if beta <= alpha:
        break
    return best

b = 3
maxDepth = 2
values = [3, 12, 8, 2, 4, 6, 14,5,2]
print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX, b, maxDepth))

b = 4
maxDepth = 2
values = [3, 5, 6, 9, 1, 2, 0, -1, -3, -5, -6, -9, -1, -2, 0, 1]
print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX, b, maxDepth))

def getDataFromFile(filename):

  with open(filename, 'r') as file:
    data = file.read()
  return data

filename = "/content/tree.txt"
filename1 = getDataFromFile(filename)
print(filename1)
data = filename1.split()
b = int(data[0].replace("\n",""))
m = int(data[1].replace("\n",""))
values = data[2].split(",")

leaves = values
leafVals = []
for leaf in leaves:
  leafVals.append(int(leaf))
print("No. of leaf nodes: ",len(leafVals))
optimalValue = minimax(0, 0, True, leafVals, MIN, MAX, b, m)
print("Optimal Value: ",optimalValue)

def getVisitedNode(depth, nodeIndex, maximizingPlayer, values, alpha, beta, branching, maxDepth):
  if depth == maxDepth:
    visited += 1
    return values[nodeIndex,visited]
  if maximizingPlayer:
    best = MIN
    for i in range(0, branching):
      val = minimax(depth + 1, nodeIndex * branching + i, False, values, alpha, beta, branching, maxDepth)
      best = max(best, val)
      alpha = max(alpha, best)
      if beta <= alpha:
        break
    return best,visited
  else:
    best = MAX
    for i in range(0, branching):
      val = minimax(depth + 1, nodeIndex * branching + i, True, values, alpha, beta, branching, maxDepth)
      best = min(best, val)
      beta = min(beta, best)
      if beta <= alpha:
        break
    return best,visited

def alpha_beta_pruning(branching_factor, depth, leaf_nodes):
    alpha = float('-inf')
    beta = float('inf')
    remaining_leaves = 0

    def minimax(node, depth, alpha, beta, is_maximizing):
        nonlocal remaining_leaves
        if depth == 0:
            remaining_leaves += 1
            return leaf_nodes[node]
        if is_maximizing:
            value = float('-inf')
            for i in range(branching_factor):
                value = max(value, minimax(node*branching_factor+i, depth-1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float('inf')
            for i in range(branching_factor):
                value = min(value, minimax(node*branching_factor+i, depth-1, alpha, beta, True))
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value

    expected_value = minimax(0, depth, alpha, beta, True)
    return expected_value, remaining_leaves

def getDataFromFile(filename):

  with open(filename, 'r') as file:
    data = file.read()
  return data

filename = "/content/tree.txt"
filename1 = getDataFromFile(filename)
data = filename1.split()
print(filename1)
b = int(data[0].replace("\n",""))
m = int(data[1].replace("\n",""))
values = data[2].split(",")

leaves = values
leafVals = []
for leaf in leaves:
  leafVals.append(int(leaf))
expected_value, remaining_leaves = alpha_beta_pruning(branching_factor, depth, leafVal)
print("Optimal Value: ",expected_value)
print("Number of leaf nodes remaining: ",remaining_leaves)