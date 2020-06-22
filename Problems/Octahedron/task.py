import math

num = int(input())

area = 2 * math.sqrt(3) * num ** 2
volume = 1 / 3 * math.sqrt(2) * num ** 3

print(round(area, 2), round(volume, 2))
