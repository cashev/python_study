def newton(x):
  for _ in range(10):
    x = x - (x**3 - 1) / (3 * x**2)
    print(x)

print(newton(-1 - 1j))
