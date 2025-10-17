# tuples in this code we will use
tup=(1,5,7,9,6,2,3)
print(type(tup),tup)
tup2=tup[0:3]
print(tup2)
# tuples can be manipulated but not directly, indirectly
countries =("Spain","Italy","India","England","Germany")
temp=list(countries)# making list temp and copy items in new list temp
temp.append("Russia")
temp.pop(3)#erase an item from list this is a list method
temp[2]="Finland"
countries=tuple(temp)#this line will add the items tha weren't their previously
print(countries)

