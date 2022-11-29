#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_num = int(repr(number)[-1])


if last_num == 0:
    state = "and is 0"
elif last_num > 5:
    state = "and is greater than 5"
else:
    state = "and is less than 6 and not 0"

if number < 0:
    last_num = -last_num

print("Last digit of", number, "is", last_num, state)
