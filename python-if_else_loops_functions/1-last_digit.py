#!/usr/bin/python3
import random
#number = random.randint(-10000, 10000)
number = 60
ld = abs(number) % 10
if ld == 0:
    print("Last digit of", number, "is", ld, "and is 0")
elif number < 0:
    ld = -ld
    print("Last digit of", number, "is", ld, "and is less than 6 and not 0")
elif number > 0 and ld > 5:
    print("Last digit of", number, "is", ld, "and is greater than 5")
else:
    print("Last digit of", number, "is", ld, "and is less than 6 and not 0")
