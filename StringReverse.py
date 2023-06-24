str=input('Enter a String: ')
strlen=len(str)
st=''
for i in range(strlen-1,0-1,-1):
     st=st+str[i]
print(st)
