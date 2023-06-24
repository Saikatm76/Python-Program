n1=int(input("Enter 1st value: "))
n2=int(input("Enter 2nd value: "))
n3=int(input("Enter 3rd value: "))
s=n1
p=n2
q=n3
i=1
while True:
 if i%n1==0 and i%n2==0 and i%n3==0:
    print("GCD of %d & %d & %d is %d"%(n1,n2,n3,i))
    break
 else:
    i=i+1