#! /bin/python

t = int(input())
for a0 in range(t):
    n = list(map(int, input().split()))
    k = map(int, input().split())
    d = len([e for e in k if e <= 0])
    if d < n[1]: 
        print("YES")
    else: 
        print("NO")
