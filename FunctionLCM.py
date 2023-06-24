def functionlcm(n1,n2,n3):
    i=1
    while True:
      if i%n1==0 and i%n2==0 and i%n3==0:
         print('LCM of %d , %d and %d is %d'%(n1,n2,n3,i))
         break
      else:
         i=i+1
a=int(input('Enter 1st Number '))
b=int(input('Enter 2nd Number '))
c=int(input('Enter 3rd Number '))
functionlcm(a,b,c)