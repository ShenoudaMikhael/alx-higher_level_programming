#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = (10 - (number % 10)) * -1 if number < 0 else number % 10
if last_digit > 5:
    str1 = "and is greater than 5"
elif last_digit != 0 and last_digit < 6:
    str1 = "and is less than 6"
else:
    str1 = "and is 0"


print(f"Last digit of {number} is {last_digit} {str1}")
