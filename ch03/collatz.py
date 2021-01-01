# from graphviz import Digraph

def collatz(i):
  print(i)
  while i != 1:
    if i % 2 == 0:
      i = i // 2
    else:
      i = i * 3 + 1
    print(i)

collatz(3)
