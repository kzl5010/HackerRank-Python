def partition(ar):
    a = []
    b = []
    c = []
    for x in range (1, len(ar)):
        if ar[0] < ar[x]:
            a.append(ar[x])
        if ar[0] >= ar[x]:
            b.append(ar[x])
    b.append(ar[0])
    c = b + a
    for i in c:
        print(i, end = " ")
m = input()
ar = [int(i) for i in input().strip().split()]
partition(ar)
