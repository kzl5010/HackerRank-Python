#!/bin/python3


for i in range(int(input())):
    b = int(input())
    print (len([i for i in map(int, list(str(b))) if i != 0 and b % i == 0]))
