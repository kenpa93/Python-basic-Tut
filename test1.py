a=[]
b=input("Enter the word you wanna encode ")
c=len(b)
for i in range(0,c):
    a.append(b[i])

print(a)
d=a.pop(0)

print(a)
a.append(d)
print(a)
# e=random(a,) useless line this is
a.append(e)
print(a)