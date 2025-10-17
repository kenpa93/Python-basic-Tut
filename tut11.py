# match case statement
# this function is avalilable after the python version 3.10
# this is just to teach you what is match case statement it ios similar c and c++ so its nostalgia 
x =int(input("Enter number between 1 to 2 "))
match x:
    case 1:
        print("x is one")
    case 2:
        print("x is 2")
    # for default line is 
    case _:
        print("You entered an interesting value",x)


# in this line we will how you that if can be use int match case statement
# case _ if(x!=90):
    # print(x,"is not 90")