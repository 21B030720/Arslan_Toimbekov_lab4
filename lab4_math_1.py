import math
a = int(input())
print(math.radians(a))
a = '{:.6f}'.format(math.radians(a/180*math.pi))
print(a)