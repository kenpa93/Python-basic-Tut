# in this we are going to use else, if and elif 
num =int(input("Enter the value of num "))
if (num<0):
    print("the value is negative")
elif (num>0):
    # nested if else
    if (num<99):
        print("the value of num is positive")
    else:
        print("this number is out off 100")
else:
    print("this is not a numnber")

# if else and case inside will have syntax
# if (num<=10 and num >=0):
    # print("this number is bestween 0 to 10")
