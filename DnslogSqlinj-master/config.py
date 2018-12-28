#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DNSlog 设置
APItoken = 'you_api'
DNSurl = 'you_addr'

# 超时时间
timeout = 30

# 多线程线程数
# thread_count = 10

# 识别规则列表
patternClose = ['',"'","')",'"','")']
patternLink = ['and', 'or', 'like', '=', '<', '>', 'regexp']

# 是否允许URL重定向
allow_redirects = True

# 是否允许随机User-Agent
allow_random_useragent = False

# 是否允许随机X-Forwarded-For
allow_random_x_forward = False




USER_AGENTS = [
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
	"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
	"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
	"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
	"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
	"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
	"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
	"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
	"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
	"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
	"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
	"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
	"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# 随机生成User-Agent
def random_useragent(condition=False):
	if condition:
		return random.choice(USER_AGENTS)
	else:
		return USER_AGENTS[0]

# 随机X-Forwarded-For，动态IP
def random_x_forwarded_for(condition=False):
	if condition:
		return '%d.%d.%d.%d' % (random.randint(1, 254),random.randint(1, 254),random.randint(1, 254),random.randint(1, 254))
	else:
		return '8.8.8.8'

# HTTP 头设置
headers = {
	'User-Agent': random_useragent(allow_random_useragent),
	'X_FORWARDED_FOR': random_x_forwarded_for(allow_random_x_forward),
	'Referer' : 'http://www.baidu.com',
	'Cookie': "",
}

def banner():
	"""
	@DnsLog SqlInj banner
	"""
	str = """_______________________________________________________________
	 _____            _                   _____       _ 
	|  __ \          | |                 |_   _|     (_)
	| |  | |_ __  ___| |     ___   __ _    | |  _ __  _ 
	| |  | | '_ \/ __| |    / _ \ / _` |   | | | '_ \| |
	| |__| | | | \__ \ |___| (_) | (_| |  _| |_| | | | |
	|_____/|_| |_|___/______\___/ \__, | |_____|_| |_| |
	                               __/ |            _/ |
	                              |___/            |__/ 

	DnsLog SqlInj Scanner by ADO
	Version 1.0
	https://github.com/ADOOO/DnslogSqlinj
_______________________________________________________________
	"""
	print (str)



