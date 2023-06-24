class triangle:
    def create_triangle(self,a,b,c):
          self.a=a
          self.b=b
          self.c=c
          print('Triangle is created')
    def print_sides(self):
          print('side a=',self.a)
          print('side b=',self.b)
          print('side c=',self.c)
t1=triangle()
t1.create_triangle(5,6,7)
def size_double(obj):
     t2=triangle()
     t2.a=t1.a*2
     t2.b=t1.b*2
     t2.c=t1.c*2
     return t2
t3=size_double(t1)
t3.print_sides()