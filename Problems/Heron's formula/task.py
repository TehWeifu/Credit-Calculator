# put your python code here
import math

side_a = int(input())
side_b = int(input())
side_c = int(input())

p = (side_a + side_b + side_c) / 2

s = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))

print(s)
