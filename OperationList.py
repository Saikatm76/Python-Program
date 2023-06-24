l1=[1,'two',3.3,'four',6]
l2=[2,3,1,5,'s',{'u':6},['g',7],('t',8)]
l3=[['a',1],['b',3],['c',4],]
print(l1)
print(l2)
print(l3,'\n')

l4=[i for i in range(0,10)]
l5=list(range(0,10))           #just print
print(l4)
print(l5,'\n')

l6='Hi,Hello'
l7=l6.split(',')       #split
print(l7,'\n')

l8='saikat'
l9=list(l8)          #string to list
print(l9,'\n')

l10=12345
l11=[int(i) for i in str(l10)]      #integer to list
print(l11,'\n')

mdict={'a':1,'b':2,'c':3}
print(mdict)
print(list(mdict.keys()))          #dictionary keys to list
print(list(mdict.values()),'\n')     #dictionary values to list

l12=[1,'two',3.3,'four',6]
print(l12)
l12.append('five')    #append
print(l12,'\n')

l13=[1,'two',3.3,'four',6]
l14=[7,8,'nine']
print(l13)
print(l14)
l13.extend(l14)    #extend
print(l13,'\n')

l15=[1,'two',3.3,'four',6]
print(l15)
l15.insert(2,'nine')     #insert
print(l15,'\n')

l16=[1,'two',3.3,'four',6]
print(l16)
l16.remove(3.3)     #remove
print(l16,'\n')

l16=[1,'two',3.3,'four',6]
print(l16)
l16.pop()
print(l16)
l17=l16.pop(1)     #pop
print(l17)
print(l16,'\n')

l18=[1,4,10,5,6,2]
print(l18)
l18.sort()
print(l18)
l18.sort(reverse=True)       #sort
print(l18,'\n')

l19=[1,4,10,5,6,2]
print(l19)
l19.reverse()            #reverse
print(l19,'\n')

l20=[1,4,10,5,6,2]
print(l20)                #length
print(len(l20),'\n')

l21=[1,4,10,5,6,2]
print(l21)
print(min(l21))
print(max(l21),'\n')            #MinMax   

l22=['a','a','b','c','a']
print(l22)
print(l22.count('a'),'\n')          #count


l23=['a','a','b','c','a']
print(l23)
l23.clear()
print(l23,'\n')                      #clear

l24=['a','a','b','c','a']
print(l24)
if 'a' in l24:
   print('exist','\n')                    #membership

l25=[1,2,3,4,5]
print(l25)
print(l25[2],l25[-1],'\n')               #indexing

l25=[1,2,3,4,5]
print(l25)
print(l25[0:3])
print(l25[::-1])                 #slicing
print(l25[:3])
print(l25[3:],'\n')


l25=[1,2,3,4,5]
print(l25)
l26=l25
print(l26,'\n')               #copy












