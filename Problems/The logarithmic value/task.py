import math

num1 = int(input())
num2 = int(input())
result = 0

if num2 <= 1:
    result = round(math.log(num1), 2)
else:
    result = round(math.log(num1, num2), 2)

print(result)
