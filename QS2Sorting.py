def partition(ar):
    a = []
    b = []
    c = []
    for x in range (1, len(ar)):
        if ar[0] < ar[x]:
            a.append(ar[x])
        elif ar[0] >= ar[x]:
            b.append(ar[x])
    if len(b) > 1:
        b = partition(b)
        print (*b)
    if len(a) > 1:
        a = partition(a)
        print (*a)
    b.append(ar[0])
    c = b + a
    return c

m = input()
ar = [int(i) for i in input().split()]
d = partition(ar)
for y in d:
    print (y, end = ' ')
