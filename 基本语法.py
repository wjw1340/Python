# I/O
age = input('please your age:'); #input()返回的数据类型是str
print('your age is %s' % age)
age = int(age);
print('your age is %d' % age)
print('Pi is %.2f or %.6f' % (3.1415926,3.145926) )
print( 'Hello, {0}, 成绩提升 {1:.1f}%'.format('小明', 17.125) )

# 数组
a = [1,2,3]
print(a[0])
print(a[-1])
a.append(5)                  #末尾加5
a.insert(0,9)                #0位置加9，其余后退
a.pop()                      #末尾删
a.pop(0)                     #0位置删
b = ['wjw1340',22,'WUST']    #数组内元素类型可以不同

c = (1,2)            #tuple,,里面内容不能改变，除非以下
e = (1,2,[3,4])
e[2][0] = 5

# 判断
if age >= 18:
	print('adult\n')
elif age >= 6:
	print('teenege\n')
else:
	print('kid\n')

# 循环  内含(while break continue)
names = ['Michael', 'Bob', 'Tracy']
for name in names:        #直接取值，没有下标 从头开始取两个数in name[0:2]
    print('hello',name)


# dict (类似 map)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Peter'] = 99
print(d['Bob'])
d.pop('Bob')
if 'Thomas' in d:                   #key是否存在
    print('good')
print(d.get('Thomas' ) )            #不存在,返回None;不然,返回value
print(d.get('Thomas', 'Baaaaad') )  #自定义不存在的返回值


# set
s = set([1, 2, 3])
s.add(4)
s.remove(2)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
