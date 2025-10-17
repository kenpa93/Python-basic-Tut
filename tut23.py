# f string is the for anyone to use variable in the string
name="Sparsh"
country ="India"
print(f"hey my name is {name} and i am from {country}")
# in float values sometime values after decimal goes way big
f1 = 49.99999
# to print the limited values after decimal 
# in this print line the format will be
# (float variable:. the number values you wanna print f) 
text=f"for only {f1:.2f}"
print(text)
# to create a new string with numbers only 
print(f"{2*30}")
# to print curly brackets with values in f strings are 
print(f"{{name}}{{country}}")