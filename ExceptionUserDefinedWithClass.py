class characterhigh(RuntimeError):
   pass
try:
   t=input('Enter a string: ')
   a=len(t)
   if(a>=6):
      print('The size of the String is',a) 
   else:
      raise(characterhigh())
except characterhigh:
   print('String size less than 6')