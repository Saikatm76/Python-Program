def recursion(n,p=0):
    if n==0:
       return p
    else:
       s=n%10
       n=n//10
       p=p*10+s
       return recursion(n,p)
a=int(input('Enter a Number: '))
f=recursion(a)
print('Reverse Of the Number is:',f)