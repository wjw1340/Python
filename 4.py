# 切片 (同Matlab)
a = list( range(100) )
print(a[:10:2])

for i in a[1:10:1]:
    print(i)

def trim(s):
    st = i = 0
    for x in s:
        if x != ' ':
            st = i
            break
        i += 1
    en = j = len(s)
    for x in s[-1:0:-1]:
        if x != ' ':
            en = j
            break
        j -= 1
    if (st==0) and (en==len(s)):
        return ''
    else:
        return s[st:en]

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')
	
L = ['Hello', 'World', 18, 'Apple', None]
L2 =[s.lower() for s in L if isinstance(s, str)] 

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

def tr():
   a = [1]
   while 1:
       yield a
       a = [ a[i]+a[i+1] for i in range(len(a)-1) ]
       a.append(1)
       a.insert(0,1)

n = 1
for x in tr():
    print(x)
    n += 1
    if n == 10:
        break

