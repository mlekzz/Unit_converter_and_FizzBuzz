# -*- coding: utf-8 -*-

print "The FizzBuzz game"
x = int(raw_input("Select a number between 1 and 100: "))

for number in range(1, x+1):
    if number % 3 == 0 and number % 5 == 0:
        print "fizzbuzz"
    elif number % 3 == 0:
        print "fizz"
    elif number % 5 == 0:
        print "buzz"
    else:
        print number