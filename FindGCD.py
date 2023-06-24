n1=int(input("Enter 1st value: "))
n2=int(input("Enter 2nd value: "))
s=n1
p=n2
while(n1!=n2):
  if(n1>n2):
    n1=n1-n2
  else:
    n2=n2-n1
print("GCD of %d & %d is %d"%(s,p,n1))