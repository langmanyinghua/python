#!coding=utf-8;
import urllib,urllib2;

#发送get请求
def get(url,headers = {}):
	request = urllib2.Request(url,headers = headers);
	result = urllib2.urlopen(request).read();
	return result;

#发送post请求
def post(url,headers = {},parameter = {}):
	request = urllib2.Request(url,urllib.urlencode(parameter),headers);
	result = urllib2.urlopen(request).read();
	return result;

