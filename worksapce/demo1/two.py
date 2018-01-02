#coding=utf-8;
import random;
import requests;

#获取随机时间
def getRandomSleepTime():
	return random.randint(3,10);

#获取html数据
def getHtml(index = 1):
	if index >= 0:
		return '参数异常';
	url = 'http://www.budejie.com/video/'+str(index);
	return requests.get(url).content;

#解析html数据
def analysisHtml(html = ''):
	if html == '' or html == "" or html == '''''' or html == None :
		return html;


#print getHtml(0);
a = -1;
if a > 0:
	print 'ok';
elif a < 0:
	print 'no';
else:
	print '0';

s = 'Hello World'

print s.startswith('h')
