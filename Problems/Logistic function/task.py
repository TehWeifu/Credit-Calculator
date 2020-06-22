import math

num = int(input())

result = round(math.exp(num) / (math.exp(num) + 1), 2)

print(result)
