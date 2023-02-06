#! /usr/bin/env python3


import prob1



(a,b,c) = ("xyz", "hello", "world")

print("Inputs:")
print("  a = "+str(a))
print("  b = "+str(b))
print("  c = "+str(c))
print()

print("First Object:")
obj = prob1.Simplest(a,b,c)

print("  obj.a = "+str(obj.a))
print("  obj.b = "+str(obj.b))
print("  obj.c = "+str(obj.c))
print()

print("After making some changes...")
obj.a = 123
obj.b = ["foo","bar","baz"]
obj.c = (obj.b, obj.b)
print("  obj.a = "+str(obj.a))
print("  obj.b = "+str(obj.b))
print("  obj.c = "+str(obj.c))
print()

print("Creating a new object, using multiples of the inputs:")
obj = prob1.Simplest(a*2, b*3, c*4)
print("  obj.a = "+str(obj.a))
print("  obj.b = "+str(obj.b))
print("  obj.c = "+str(obj.c))


