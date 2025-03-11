#!/usr/bin/python3.12

def add(n):
  if(n<=1):
    return n
  else:
    sum=n+add(n-1)
    return sum

in1=int(input("enter number:"))
print("sum of number:",add(in1))
