'''
\d 可以匹配一个数字
\w 可以匹配一个字母或数字
.  可以匹配任意字符
\s 可以匹配一个空格（也包括Tab等空白符）

* 表示任意个字符（包括0个）
+ 表示至少一个字符
? 表示0个或1个字符
{n} 表示n个字符
{n,m} 表示n-m个字符
'''
import re
test = '132-456'
pat = r'\d{3}\-\d{3}'
if re.match(pat, test):
    print('ok')
else:
    print('failed')

print( re.split(r'\s+','a b  c') )   # 切分字符串
print( re.split(r'[\s,]+','a,b, c  d') )

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')  # 分组
print( m.group(0) )
print( m.group(1) )
print( m.group(2) )
