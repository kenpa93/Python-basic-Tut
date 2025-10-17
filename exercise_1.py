import time
timestamp= time.strftime('%H')
if (timestamp<'12'):
    print("Good morning")
elif (timestamp >'12' and timestamp < '16'):
    print("good afternoom")
else:
    print("Good evening")