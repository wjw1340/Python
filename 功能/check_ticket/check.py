import requests
import json
from prettytable import PrettyTable
from stations import ma
requests.packages.urllib3.disable_warnings()

def query(day,from_s,to_s):
    url = ('https://kyfw.12306.cn/otn/leftTicket/queryZ?'
           'leftTicketDTO.train_date={}&'
           'leftTicketDTO.from_station={}&'
           'leftTicketDTO.to_station={}&'
           'purpose_codes=ADULT').format(day,from_s,to_s)
    #print(url)
    head = {
    'Host': 'kyfw.12306.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
    'Connection': 'keep-alive'
    }
    r = requests.get(url, verify=False, headers = head)
    try:
        res = r.json()['data']['result']
        table = PrettyTable(['车次', '出发站', '目的地', '出发时间', '到达时间', '消耗时间','一等座','二等座', '软卧', '硬卧', '硬座', '无座'])
        for raw_train in res:
            data_list = raw_train.split('|')
            train_no = data_list[3]
            from_station_code = data_list[6]
            from_station_name = mma[from_station_code]
            to_station_code = data_list[7]
            to_station_name = mma[to_station_code]
            start_time = data_list[8]
            arrive_time = data_list[9]
            time_fucked_up = data_list[10]
            first_class_seat = data_list[31] or '--'
            second_class_seat = data_list[30]or '--'
            soft_sleep = data_list[23]or '--'
            hard_sleep = data_list[28]or '--'
            hard_seat = data_list[29]or '--'
            no_seat = data_list[26]or '--'
            table.add_row([train_no, from_station_name, to_station_name, start_time, arrive_time, time_fucked_up,first_class_seat,second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat])
        print(table)
    except:
	    print('输入有误!')
		


mma = { v:k for k,v in ma.items() }
while True:
    '''
    day = input('输入日期(2018-02-12):')
    from_s = input('从:')
    to_s = input('去:')
    query(day,ma[from_s],ma[to_s])
    '''
    day = '2018-03-01'
    from_s = '上海虹桥'
    to_s = '武昌'
    query(day,ma[from_s],ma[to_s])
    flag = input('结束?(Y/N):')
    if flag == 'Y':
        break

