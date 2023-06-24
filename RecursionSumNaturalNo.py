def recursion(n):
    if n==0:
       return 0
    else:
       return n + recursion(n-1)
a=int(input('Enter a Limit: '))
s=recursion(a)
print('Sum of %d natural number is %d'%(a,s))