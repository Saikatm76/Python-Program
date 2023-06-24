n1=int(input('Enter a Limit:'))
print('Perfect Numbers:')
for i in range(1,n1+1):
   temp=i
   sum=0
   for j in range(1,i):
       if i%j==0:
          sum=sum+j
   if sum==temp:
       print(temp,'',end='')
   
