for i in range(0,4):
  for j in range(0,2-i+1):
     print(" ",end='')
  for j in range(9,9-i-1,-1):
     print(j,end='')
  for j in range(10-i,9+1):
     print(j,end='')
  print()