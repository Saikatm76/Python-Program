n1=int(input("Enter a Limit: "))
a=0
b=1
print("Fibonacci Series:")
for i in range(n1):
    if i<=1:
        print(i,'',end='') 
    else:
        s=a+b
        print(s,'',end='')
        a=b
        b=s