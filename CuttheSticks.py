n = int(input())
arr = list(map(int, input().split()))
while len(arr) > 0:
    print (len(arr))
    arr = [x for x in arr if x - min(arr) > 0]
