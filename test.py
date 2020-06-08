import os
from time import sleep as delay

class tcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

os.system('title Verifying prime numbers... ')

clear = lambda : os.system('cls')
clear()
print(tcolors.WARNING + 'Please enter a number to verify. ' + tcolors.END)
try :
    num = int(input(tcolors.OKBLUE))
    print(tcolors.END)
except :
    print(tcolors.END)

if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(tcolors.FAIL + str(num) + " is not a prime number")
           div = num//i
           print(i,"times",str(div),"is",str(num) + tcolors.END)
           break
   else:
       print(tcolors.OKGREEN + str(num),"is a prime number" + tcolors.END)
