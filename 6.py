'''
import requests
r = requests.get('http://202.114.242.231:8036/default.html')
print( r.encoding)
'''


from urllib import request

with request.urlopen('http://202.114.242.231:8036/default.html') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('ISO-8859-1'))
