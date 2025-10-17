# function arguements
# these function arguements are variables just normal integers
def average(a,b):
    print("The average is ",(a+b)/2)

average(5,6)
# default arguement
# if you don't give any value as an arguement during function call then it will tak the already assigned value
#  in the function arguement
def addition(a=3,b=6):
    print("The addition ",a+b)

addition(7)
# for multiple number we should make a tuple or dictionary in function arguement
# one star in arguement means tuple in arguement
def averagem(*numbers):
    sum=0
    for i in numbers:
        sum =sum+i
    print("Average: ",sum/len(numbers))

averagem(5,5,5)
# double star means dictionary in arguements
def dict_average(**benum):
    pass