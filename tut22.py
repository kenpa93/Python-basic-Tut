# tuple testing
tuple1 =(0,1,2,3,0,1,2,3,0,1,2,3)
res=tuple1.count(1)#in this line it counts how many times it got repeated in the tuple
print("1 is repeated timesd are ",res)
res1=tuple1.index(3)#where its shown in tuple the first time
print(res1)
rest= tuple1.index(3,4,8)
# tuple1.index(number we want to find,start,finish)
print(rest)
rest1=len(tuple1)#this line calculate length tuple1
print(rest1)