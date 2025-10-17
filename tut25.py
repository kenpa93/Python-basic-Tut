# factorial program
# def factorial(n):
    # if (n==0 or n==1):
        # return 1
    # else:
        # return n*(n-1)

# print(factorial(5))
# recursion this means calling the function in itself
def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))