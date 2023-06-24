for i in range(0,4):
    for j in range(0,3-i):
        print(" ",end='')
    for j in range(1,i+1+1):
        print(j,end='')
    for j in range(i,1-1,-1):
        print(j,end='')
    print()
for k in range(0,3):
    for l in range(0,k+1):
        print(" ",end='')
    for l in range(1,4-k):
        print(l,end='')
    for l in range(2-k,1-1,-1):
        print(l,end='')
    print()