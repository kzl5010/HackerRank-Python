a = [0] * 100
input()
b = [int(x) for x in input().split()]
for i in b:
  a[i] += 1
for x in range(100):
  for y in range(a[x]):
      print (x, end = ' ')
  
