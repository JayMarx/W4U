#-*-coding: utf-8 -*-

import time 
import sys 
import urllib2
import json
from weibo import Client
from config import cfg 

reload(sys)
sys.setdefaultencoding('utf-8')

app_key = cfg.api_key 
app_secret = cfg.api_secret
callback_url = cfg.callback_url 
usr_id = cfg.usr_id 
passwd = cfg.password
city = cfg.city 
safe_link = cfg.safe_link 

debug = 0

def checkweather(city_code):
    site = cfg.api_url + str(city_code)
    webinfo = urllib2.urlopen(site)

    content = webinfo.read()
    data = json.loads(content)

    return data 

if __name__ == '__main__':
    
    count = 0
    flag = 0
    while(1):
        data = checkweather(city['上海'])
        count += 1                   # 计数，若尝试20次仍然失败则退出
        if data['status'] == 200:    # 判断是否成功返回数据
            break 
        else:
            if count == 20:
                flag = -1            # 达到请求次数上限，退出
                break
            else:
                time.sleep(20)
    if flag == -1:
        print 'Error: get weather data failed!'
        exit(-1)

    if debug: print data
    
    date = data['date']
    humidity = data['data']['shidu']
    pm25 = data['data']['pm25']
    quality =  data['data']['quality']
    forecast = data['data']['forecast']
    
    # 以此类推
    today = forecast[0]
    tomorrow = forecast[1]
    
    today_type = today['type']
    today_high = today['high']
    today_low = today['low']
    today_notice = today['notice']
    
    if debug: print today_type, today_high, today_low, today_notice

    weather = '{:s}\nhumidity {:s}   pm2.5 {:s}   quality {:s}\n{:s}   {:s}   {:s}\n{:s}\n'.format(date, humidity, str(pm25), quality, today_type, today_high, today_low, today_notice)
    # add safe link
    text_info = weather + safe_link

    # login
    client = Client(app_key, app_secret, callback_url, username = usr_id, password = passwd)

    client.post('statuses/share', status = text_info)
    #pic = open('./pic/totoro.png')
    #client.post('statuses/share', status = 'Test!\n' + safe_link, pic = pic)
