#-*-coding: utf-8-*-

from easydict import  EasyDict as edict 

__C = edict()

cfg = __C 

# for weibo
__C.api_key = 'xxx'     # api key
__C.api_secret = 'xxx'  # api secret
__C.callback_url = 'https://api.weibo.com/oauth2/default.html'  # 回调url
__C.usr_id = 'xxx'      # 微博账号
__C.password = 'xxx'    # 微博密码
__C.safe_link = 'xxx'   # 微博安全链接

__C.city = {
    '上海': 101020100,
    '闵行区': 101020200,
    '北京': 101010100,
    '宜昌': 101200901}

__C.api_url = 'http://t.weather.sojson.com/api/weather/city/'
