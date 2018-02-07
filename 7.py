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

PAT = r'[a-zA-Z.]*@[a-zA-Z]*.com'
def is_valid_email(addr):
    if re.match(PAT,addr):
        return 1
    else:
        return 0

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

pa = r'<?([a-zA-Z\s]*)>?\s?[a-zA-Z]*@[a-zA-Z]*.[a-zA-Z]*'
def name_of_email(addr):
    m = re.match(pa,addr)
    print( m.group(1) )
    return m.group(1)
    

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue().decode('utf-8'))


