#!/usr/bin/python3
for i in range(0, 10):
    for x in range(1, 10):
        if i >= x:
            continue
        if i == 8 and x == 9:
            print("{:d}{:d}".format(i, x))
        else:
            print("{:d}{:d}".format(i, x), end=", ")
