n1=int(input("Enter a Number: "))
p=n1
print("Factors of %d "%n1)
for i in range(1,p+1):
  if (p%i)==0:
   print(i)