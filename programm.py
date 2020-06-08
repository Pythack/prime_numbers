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

os.system('title Calculating prime numbers... ')

clear = lambda : os.system('cls')
clear()
print(tcolors.WARNING + 'Importation of the numbers... ' + tcolors.END)
list = open('list.txt', 'r').read()
list = list.split('\n')
last_tested = int(open('last.txt', 'r').read())
num = last_tested + 1
new = []
clear()
print(tcolors.WARNING + 'Starting... ' + tcolors.END)
delay(0.3)
clear()
try :
    primes_number = 0
    num = last_tested + 1
    if last_tested == 1 :
        print('2')
        print('3')
    last_found = list[-1]
    while True :
        prime = 1
        print('Actually testing : ' + tcolors.OKBLUE + str(num) + tcolors.END)
        print('Last prime number found : ' + tcolors.OKBLUE + str(last_found) + tcolors.END)
        difference = int(num) - int(last_found)
        print('Difference : ' + tcolors.OKBLUE + str(difference) + tcolors.END)
        for i in list :
            i = int(i)
            if (num % i) == 0:
                prime = 0
                break
        if prime == 1:
            list.append(str(num))
            new.append(str(num))
            last_found = num
            primes_number += 1
        last = num
        num += 1
        clear()
except KeyboardInterrupt :
    print(tcolors.WARNING + 'Saving in progress, please don\'t interrupt... ' + tcolors.END)
    open('last.txt', 'w').write(str(last))
    upload = '\n'
    for i in new :
        if not i == new[-1] :
            upload = upload + i + '\n'
            continue
        upload = upload + i
    open('list.txt', 'a').write(upload)
    clear()
    print(tcolors.OKGREEN + 'Successfully saved to list.txt' + tcolors.END)
    delay(1)
    clear()
    print('')
    print(tcolors.OKBLUE + str(primes_number) + ' prime numbers have been generated. ' + tcolors.END)
    print('')
    print(tcolors.OKBLUE + 'The last prime number generated is ' + str(new[-1]) + '. ' + tcolors.END)
    print('')
    print(tcolors.OKGREEN + 'See you! ;)' + tcolors.END)
