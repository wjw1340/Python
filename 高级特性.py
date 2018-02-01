
# 切片 (同Matlab)
a = list( range(100) )
print(a[:10:2])

for i in a[1:10:1]:
    print(i)
	
# 迭代
d = {'a': 1, 'b': 2, 'c': 3}         #dict
for key in d:                        #key
	print(key)                    
for val in d.values():               #val
	print(val)
for key,val in d.items():            #同时迭代key 和 val
	print('d[%s] = %d'%(key,val))
	
for i,val in enumerate(a[2:14:3]):   #自动加下标
	print(i,val)
	
# 列表生成式
a = [x * x for x in range(1, 11) if x%2 == 0]
print(a)

b = [n+m for n in 'XYZ' for m in '123']
print(b)

# 生成器
g = (x * x for x in range(1, 11) if x%2 == 0)   #把列表生成式的[]改成()
print(next(g))
print(next(g))
for x in g:
    print(x)

def odd():                 #每次到yield结束(return),下次从上一个yield开始
    print('step 1')
    yield
    print('step 2')
    yield
    print('step 3')
    yield
o = odd()
next(o)
next(o)
next(o)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib(6):
    print(n)
