#!/usr/bin/python3.12

print("*************factorial using recursive **********\n")

n=int(input("enter number"))
def fact(n):
  if(n>1):
   fac=n*fact(n-1)
   return fac
  else:
   return 1
print("factorial=",fact(n))

