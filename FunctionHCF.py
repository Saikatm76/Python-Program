def functionhcf(n1,n2):
   while n1!=n2:
     if n1>n2:
         n1=n1-n2
     else:
         n2=n2-n1
   print('HCF: ',n1)
   return
a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))
functionhcf(a,b)