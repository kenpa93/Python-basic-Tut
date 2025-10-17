# dictionary methods 
# update function
# its used update the database of a dictionary
ep1={122:45,123:89,567:69,670:69}
ep2={22:67,566:90}
ep1.update(ep2)
print(ep1)
# to clean the dictionary
# clear function
# ep1.clear()
# print(ep1)
ep1.pop(123)
print(ep1)
# pop item method this will remove the last item of the dictionary
ep1.popitem()
print(ep1)
# del method you can either delete a dictionary, or an item
del ep1[122]
print(ep1)
del ep1
print(ep1)
