#coding=utf-8
import paramiko

#获取 ssh 的连接
def get_client():
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(hostname = '192.168.31.101',username = 'root',password = '123456')
	return client

#执行ssh 连接指令
def execs():
	client = get_client()
	stdin, stdot, stderr = client.exec_command('pwd')
	result = stdot.read();
	client.close()

execs()