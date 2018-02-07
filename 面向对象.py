class student(object):

    def __init__(self,name,sc):
        self.name = name
        self.sc = sc
    def print_s(self):
        print('%s %s' % (self.name,self.sc))

no1 = student('Peter',96)
print( no1.name )
no1.print_s()

class stu(object):

    def __init__(self,name,sc): #变量名前加两个下划线,就无法从外部调用aa.__name
        self.__name = name
        self.__sc = sc
    def print_s(self):
        print('%s %s' % (self.__name,self.__sc))
aa = stu('wjw',95)
print( aa._stu__name )          #但是可以这样访问

class animal(object):
    def go(self):
        print('anumal go')
    def run(self):
        print('anumal run')

class dog(animal):
    def run(self):
        print('dog run')

d = dog()
print( d.go() )     #继承animal的函数
print( d.run() )    #run名字相同，子类的覆盖父类
