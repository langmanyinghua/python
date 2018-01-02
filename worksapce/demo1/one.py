# -*- coding: UTF-8 -*-
import MySQLdb;

def testOne():
	count = 9;
	while count > 0:
		count -= 1;
		print count;
	else:
		print 'over';

def testTwo():
	list1 = ['11',20,30.5,True]
	dic = {'name':'潘来星','age':10}

	print list1[0];
	print list1;
	for item in list1:
		print item;

	print dic;
	print dic['age']

	print len(list1);
	print len(dic);


#testTwo();

def getConn():
	conn = MySQLdb.connect("192.168.31.86",'root','root','srobot');
	return conn;

def select():
	conn = getConn();
	cursor = conn.cursor();
	cursor.execute("SELECT VERSION()");
	data = cursor.fetchone();
	print data;

#select();
print 10;


