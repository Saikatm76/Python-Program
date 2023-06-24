c=0;
for i in range(1,5+1):
  if i%2==1:
   c=c+i
   for j in range(1,i+1):
    print(c," ",end='')
    c=c+1
  else:
   c=c+i-1
   for j in range(1,i+1):
    print(c," ",end='')
    c=c-1 
  print()
     