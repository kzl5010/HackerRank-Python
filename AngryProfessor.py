#! /bin/python

t = int(input())
for i in range(t):
  a = map(int, input().split())
  b = map(int, input().split())
  d = len([e for e in c if e <= 0])
  if d < a[1]: 
    print("YES")
  else: 
    print("NO")
