def recursion(n1,n2):
    if n1==n2:
       return n1
    elif n1>n2:
       n1=n1-n2
       return recursion(n1,n2)
    else:
       n2=n2-n1
       return recursion(n1,n2)
a=int(input('Enter 1st Value: '))
b=int(input('Enter 2nd Value: '))
s=recursion(a,b)
print('GCD:',s)