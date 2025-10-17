# docstring
# its the description we add for for the function we create
def square(n):
    # that's how you add description for a function
    '''takes in a number n,returns the square of n'''
    print(n**2)
square(5)
# to print the the descripton you wrote
print(square.__doc__)
# there is a condition this docstraing will not work if the description is not just under the name of the function