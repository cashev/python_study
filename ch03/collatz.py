from graphviz import Digraph

def collatz(i):
  print(i)
  while i != 1:
    if i % 2 == 0:
      i = i // 2
    else:
      i = i * 3 + 1
    print(i)

def collatz_graph(i, edges):
  while i != 1:
    j = i
    if i % 2 == 0:
      i = i // 2
    else:
      i = i * 3 + 1
    edges.add((j, i))

def make_graph(n):
  g = Digraph()
  edges = set()
  for i in range(1, n+1):
    collatz_graph(i, edges)
  for i, j in edges:
    g.edge(str(i), str(j))
  g.attr(size="10,10")
  return g

make_graph(3)
