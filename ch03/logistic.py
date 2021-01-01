import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt

def logistic(r):
  n = 0.1
  for i in range(1000):
    n = r * n * (1.0 - n)
    if i > 990:
      print(n)

def logistic_plot(start, end, x, y):
  for i in range(1000):
    r = (end - start) * i / 1000 + start
    n = 0.1
    for j in range(1000):
      n = r * n * (1.0 - n)
      if j > 900:
        x.append(r)
        y.append(n)

def plot(start, end):
  x, y = [], []
  logistic_plot(start, end, x, y)
  plt.scatter(x, y, s=0.1)
  plt.show()

plot(1.0, 3.0)

plot(1.0, 4.0)

plt.ylim([0.335, 0.39])
plot(3.54, 3.58)
