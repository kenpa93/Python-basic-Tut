# list methods
l=[9, 1, 3, 4, 5, 6]
print(l)
# to add a new item to list
l.append(7)
# to sort and arrange the items in the list
l.sort()
print(l)
# to arrange items in reverse decending order
l.sort(reverse=True)
print(l)
# another alternative for this is 
l.reverse()
print(l)
# in this below line we learn what is the index of the itme we specified in index line
print(l.index(4))
# in this below we count how many times the asked item is repeated in list
print(l.count(1))
# m=l this line won't do the job so don't try this
# m=l.copy() this line will copy contents of list l to list m
m=l.copy() #this line will also make a new list m with all the contents of list l
# to add a new content to certain index their 2 ways
# way 1
m[0]=0
print(m)
# 2 nd way
l.insert(1,899)
# now int his line l.insert(index,content)
print(m)
# in this line in below adding all contents of list m to list k
l.extend(m)# warining for line usage you have to declare a list first thgen you can use this funtion
# in this blow line we will add two lists
o=l+m
print(o)