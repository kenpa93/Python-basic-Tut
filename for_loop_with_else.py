for i in ["22","33","44"]:
    print(i)
else:
    print("sorry")
# in this upper loop after loop is executed then else statement also executes
for j in range(6):
    print(j)
    if j ==4:
        break
    # with this break function and if inside the loop will stop else to execute
else:
    print("Sorry no j")