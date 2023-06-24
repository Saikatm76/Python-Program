lst=list()
limit=int(input('Enter the number you want to insert: '))
for i in range(0,limit):
    no=int(input('Enter the Number: '))
    lst.append(no)
print('The Max Number is',max(lst))
print('The Min Number is',min(lst))