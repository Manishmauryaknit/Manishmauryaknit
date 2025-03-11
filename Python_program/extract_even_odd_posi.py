print("***************extract even and odd number from list**********************")

list1=[1,2,3,4,5,6,7,8,9]
list2=list1[slice(0,len(list1),2)]  #odd position number
list3=list1[slice(1,len(list1),2)]  #even position number
print(list2)
print(list3)


print("**************************************************************************")
list4=[0,2,5,4,10,6,71,1,9]
list5=list4[slice(0,len(list4),2)]  #odd position number
list6=list4[slice(1,len(list4),2)]  #even position number
print(list5)
print(list6)
print("*******************************slice method*******************************")

a = ("a", "b", "c", "d", "e", "f", "g", "h")

x = slice(3, 5)  #3rd and 4th element will come
print(x)
print(a[x])
x=slice(3)       # til 3rd element will come 
print(a[x])

x=slice(0,10,3)# a,d,g will come
print(a[x])

x=a[slice(0,10)]#it will print a to h
print(x)
x=a[slice(0,9)]#it will print a to h
print(x)
