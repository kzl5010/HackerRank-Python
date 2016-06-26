t = int(input())
for i in range(t):
    u = int(input())
    if u == 0:
        print ("1")
    else:
        n = 1
        for e in range(u):
            if e % 2 ==0:
                n *= 2
            if e % 2 == 1:
                n += 1    
        print (n)
