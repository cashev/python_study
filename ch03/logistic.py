import matplotlib.pyplot as plt

def logistic(r):
  n = 0.1
  for i in range(1000):
    n = r * n * (1.0 - n)
    if i > 990:
      print(n)

logistic(1.5)
print()
logistic(2.0)
print()
logistic(3.1)
