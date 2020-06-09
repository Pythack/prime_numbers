import os
import sys
try :
    from plyer import notification
except :
    os.system('pip install plyer')
    from plyer import notification
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
tested = 0
try :
    primes_number = 0
    num = last_tested + 1
    if last_tested == 1 :
        print('2')
        print('3')
    last_found = list[-1]
    while True :
        prime = 1
        difference = int(num) - int(last_found)
        print('Actually testing : ' + tcolors.OKBLUE + str(num) + tcolors.END)
        print('Last prime number found : ' + tcolors.OKBLUE + str(last_found) + tcolors.END)
        print('Difference : ' + tcolors.OKBLUE + str(difference) + tcolors.END)
        print('Count of tested numbers for now : ' + tcolors.OKBLUE + str(tested) + tcolors.END)
        print('Count of prime numbers found for now : ' + tcolors.OKBLUE + str(primes_number) + tcolors.END)
        print('Count of prime numbers found in total : ' + tcolors.OKBLUE + str(len(list)) + tcolors.END)
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
        tested += 1
        clear()
        if num == 1000000000 :
            notification.notify(title='Prime numbers calculator', message='We have reached the billion !!!', app_icon=None, timeout=3200)
except KeyboardInterrupt :
    print(tcolors.WARNING + 'Saving in progress, please don\'t interrupt... ' + tcolors.END)
    open('last.txt', 'w').write(str(last))
    upload = '\n'
    if not primes_number == 0 :
        for i in new :
            if not i == new[-1] :
                upload = upload + i + '\n'
                continue
            upload = upload + i
        open('list.txt', 'a').write(upload)
    clear()
    print(tcolors.OKGREEN + 'Successfully saved to list.txt' + tcolors.END)
    notification.notify(title='Prime numbers calculator', message='Results successfully saved to list.txt', app_icon=None, timeout=5)
    delay(1)
    clear()
    print('')
    if primes_number <= 1 :
        print(tcolors.OKBLUE + tcolors.UNDERLINE + str(primes_number) + tcolors.END + ' prime number have been generated. ')
    else :
        print(tcolors.OKBLUE + tcolors.UNDERLINE + str(primes_number) + tcolors.END + ' prime numbers have been generated. ')
    print('')
    print(tcolors.OKBLUE + tcolors.UNDERLINE + str(len(list)) + tcolors.END + ' prime numbers have been generated in total. ')
    print('')
    if not primes_number == 0 :
        print('The last prime number generated is ' + tcolors.OKBLUE + tcolors.UNDERLINE + str(new[-1]) + tcolors.END + '. ')
        print('')
    print(tcolors.OKBLUE + tcolors.UNDERLINE + str(tested) + tcolors.END + ' tested numbers. ')
    print('')
    print(tcolors.OKGREEN + 'See you! ;)' + tcolors.END)
    print('')
#    print(tcolors.WARNING + 'Do you want to close the window ? (Press y for \'yes\' and n for \'no\'. )' + tcolors.END)
#    while True :
#        if keyboard.is_pressed('y') :
#            clear()
#            print('')
#            if primes_number <= 1 :
#                print(tcolors.OKBLUE + tcolors.UNDERLINE + str(primes_number) + tcolors.END + ' prime number have been generated. ')
#            else :
#                print(tcolors.OKBLUE + tcolors.UNDERLINE + str(primes_number) + tcolors.END + ' prime numbers have been generated. ')
#            print('')
#            print(tcolors.OKBLUE + tcolors.UNDERLINE + str(len(list)) + tcolors.END + ' prime numbers have been generated in total. ')
#            print('')
#            if not primes_number == 0 :
#                print('The last prime number generated is ' + tcolors.OKBLUE + tcolors.UNDERLINE + str(new[-1]) + tcolors.END + '. ')
#                print('')
#            print(tcolors.OKBLUE + tcolors.UNDERLINE + str(tested) + tcolors.END + ' tested numbers. ')
#            print('')
#            print(tcolors.OKGREEN + 'See you! ;)' + tcolors.END)
#            delay(3)
#            self.exit()
#        elif keyboard.is_pressed('n') :
#            clear()
#            print('')
#            if primes_number <= 1 :
#                print(tcolors.OKBLUE + tcolors.UNDERLINE + str(primes_number) + tcolors.END + ' prime number have been generated. ')
#            else :
#                print(tcolors.OKBLUE + tcolors.UNDERLINE + str(primes_number) + tcolors.END + ' prime numbers have been generated. ')
#            print('')
#            print(tcolors.OKBLUE + tcolors.UNDERLINE + str(len(list)) + tcolors.END + ' prime numbers have been generated in total. ')
#            print('')
#            if not primes_number == 0 :
#                print('The last prime number generated is ' + tcolors.OKBLUE + tcolors.UNDERLINE + str(new[-1]) + tcolors.END + '. ')
#                print('')
#            print(tcolors.OKBLUE + tcolors.UNDERLINE + str(tested) + tcolors.END + ' tested numbers. ')
#            print('')
#            print(tcolors.OKGREEN + 'See you! ;)' + tcolors.END)
#            exit()
