age = 3
if age >= 18:
    print('your age is', age)
    print('adult')

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print('hello',name)

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Peter'] = 99
print(d['Bob'])
if 'Thomas' in d:
    print('good')
else:
    print('bad')
print(d.get('Thomas' ) )
print(d.get('Thomas', 'Baaaaad') )

d.pop('Bob')

s = set([1, 2, 3])
s.add(4)
s.remove(2)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)

r ={}
r['a']=1,2,3
r['b']=1,[2,3]
print(r)


	
