

import math
a = {1, 2, 3}
b = {2, 4, 3, 8}
i = a.intersection(b)
u = a.union(b)
d1 = a.difference(b)
d2 = b.difference(a)
# print(i)
# print(u)
print(d2)
l = [1, 2, 3, 4]
# print(" ".join(list(map(str,l))))
print(*l)
# n = int(input())
# L = [int(i) for i in input().split()]
# a = sum(L)//(n+1)
# x = [j-a for j in L]
# print(*x)
x = (9, 2, 3, 4, 9)
a1, a2, *a3 = x

# x[1] = 4
# print(type(c))
# print(type(a3))

# c = {"f": "t", "f1": "t1", "f3": "t3"}
# for k, i in c.items():
# print(k)

ds = {8, 7, 6, 8, 9, 9, 7}
ds2 = {"R", "h", "R", "l", 7}
ds.add(0)
ds2.remove("R")
q = ds2.symmetric_difference(ds)
i = ds.difference_update(ds2)
print(q)

sew = "a bg klkkfklkk"
# if "klkka" not in sew:
# sd = sew.count("klk")
# c43 = sew.replace("klkk","lkkk")
# print(sd)
# print(c43)
c44 = sew.count("klkk")
# print(c44)
print(math.lcm(2, 9))
print(math.gcd(9, 2))
