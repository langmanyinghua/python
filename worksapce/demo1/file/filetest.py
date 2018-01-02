#coding:utf-8;
import csv;
import requests;

# 保存csv文件
def bulidCSV():
	try:
		file = open("/Users/panlaixing/Desktop/python/worksapce/demo1/testfile/one.csv","w+");
		writer = csv.writer(file);
		writer.writerow(('姓名','性别','年龄','生日'));
		for i in xrange(1,10):
			writer.writerow(("潘来星 '%d' "%(i),'男',20,'04-21'));
	except Exception as e:
		print e;
	finally:
		file.close();


def buildTXT():
	txt = requests.get("https://www.ietf.org/rfc/rfc1149.txt");
	content = txt.content;
	with open('/Users/panlaixing/Desktop/python/worksapce/demo1/testfile/test.txt','w+') as file:
		file.write(content);

