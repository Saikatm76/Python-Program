class A1:
   def ab1(self):
      print('This is A1')
class A2:
   def ab2(self):
      print('This is A2')
class A3(A1,A2):
   def ab3(self):
      A1.ab1(self)
      A2.ab2(self)
      print('This is A3')
s=A3()
s.ab3()