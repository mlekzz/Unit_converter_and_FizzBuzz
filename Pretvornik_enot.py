# -*- coding: utf-8 -*-

print "Hello this is km to mile converter"

while True:
    km = int(raw_input("Enter Km: "))
    convertion = 0.621371
    miles = km * convertion
    print "The distance in miles is:",miles

    more = raw_input("Another conversion (y/n):".lower())
    if more == "n":
        break

print "end"