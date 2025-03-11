print("**************************list operation*********************************************")
list1=[0,[1,2,3],4,5]
print(list1)
print(id(list1),list1)
print(id(list1[0]),list1[0]) #it will print list1[0] id and containt 0
print(id(list1[1]),list1[1]) #it will print list1[1] id and containt [1,2,3]

print("*********************inside list1 another list address and data**********************")
#every list element address will be diffrent
print(id(list1[1][0]),list1[1][0]) #it will print list1[1][0] id and containt 1
print(id(list1[1][1]),list1[1][1]) #it will print list1[1][1] id and containt 2
print(id(list1[1][2]),list1[1][2]) #it will print list1[1][2] id and containt 3
print(id(list1[2]),list1[2]) #it will print list1[2] id and containt 4
print(id(list1[3]),list1[3]) #it will print list1[3] id and containt 5


print("**************************list  inside list operation*********************************************")
list1=[0,[1,2,3,["manish","kumar","maurya"],4],5,6]
print("address of list1=",id(list1),"containt of list1=",list1)
print("address of list1[0]=",id(list1[0]),"containt of list1[0]=",list1[0])
print("address of list1[1]=",id(list1[1]),"containt of list1[1]=",list1[1])
print("address of list1[2]=",id(list1[2]),"containt of list1[2]=",list1[2])

print("**********************address of list inside list***********************")
print("address of list1[1][0]=",id(list1[1][0]),"containt of list1[1][0]=",list1[1][0])
print("address of list1[1][1]=",id(list1[1][1]),"containt of list1[1][1]=",list1[1][1])
print("address of list1[1][2]=",id(list1[1][2]),"containt of list11[1[2]=",list1[1][2])
print("address of list1[1][3]=",id(list1[1][3]),"containt of list1[1][3]=",list1[1][3])
print("address of list1[1][4]=",id(list1[1][4]),"containt of list1[1][3]=",list1[1][4])


print("address of list1[1][3][0]=",id(list1[1][3][0]),"containt of list1[0]=",list1[1][3][0])
print("address of list1[1][3][1]=",id(list1[1][3][1]),"containt of list1[0]=",list1[1][3][1])
print("address of list1[1][3][2]=",id(list1[1][3][2]),"containt of list1[0]=",list1[1][3][2])
print("address of list1[1][4]=",id(list1[1][4]),"containt of list1[0]=",list1[1][4])


