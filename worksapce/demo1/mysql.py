#coding:utf-8
import MySQLdb;
import json;
import sys;
# 设置字符编码
reload(sys)  
sys.setdefaultencoding('utf8');

#获取链接
def getConn():
	conn = MySQLdb.connect("192.168.31.86",'root','root','srobot',charset="utf8");
	return conn;

#保存数据
def save():
	conn = getConn();
	#获取游标
	cursor = conn.cursor();
	try:
		sql = "insert into t_lable(level,name,remark,type) values('%d','%s','%s','%s')"%\
		(1,'python','牛逼的语言','SERVER');
		cursor.execute(sql);
		conn.commit();
	except Exception as e:
		print ' error ',e.message;
	finally:
		cursor.close();					#关闭游标
		conn.close();					#关闭连接

#查询数据
def find():
	conn = getConn();			#获取连接
	cursor = conn.cursor();		#获取游标
	response = [];
	try:
		sql = "select * from t_lable";	#定义sql 语句
		cursor.execute(sql)		#执行sql 语句
		result = cursor.fetchall();		#获取到数据
		for item in result:
			dic = {};
			dic['id'] = item[0];
			dic['level'] = item[2];
			dic['name'] = item[3];
			dic['parentid'] = item[4];
			dic['remark'] = item[5];
			dic['type'] = item[6];
			response.append(dic);
	except Exception as e:
		print " error: ",e.message;
	finally:
		cursor.close();			#关闭游标
		conn.close();			#关闭连接
	return response;

#写入文件
def writeToFile():
	result = find();
	resultJson = json.dumps(result,ensure_ascii=False);
	try:
		file = open("/Users/panlaixing/Desktop/python/worksapce/demo1/one.txt","w+");
		file.write(resultJson);
	except Exception as e:
		print e.message;
	finally:
		file.close();

def update():
	conn = getConn();
	cursor = conn.cursor();
	try:
		sql = "update t_lable set parentid = '%d' where id = '%d'"%(1,277);
		cursor.execute(sql);
		conn.commit();
	except Exception as e:
		print e.message;
	finally:
		cursor.close();
		conn.close();

#update();

def remove(id):
	conn = getConn();
	cursor = conn.cursor();
	try:
		sql = "delete from t_lable where id = '%d'"%(id);
		cursor.execute(sql);
		conn.commit();
	except Exception as e:
		print e.message;
	finally:
		cursor.close();
		conn.close();

#remove('2102010210');
