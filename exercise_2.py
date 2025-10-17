# to encode the word
a=[]
b=input("Enter the word you wanna encode ")
c=len(b)
if(c>=3):
    a.append("a")
    a.append("b")
    a.append("c")
    for i in range(0,c):
        a.append(b[i])
    d=a.pop(3)
    a.append(d)
    a.append("x")
    a.append("y")
    a.append("z")
    print(a)
else:
    for i in range(0,c):
        a.append(b[i])
    a.reverse()
    print(a)