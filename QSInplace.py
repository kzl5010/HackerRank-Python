def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        print (*A)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)
    return A

def partition(A, lo, hi):
    pivot = A[hi]
    i = lo
    for j  in range(lo, hi):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[hi] = A[hi], A[i]
    return i

n = int(input())
Arr = [int(x) for x in input().split()]
quicksort(Arr, 0, len(Arr)-1)
