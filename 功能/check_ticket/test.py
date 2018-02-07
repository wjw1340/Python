print('%s%s' % ('asd'.ljust(10),'ert'.ljust(10)))
try:
        a = 123 / 0
        print('asd')
except:
	print('sdf')

while 1:
    from_s = input('从:')
    to_s = input('去:')
    flag = input('结束(Y/N):')
    if flag == 'Y':
	    break
