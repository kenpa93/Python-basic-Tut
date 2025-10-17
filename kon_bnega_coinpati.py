quest=["What is the capital of japan?",
"What is the oxygen carrier of the human body?",
"What is the chemical formula for copper sulphate",
"Cyber security term TCP fullform is?",
"What is the first egyptian king name?",
"what do bard's play in their performances?",
"what is the 3rd law of newton?",
"who is the newest gradmaster of chess?",
"what was the date of last olympic in 2024?",
"Name of the google new CEO?"]
ab=0
print(quest[0])
print("1.Delhi")
print("2.Kyoto")
print("3.Shibuya")
print("4.Tokyo")
a=int(input("Enter the number of your answer "))
if(a==4):
    print("Right answer",)
    ab+=1
else:
    print("Wrong answer")
print(quest[1])
print("1.White blood cells")
print("2.Haemoglobin")
print("3.Mitochondria")
print("4.RNA")
b=int(input("Enter the number of your answer "))
if(b==2):
    print("Right answer")
    ab+=1
else:
    print("Wrong answer")
print(quest[3])
print("1.CU4SO3")
print("2.CU2SO4")
print("3.CUSO4")
print("4.CUSO3")
c=int(input("Enter the number of your answer "))
if(c==3):
    print("Right answer",)
    ab+=1
else:
    print("Wrong answer")
print(quest[3])
print("1.Transmission control protocol")
print("2.Transmission center protocol")
print("3.Transfering center pretext")
print("4.Transmitting censtion protocol")
d=int(input("Enter the number of your answer "))
if(d==1):
    print("Right answer")
    ab+=1

else:
    print("Wrong answer")
print(quest[4])
print("1.Menes")
print("2.Tynes")
print("3.Great King Tut")
print("4.Wenter")
e=int(input("Enter the number of your answer "))
if(e==1):
    print("Right answer")
    ab+=1
else:
    print("Wrong answer")
print(quest[5])
print("1.Harmonica")
print("2.Lyre")
print("3.Piano")
print("4.Trumpet")
f=int(input("Enter the number of your answer "))
if(f==2):
    print("Right answer")
    ab+=1
else:
    print("Wrong answer")
print(quest[6])
print("1.For every action their is an equal and oppsite reaction")
print("2.Inertia")
print("3.Thermodynamics")
print("4.Conservation of energy")
g=int(input("Enter the number of your answer "))
if(g==1):
    print("Right answer")
    ab+=1
else:
    print("Wrong answer")
print(quest[7])
print("1.Gukesh Dommaraju")
print("2.Maya chaudhary")
print("3.Ramesh verma")
print("4.Ying shung")
h=int(input("Enter the number of your answer "))
if(h==1):
    print("Right answer")
    ab+=1
else:
    print("Wrong answer")
print(quest[8])
print("1.12 May 2024")
print("2.23 June 2024")
print("3.12 August 2024")
print("4.05 septamber 2024")
i=int(input("Enter the number of your answer "))
if(i==3):
    print("Right answer")
    ab+=1
else:
    print("Wrong answer")
print(quest[9])
print("1.Sunder pichai")
print("2.Larry Yang")
print("3.Bill gates")
print("4.Walter melt")
j=int(input("Enter the number of your answer "))
if(j==1):
    print("Right answer")
    ab+=1
else:
    print("Wrong answer")
if(ab==1):
    print("Then you will get 1 bitcoin")
elif (ab==2):
    print("Then you will get 2 bitcoin")
elif (ab==3):
    print("Then you will get 3 bitcoin")
elif (ab==4):
    print("Then you will get 4 bitcoin")
elif (ab==5):
    print("Then you will get 5 bitcoin")
elif (ab==6):
    print("Then you will get 6 bitcoin")
elif (ab==7):
    print("Then you will get 7 bitcoin")
elif (ab==8):
    print("Then you will get 8 bitcoin")
elif (ab==9):
    print("Then you will get 9 bitcoin")
elif (ab==10):
    print("Then you will get 10 bitcoin")
else:
    print("You lost no money for you",ab)