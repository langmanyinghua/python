#coding: utf-8
import json,sys;
import demjson;
import mysql;

reload(sys)  
sys.setdefaultencoding('utf-8')   

def dicWriteToFile():
	dictObj = {  
	    'andy':{  
	        'age': 23,  
	        'city': '上海',  
	        'skill': 'python'  
	    },  
	    'william': {  
	        'age': 33,  
	        'city': '广州',  
	        'skill': 'js'  
	    }  
	}
	result = json.dumps(dictObj,ensure_ascii=False);#不使用ascii 码
	try:
		file = open("/Users/panlaixing/Desktop/python/worksapce/demo1/testfile/one.txt","w+");
		file.write(result)
	except Exception as e:
		print e;
	finally:
		file.close();

dicWriteToFile();