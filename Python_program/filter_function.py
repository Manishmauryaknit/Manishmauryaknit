#filter function in python
inp1=int(input("enter range"))
list1=[]
for i in range(inp1):
   list1.append(i)

list_num=list(filter(lambda x:x%2==0,list1)) 
print("even",list_num)
list_num=list(filter(lambda x:x%2,list1)) 
print("odd",list_num)
list_num=list(filter(lambda x:x%5==0,list1))
print("divisible by 5",list_num)

list_num=list(filter(lambda x:x>10,list1))
print("greter than 10 in given range",list_num)

