import requests
import re

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9047'
r = requests.get(url,verify=False)
pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
result = re.findall(pattern,r.text)
station = dict(result)
print(station)
