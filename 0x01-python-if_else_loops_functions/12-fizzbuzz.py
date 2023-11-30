#!/usr/bin/python3
for x in range(1, 101):
    if x == 100:
        print("Buzz")
    else:
        if x % 3 == 0:
            print("Fizz ", end="")
        elif x % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(x), end="")
