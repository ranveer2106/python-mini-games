# print("hello")
# a = "hhi"
# print(a)
# x = 9
# for i in range(1, x, 2):
#     print(" "*((x-i)//2) + "*"*(i))
# for i in range(0, x+2, 2):
#     print(" "*(i//2) + "*"*(x-i))


from random import randint
a = {"a": 4,
     "b": 5,
     5: 6,
     "c": 9}
a.update({"b": "69"})
a.pop(5)
a.popitem()
# del a[]
# a.clear()
print(type(a))
print(a["b"])
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}


c = myfamily.copy()
c.popitem()
print(myfamily)
print(c)


def greet(r):
    return "hello "+r


ll = greet("ranvir")
print(ll)


print(randint(0, 3))
