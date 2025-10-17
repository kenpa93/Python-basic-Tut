# this program is a mathemactical simulation of star
# but this program will only simulate one star because if we
# try to smiluate whole universe then you need super computers
import time
print("*****  *   *  ******       ******     *****     ***      *****")
print("  *    *   *  *            *            *      *   *     *    *")
print("  *    *****  ******       ******       *      *****     ******")
print("  *    *   *  *                 *       *      *   *     * *")
print("  *    *   *  ******       ******       *      *   *     *   *")
print("WARNING: THIS SIMLUATOR CREATES A STAR IN YOUR SYSTEM")
print("IN THIS PROGRAM YOU WILL ONLY VISUALLY SEE MATHEMACTICAL CALCULATIONS")
print("BASICALLY YOU WILL EVERY QUARKS AND ATOMS READINGS SO YOU CAN UNDERSTAND")
print("THE STARS WORKING FROM THE INSIDE AND THIS PROGRAM IS MEANT FOR RESEARCH")
print("THIS PROGRAM DOESN'T COPY ANY DATA FROM ANY ORGANISATION")
print("THIS PROGRAM WORKS OFFLINE AND IS A SEPERATE UNIT ITSELF")
print("ITS FOR EDUCATIONAL PURPOSE AND YOU CAN ENJOY TOO")
print("THIS PROGRAM IS CREATED FOR ASTRONOMY ENTUSIASTS")
print("ENJOY ;))")
print("1. to start the star")
print("2. Start from save file")
print("3. leave the simulator")
previous_outcome=0
a=int(input("Enter your choice in the numbers form as shown "))
i=0
j=1
b=785468446123388
d=b/3
atm=2
atm2=8
massx=(b*1.674)+(b*1.6726)
future_outcome=3
atomic_number=1
atomic_number2=4
future_string=''
atm2_string=''

if a==1:
    while i<2:
        if atomic_number<=3:
            print("the number new elements formed ",atomic_number)
            print("percentage of the present element ",(1/atomic_number)*100)
            print("atom found with atomic number is ",atomic_number)
            print("remaining atoms",b/atm)
            atm+=2
            print("==========================================================")
            
        elif atomic_number>=3:
            
          print("atomic number of main element ",atomic_number)
          future_outcome=(future_outcome-1)+atomic_number
          print("the number of new elements formed ",future_outcome)
          print("remaining atoms",b/atm2)
          print("concentration of the new elements in the star is",(1/future_outcome)*100)
          atm2+=2
          print("============================================================")
          future_string=future_outcome
          atm2_string=atomic_number
        rec1='outcomes= '+str(future_string)+' '+'atomic number= '+str(atm2_string)+ ' the number in division of the atoms '+str(atm2)
        f=open('save_file.txt','w')
        f.write(rec1)
        f.close()
        time.sleep(2)
        atomic_number+=1
        


# elif a==2:

else:
    print("SORRY TO DISTURB YOU")
    time.sleep(5)

