# in this program we will make list and understand them
# list can contain both integer and string in it
marks=[3,5,6,"Sparsh"]
# prints list
print(marks)
# prints the type
print(type(marks))
# in this we print a specific item from list using index
print(marks[0])
# -ve indexing
print(marks[-3])
# logic behind -ve index is length of string sub 3 that's it
if "Sparsh" in marks:
    print("yes")
else:
    print("No")
# now we can also check if the content of the list have things asked in them or not
if "Spa" in "Sparsh":
    print("Yes")

print(marks[1::2])
# in the square brackets[start:finish:step]
# list comprehension
lst=[i*i for i in range(4)]
print(lst)
lst1=[a*a for a in range(10) if a%2==0]
print(lst1)