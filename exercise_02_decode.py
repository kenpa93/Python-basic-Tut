a=[]
e=[]
b=input("Enter the word you wanna decode ")
c=len(b)
if c<3:
    for i in range(0,c):
        a.append(b[i])
    a.reverse()
    print(a)
else:
    for i in range(0,c):
        a.append(b[i])
    a.pop(c-1)
    a.pop(c-2)
    a.pop(c-3)
    d=a.pop(c-4)
    a.pop(2)
    a.pop(1)
    a.pop(0)
    print(a)
    e.append(d)
    f=len(a)
    for j in range(0,f):
        e.append(a[j])

    print(e)

