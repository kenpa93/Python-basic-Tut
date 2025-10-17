
for i in range(0,6): 
    b=i
    
    f=open('test_save.txt','w')
    rec=str(b)
    f.write(rec)
    f.close()
    print(b)

    i+=1