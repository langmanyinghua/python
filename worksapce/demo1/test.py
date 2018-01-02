#!coding=utf-8;
import urllib,urllib2;

#发送post请求
def post(url,headers = {},parameter = {}):
	request = urllib2.Request(url,urllib.urlencode(parameter),headers);
	result = urllib2.urlopen(request).read();
	return result;

#测试更新
def testUpdate():
	url = 'http://118.178.95.100:8082/manager/assist/update';
	result = post(url);
	return result

print testUpdate()