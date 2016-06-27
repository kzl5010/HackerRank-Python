from math import floor, sqrt, ceil

for x in range(int(input())): 
    b, c = map(int, input().split())
    print (int(floor(sqrt(c))-ceil(sqrt(b))+1))
