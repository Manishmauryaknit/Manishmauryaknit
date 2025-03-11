#!/usr/bin/python3.12
#assigning value in variable
print("********************assigning in variable*******************\n")

a=b=c=d=e = 10                          #assining same value for all variable
print(a,b,c,d,e)                        #it will print 10 for all variable
print(id(a),id(b),id(c),id(d),id(e))    #for all variable id will be same (for same value id(address) will be same) 

a,b,c,d,e=1,2,3,4,5                     #it will assign one one value for one one variable
print(a,b,c,d,e)
print(id(a),id(b),id(c),id(d),id(e))    #for diffrent variable id will be diffrent because value is diffrent

a,b,c,d,e=10,"hello","manish",100,120
print(a,b,c,d,e)
print(id(a),id(b[0]),id(c),id(d),id(e)) #for diffrent variable id will be diffrent because value is diffrent


#***********************************************************************
print("***********comparision operator*********\n")
#boolean it will be true or false only 
print("5 is greater than 3",5>3)
print("5 is greater than 10",5>10)
print("5 is greater or equal 5",5>=5)


#***********************************************************************

print("***********boolean operator*********\n")

print("value_for_10",bool(10))           #true
print("value_for_2000",bool(2000))       #true
print("value_for_manish",bool("manish")) #true
print("value_for_empty()",bool())        #false
print("value_for_empty[]",bool([]))      #false
print("value_for_[0]",bool([0]))         #true
print("value_for_zero",bool(0))          #false
print("value_for_none",bool(None))       #false
print("value_for_imag(0+0.1j)",bool(0+0.1j))     #true
print("value_for_imag(0+0.0j)",bool(0+0j))       #false


#*************************************************************************
x=10
y=20
print("**********bitwise operation***************\n")
z=x & y
print('bitwise and of 10,20',z)# x=10=01010 y=20=10100 after bitwise and z=00000
z=x|y
print('bitwise OR of 10,20',z) # x=10=01010 y=20=10100 after bitwise OR z=11110
z=~x
print('bitwise not of 10',z)




print("*************logical operation****************\n")
z=x and y
print('logical and of 10,20',z)
z=x or y
print('logical OR of 10,20',z)
z=not x
print('logical not of 10',z)
z=y ^ x
print('logical xor of 10,20',z)



print("*************** shifting operator**************\n")
z=x>>3
print("right shift of 10",x,z)
print("bit lenght",z.bit_length())
z=x<<3
print("left shift of 10",x,z)
print("bit lenght",z.bit_length())



