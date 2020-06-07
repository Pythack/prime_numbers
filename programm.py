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

os.system('title Calcul des nombres premiers... ')

clear = lambda : os.system('cls')
clear()
print(tcolors.WARNING + 'Importation des nombres... ' + tcolors.END)
list = open('list.txt', 'r').read()
list = list.split('\n')
last_tested = int(open('last.txt', 'r').read())
num = last_tested + 1
new = []
clear()
print(tcolors.WARNING + 'Démarage des calculs... ' + tcolors.END)
delay(0.3)
clear()
try :
    primes_number = 0
    num = last_tested + 1
    if last_tested == 1 :
        print('2')
        print('3')
    while True :
        prime = 1
        for i in list :
            i = int(i)
            if (num % i) == 0:
                prime = 0
                break
        if prime == 1:
            list.append(str(num))
            new.append(str(num))
            print(tcolors.OKBLUE + str(num) + tcolors.END)
            primes_number += 1
        last = num
        num += 1
except KeyboardInterrupt :
    print(tcolors.WARNING + 'Sauvegarde en cours... ' + tcolors.END)
    open('last.txt', 'w').write(str(last))
    upload = '\n'
    for i in new :
        if not i == new[-1] :
            upload = upload + i + '\n'
            continue
        upload = upload + i
    open('list.txt', 'a').write(upload)
    clear()
    print(tcolors.WARNING + 'Valeurs sauvegardées!' + tcolors.END)
    delay(1)
    clear()
    print('')
    print(tcolors.OKBLUE + str(primes_number) + ' nombres premiers ont été générés. ' + tcolors.END)
    print('')
    print(tcolors.OKBLUE + 'Le dernier nombre premier généré est ' + str(last) + tcolors.END)
    print('')
    print(tcolors.OKGREEN + 'A bientôt! ;)' + tcolors.END)
