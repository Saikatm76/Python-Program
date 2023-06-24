def recursion(n1):
   if n1==0:
      return 1
   else:
      return n1 * recursion(n1-1)
a=int(input('Enter a Number '))
p=recursion(a)
print('Factorial of %d is %d'%(a,p))