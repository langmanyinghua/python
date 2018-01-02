#! -*- coding:UTF-8 -*-
import httputils as http;
import json;

#测试更新
def testUpdate():
	url = 'http://192.168.31.86:8082/manager/assist/update';
	result = http.post(url);
	return result

print testUpdate();

#测试登录
def testLogin():
	url = "http://192.168.31.86:8082/manager/account/login";
	parameter = {
		'username':'admin',
		'password':'123456'
	};
	return http.post(url,parameter = parameter);

print testLogin();

def getInfo():
	result = testLogin();
	token = json.loads(result)['result'];
	if token == '':
		print '登录失败';
		return '';
	url = 'http://192.168.31.86:8082/manager/account/me';
	headers = {
		'token': token
	}
	return http.post(url,headers = headers);

print getInfo();
