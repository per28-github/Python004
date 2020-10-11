#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import requests
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent' : ua.random,
'Referer' : 'https://processon.com/login?f=index'
}

s = requests.Session()
# 会话对象：在同一个 Session 实例发出的所有请求之间保持 cookie， 
# 期间使用 urllib3 的 connection pooling 功能。
# 向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。
login_url = 'https://processon.com/login'
form_data = {
'login_email':'1377068752-------------',
'login_password':'qa--------',
}

r = s.post(login_url, data=form_data, headers=headers)
t= r.text
return_text = r.json
status_code=r.status_code
print(status_code)
print(return_text)
print(t)