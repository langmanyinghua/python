#coding=utf-8
import os,sys,subprocess
import thread

#杀死进程（根据进程id）
def killprocess(pid):
	cmd = 'kill -9 ' + pid
	res = os.system(cmd)
	if res == 0:
		print ' kill '+pid +' success '

#获取进程id
def handleProcessid(cmd = 'java'):
	cmd = 'ps aux|grep ' + cmd
	list = os.popen(cmd).readlines()
	index = 10
	for line in list:
		#根据空格分割字符串
		line = line.split()
		if len(line) > index:
			cmds = ''
			while len(line) > index:
				if cmds == '':
					cmds = line.pop(index)#移除最后一个元素
				else:
					cmds = cmds +  ' ' + line.pop(index)
			line.append(cmds)

		cmd = line[len(line)-1]
		if 	cmd.startswith('java -jar manager') or \
			cmd.startswith('java -jar crawler') or \
			cmd.startswith('java -jar web'):
			pid = line[1]
			killprocess(pid)

def start():
	path = '/root/srobot/jar/'
	os.chdir(path)

	subprocess.Popen('nohup java -jar crawler.jar &',shell='true')
	subprocess.Popen('nohup java -jar manager.jar &',shell='true')
	subprocess.Popen('nohup java -jar web.jar &',shell='true')
	sys.exit(1)
	print '启动成功'

#安装jar包(cawler,manager,web)
def updateJar(	crawlerurl = 'http://srobot.oss-cn-hangzhou.aliyuncs.com/dev/crawler-1.0-SNAPSHOT.jar',
				managerurl = 'http://srobot.oss-cn-hangzhou.aliyuncs.com/dev/manager-1.0-SNAPSHOT.jar',
				weburl = 'http://srobot.oss-cn-hangzhou.aliyuncs.com/dev/web-1.0-SNAPSHOT.jar'):
	path = '/root/srobot/jar/'
	os.chdir(path)

	# 处理进程(杀死进程)
	handleProcessid()
	
	# 删除jar文件
	cmd = 'rm -rf *.jar'
	res = os.system(cmd)
	if res == 0:
		print '删除jar 文件成功'

	# 爬虫（crawler）
	# 下载jar
	cmd = 'wget -O crawler.jar ' + crawlerurl
	res = os.system(cmd)
	if res == 0:
		print ' crawler下载成功'

	# 客户经理端（manager）
	# 下载jar
	cmd = 'wget -O manager.jar ' + managerurl
	res = os.system(cmd)
	if res == 0:
		print ' manager下载成功'

	# 客户经理端（web）
	# 下载jar
	cmd = 'wget -O web.jar ' + weburl
	res = os.system(cmd)
	if res == 0:
		print ' web下载成功'

	#启动项目
	start()


# 更新网页端
def updateHtml(url = 'http://srobot.oss-cn-hangzhou.aliyuncs.com/dev/admin.zip'):
	#删除
	cmd = 'rm -rf /home/www/admin*'
	res = os.system(cmd)
	if res == 0:
		print '删除html 文件成功'

	#下载
	cmd = 'wget -P /home/www/ ' + url
	res = os.system(cmd)
	if res == 0:
		print '下载成功'

	#解压
	cmd = 'unzip -xd /home/www/ /home/www/admin.zip'
	res = os.system(cmd)
	if res == 0:
		print 'html 解压成功'

#入口
def main():
	#更新jar
	updateJar(
		crawlerurl = 'http://srobot.oss-cn-hangzhou.aliyuncs.com/show/crawler-1.0-SNAPSHOT.jar',
		managerurl = 'http://srobot.oss-cn-hangzhou.aliyuncs.com/show/manager-1.0-SNAPSHOT.jar',
		weburl = 'http://srobot.oss-cn-hangzhou.aliyuncs.com/show/web-1.0-SNAPSHOT.jar'
	)
	#更新html
	updateHtml()		

if __name__ == '__main__':
	#判断身份
	if os.geteuid() != 0:
		print '请以root身份运行脚本'
		sys.exit(1)
	else:
		main()

