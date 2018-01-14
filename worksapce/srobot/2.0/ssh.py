#coding=utf-8
import paramiko

#获取 ssh 的连接
def get_client(hostname, username, password):
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		client.connect(hostname = hostname,username = username,password = password)
	except Exception as e:
		client = None
		print '连接异常 hostname = %s username = %s password = %s'%(hostname,username,password)  
	return client

#关闭 ssh 连接
def close_client(client):
	client.close()