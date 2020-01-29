'''
Hey, my name is Martín Alarcón and I would be glad to be part of the STACK BUILDERS workteam
here's my code, hope you like it
the user must enter the date and plate
input restrictions were considered for both cases
'''

from datetime import datetime
import time


i=0

# function to validate the date's format
def validateDate(date):
    for format in ['%d/%m/%y %H:%M:%S']:
        try:
            result = time.strptime(date, format)
            return True
        except:
            pass
    return False

#date input condition
while (i==0):
    users = input("Please write the date in format: dd/mm/yy hh:mm:ss  ")
    if validateDate(users):
        print ('Valid Date')
        todays = datetime.strptime(users, '%d/%m/%y %H:%M:%S')
        i=1
    else:
        print ('Invalid Date')

# function to validate the plate's format
def validatePlate(plate):
    if (plate[3:4] != '-' or len(plate)>8):
        return False
    else:
        return True

i=0

#plate input condition
while (i==0):
    users = input("Please write the plate in format: ABC-1234  ")
    if validatePlate(users):
        print ('Valid Plate')
        plates=users
        i=1
    else:
        print ('Invalid Plate')

last_number = int(plates[7:8])   #last digit in plate
if (last_number == 0):
    last_number=10

weekday=todays.weekday()         #day of the week
reference = (weekday + 1)*2
compare=todays

#computing and resulting
import datetime
if ((last_number == reference or last_number == reference - 1) and (weekday < 5) and ((todays.time() >= datetime.time(7,0,0) and todays.time() <= datetime.time(9,30,0)) or (todays.time() >= datetime.time(16,0,0) and todays.time() <= datetime.time(19,30,0)))):
    print(r"""\
   __
 /    \
| STOP |
 \ __ /
   ||
   ||
   ||
   ||
   ||
 ~~~~~~~
 youre not allowed to move inside DMQ
                    """)
else:
    print(r"""\
   __
 /    \
|  GO  |
 \ __ /
   ||
   ||
   ||
   ||
   ||
 ~~~~~~~
 youre allowed to move inside DMQ
                    """)
        
input("Press Enter to continue...")
    

    
