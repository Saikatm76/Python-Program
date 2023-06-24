for i in range(0,5):
    if (i%2)==0:
      for j in range(0,i+1):
         print("1",end='')
    else:
      for j in range(0,i+1):
         print("0",end='')
    print()