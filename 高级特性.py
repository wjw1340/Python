# 切片 (同Matlab)
a = list( range(100) )
print(a[:10:2])

for i in a[1:10:1]:
    print(i)
	
# 迭代
d = {'a': 1, 'b': 2, 'c': 3}      #dict
for key in d:                     #key
	print(key)                    #val
for val in d.values():
	print(val)
for key,val in d.items():
	print('d[%s] = %d'%(key,val))
