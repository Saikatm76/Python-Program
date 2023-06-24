str=input('Enter a String: ')
c1=0
c2=0
for i in str:
    if(i.isupper()):
        c1=c1+1
    if(i.islower()):
        c2=c2+1
print('The number of uppercase Character',c1)
print('The number of lowercase Character',c2)