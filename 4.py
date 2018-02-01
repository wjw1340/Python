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


