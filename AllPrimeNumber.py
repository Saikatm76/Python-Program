n1=int(input("Enter a Limit "))
print("Prime Numbers between 1 & %d"%n1)
for i in range(1,n1+1):
    c=0
    for j in range(1,i+1):
      if i%j==0:
       c=c+1
    if c==2:
     print((i)," ",end='')  