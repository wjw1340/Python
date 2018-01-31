#name = input('please input your name:')
#print('hello',name)

print('1024 * 768 =',1024*768)

a = -100
if a >= 0:
	a = a;
else:
	a = -a;
print(a)
print('I\'m OK')

print('1\n2\n3');

print('''line1
line2
line3''')

print('\\\tasd')
print(r'\\\tasd')

#ord('吴')
#chr(66)

len('wjw1340')
print('hello,%s'%'wjw1340')

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))

s1 = 72
s2 = 85
print('up %.2lf %%' % (100*(s2-s1)/s1))
print('up',
      100*(s2-s1)/s1)

a = [1,2,3]
print(a[0])
print(a[-1])
print(a)
a.append(5)
print(a)
a.pop(0)
a.pop()
a.insert(0,9)
print(a)

b = ['wjw1340',22,'WUST'] #数组

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])

c = (1,2) #tuple,,里面内容不能改变，除非以下
d = (1,2,[3,4])
d[2][0] = 5

