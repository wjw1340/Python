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

pr('wjw1340','M',age = 22)           #改变某个默认参数，别的不变
