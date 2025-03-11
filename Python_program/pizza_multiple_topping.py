#!/usr/bin/python3.12

print("pizza with diffrent flavor diffrenst size,diffrent topping\n")

def pizza(company,flavour,size,*topping):
     print("company:",company)
     print("flavour:",flavour)
     print("size:",size)
     for topin in topping:
         print("topping:",topin)


#pizza("dominos","garlic",200,["chilli","tommato"])

a=str(input("enter company:"))
b=str(input("enter flavour:"))
c=int(input("enter size:"))
d=str(input("enter topping:"))
pizza(a,b,c,d)
