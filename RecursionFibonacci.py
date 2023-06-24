def recursion(n1,n2,l):
   s=n1+n2
   print(s)
   if l == 0:
      return 0
   else:
      return recursion(n2,s,l-1)
a=int(input('Enter a Limit: '))
p=0
t=1
print('Fibonacci Series: ')
print(p)
print(t)
t=recursion(p,t,a-3)
