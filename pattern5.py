for i in range(0,5):
  for j in range(4-i,0,-1):
    print(" ",end='')
  for j in range(i+1,0,-1):
    print(j,end='')
  for j in range(2,i+1+1):
    print(j,end='')
  print()