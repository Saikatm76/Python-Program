n1=int(input("Enter a Limit "))
print("Amstrong Number:")
for i in range (1,n1+1):
    p=0
    sp=i
    while sp!=0:
      t=sp%10
      sp=sp//10
      p=p+(t*t*t)
    if p==i:
      print(i," ",end=" ")