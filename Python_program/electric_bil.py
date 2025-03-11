#!/usr/bin/python3.12

print("*******************#electric unit *****************\n")
#electric unit 
print("welcome Electric unit")
unit=int(input("enter number of unit:"))
if unit<=10:
 rupee=unit*1
 print("1 to 10 unit total price",rupee)

elif(10 < unit and unit<=50):
  print("upto 50 unit total price",unit*2)

elif(50 < unit and unit<=100):
  print("upto 100 unit total price",unit*3)

elif(100 < unit and unit<=200):
  print("upto 200 unit total price",unit*5)
  
else:
  print("more than 200 unit total price",unit*6)



#********************************************************

print("****electric unit using match case method 1 ********\n")

unit=int(input("enter unit:"))
if(unit<10):  
  value=1
elif(10 < unit<=20):
  value=2
elif(20 < unit<=50):
  value=3  
elif(50 < unit<=100):
  value=4
elif(100 < unit<=200):
  value=5  
elif(200 < unit):
  value=6

match value:
     case 1:
       print(unit*1)
     case 2:
       print(unit*2)
     case 3:
       print(unit*3)
     case 4:
       print(unit*4)
     case 5:
       print(unit*5)
     case 6:
       print(unit*6)




#*********************************************************
print("****electric unit using match case method 2 ********\n")


unit=int(input("enter number of unit:"))
match unit:
    case bill_amount if (bill_amount<=10):
        print("til 10 unit unit amount=",unit*1)
    case bill_amount if bill_amount in range(11,21):
        rate_1=10*1
        rate_2=(unit-10)*2
        total_bill=rate_1+rate_2
        print("till 20 unit unit amount=",total_bill)
    case bill_amount if bill_amount in range(21,51):
        rate_1=10*1
        rate_2=10*2
        rate_3=(unit-10-10)*3
        total_bill=rate_1+rate_2+rate_3
        print("till 50 unit unit amount=",total_bill)
    case bill_amount if bill_amount in range(51,101):
        rate_1=10*1
        rate_2=10*2
        rate_3=30*3
        rate_4=(unit-10-10-30)*4
        total_bill=rate_1+rate_2+rate_3+rate_4
        print("till 100 unit unit amount=",total_bill)
    case bill_amount if bill_amount in range(101,201):
        rate_1=10*1
        rate_2=10*2
        rate_3=30*3
        rate_4=50*4
        rate_5=(unit-10-10-30-50)*5
        total_bill=rate_1+rate_2+rate_3+rate_4+rate_5
        print("till 200 unit unit amount=",total_bill)
    case bill_amount if (bill_amount>200):
        rate_1=10*1
        rate_2=10*2
        rate_3=30*3
        rate_4=50*4
        rate_5=100*5
        rate_6=(unit-10-10-30-50-100)*6
        total_bill=rate_1+rate_2+rate_3+rate_4+rate_5+rate_6
        print("till 200 unit unit amount=",total_bill)

