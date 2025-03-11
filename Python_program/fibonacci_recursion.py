#!/urs/bin/python3.12

def fibo(num):
  if(num==0):
    return 0
  elif(num==1):
    return 1
  elif(num>1):
    fib=fibo(num-1)+fibo(num-2)
    return fib
  else:
    return 1
in1=int(input("enter number"))
for i in range(in1):
   print(f"fibonacci of {i}:",fibo(i))
 
