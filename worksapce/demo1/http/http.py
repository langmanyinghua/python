#coding: UTF-8
import urllib;
import urllib2;
import json;
from bs4 import BeautifulSoup as bs;
from urllib import urlretrieve;

#获取html
def getHtml(url):
 	header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
        , "Connection": "keep-alive"
        , "Referer": "http://www.wantu.cn/"
        ,"Accept":"application/json, text/plain, */*"
    }
    req = urllib2.Request(url, headers = header)
    html = urllib2.urlopen(req);
	result = html.read();
	return result;

#解析json
def getJson():
	try:
		html = urllib.urlopen("http://192.168.31.158:8080/test/index.json");
		jsonObject = html.read();
		print jsonObject;
		dic = json.loads(jsonObject);
		print dic['name'];

		list = dic['links'];
		print list;

		address = dic['address'];
		print address['city'];
	except Exception as e:
		print e;

#getJson();

def encodeHtml(url):
	html = getHtml(url);
	#print dir(BeautifulSoup)
	document = bs(html,'html.parser');
	print dir(document.title)
	print document.title.get_text();
	print document.html.head.title;

	#print document.body;

#encodeHtml("http://www.baidu.com");

#下载文件
def downloadFile():
	url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1513782011916&di=37eef2a72f3c6da71d05920d66d7668b&imgtype=0&src=http%3A%2F%2Fh.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2F203fb80e7bec54e749ead8f7b3389b504ec26ad1.jpg';
	#下载文件
	urlretrieve(url,'download/one.jpg');

#downloadFile();

def getGreenHtml():
	result = getHtml("https://www.zhihu.com/question/28197450");
	html = bs(result,'html.parser');
	greenlist = html.findAll("h1",{'class':'QuestionHeader-title'});
	for item in greenlist:
		print item.text;


#getGreenHtml();

def getGrilImage():
	html = getHtml("https://www.toutiao.com/a6501814743685136909");
	html = bs(html,"html.parser");
	print html;
	images = html.findAll('li',{'class':'image-item'});
	print images;
	for image in images:
		print image;
		img  = image('img');
		print img;

getGrilImage();
