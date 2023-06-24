s=input('Enter any value: ')
c1=0
c2=0
c3=0
for i in range(0,len(s)):
    if s[i].isalpha():
        c1=c1+1
    elif s[i].isdigit():
        c2=c2+1
    elif s[i].isspace():
        c3=c3+1
print('The no. of Alphabets',c1)
print('The no. of Digits',c2)
print('The no. of Spaces',c3)