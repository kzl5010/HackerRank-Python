#!/bin/python3

N, T = map(int, input().split())
widths = list(map(int, input().split()))
for x in range(T): 
    i, j = map(int, input().split())
    vehicle = min(widths[segment] for segment in range(i, j+1))
    print(vehicle)
