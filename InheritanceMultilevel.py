class person:
     def fill_details1(self,a,b):
       self.a=a
       self.b=b
class student(person):
     def fill_details2(self,a,b,c):
       person.fill_details1(self,a,b)
       self.c=c
class teacher(student):
     def fill_details3(self,a,b,c,d):
       student.fill_details2(self,a,b,c)
       self.d=d
     def display(self):
       t=self.a+self.b+self.c+self.d
       print(t)
p1=teacher()
p1.fill_details3(4,1,2,3)
p1.display()