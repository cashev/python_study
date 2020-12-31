from PIL import Image, ImageDraw

def newton(x):
  for _ in range(10):
    x = x - (x**4 - 1) / (4 * x**3)
  return x

def plot(draw, s):
  hs = s // 2
  red = (255, 0, 0)
  green = (0, 255, 0)
  blue = (0, 0, 255)
  purple = (255, 0, 255)
  for x in range(s):
    for y in range(s):
      z = complex(x - hs + 0.5, -y + hs + 0.5) / s * 0.4
      z = newton(z)
      c = red
      if z.real > 0:
        if z.imag < 0:
          c = purple
      else:
        if z.imag > 0:
          c = green
        else:
          c = blue
      draw.rectangle([x, y, x + 1, y + 1], fill=c)

size = 512
img = Image.new("RGB", (size, size))
draw = ImageDraw.Draw(img)
plot(draw, size)
img.show()
