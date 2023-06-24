for i in range(0,4):
   for j in range(i+1,i+i+1):
     print(" ",end='')
   for j in range(1,4-i+1):
     print(j,end='')
   for j in range(3-i,1-1,-1):
     print(j,end='')  
   print()