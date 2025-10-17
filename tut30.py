# local variable
# this kind of variables gets created in function
# and can only be accessed within the function
# global variable
# variables that are created outside any function
# can be accesed by any function in the program
x=5 # global variable
print(x)
def hello():
    a=6 #it is local variable
    print(x)
    print(a)
hello()
# normally global variables are const but
# there is a way to change its value
def function_2():
    global x
    x=9
    print(x)
function_2()
