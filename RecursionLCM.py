def recursion(n1,n2,n3,i=1):
    if i%n1==0 and i%n2==0 and i%n3==0:
           return i
    else:
           return recursion(n1,n2,n3,i+1)
a=int(input('Enter 1st Number: '))
b=int(input('Enter 2nd Number: '))
c=int(input('Enter 3rd Number: '))
s=recursion(a,b,c)
print('LCM of %d, %d & %d is %d'%(a,b,c,s))