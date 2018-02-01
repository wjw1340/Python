def myabs(x):
    if not isinstance(x, (int, float)):      #检查形参的类型
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x;
    

import math                                  #导入math库的函数(头文件)
def move(x, y, step, angle=0):               #angle = 0,angle要是不传入,默认为0
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

def power(x,n = 2):
    sum = 1
    while(n):
        sum *= x
        n -= 1
    return sum

def pr(name,gender,age = 6,city = 'Jiaxin'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

pr('wjw1340','M',age = 22)    #改变某个默认参数，别的不变

def cal(*numbers):            #参数数量可变    
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
a = [1,2,3]
print( cal(*a) )

def person(name, age, **kw):  #可以传入含参数名的参数
    print('name:', name, 'age:', age, 'other:', kw)
person('Bob', 35) 
person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

def product(*x):
    sum = 1;
    for i in x:
        sum *= i
    return sum

def move(n,A,B,C):
    if(n == 0):return
    move(n-1,A,C,B)
    print('%s -> %s' %(A,C))
    move(n-1,B,A,C)
