n=int(input("Enter the First Limit: "))
n1=int(input("Enter the Last Limit: "))
print("Palindrome number between %d to %d"%(n,n1))
for i in range (n,n1+1):
      q=0
      sp=i
      while sp!=0:
       t=sp%10
       sp=sp//10
       q=q*10
       q=q+t
      if q==i:
       print(i," ",end='') 