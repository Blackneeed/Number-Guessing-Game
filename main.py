import napi
import sys
from colored import cprint
import colorama
import random
colorama.init()

cprint('Welcome to the number guessing game,', 'blue', end=' ')
cprint('Press any key to continue!', 'red')
napi.pause()
napi.clear("cmd")
cprint('Enter how far the numbers can go:', end=" ")
try:
    howhard = int(input())
except:
    cprint("Enter an integer", 'red')
    napi.pause()
    sys.exit()
napi.clear("cmd")
cprint('Enter a number:', 'red')
number = random.randint(1, howhard)
tries = 0
while True:
    try:
        n = int(input())
    except:
        cprint("Enter an integer", 'red')
        napi.pause()
        sys.exit()
    if n==number:
        napi.clear('cmd')
        cprint("You won!", "red")
        cprint("Tries:" + str(tries), "red")
        napi.pause()
        break
    if n>number:
        cprint("Lower", "blue")
        tries+=1
    if n<number:
        cprint("Higher", "blue")
        tries+=1