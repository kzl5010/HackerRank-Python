def insertionSort(ar):
    key = 0
    i = 0
    for j in range(1, len(ar)):
        for i in range(j):
            if ar[j] < ar[i]:
                key = ar[j]
                ar[j] = ar[i]
                ar[i] = key
        for x in ar:
            print (x, end = ' ')
        print()




m = input()
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)
