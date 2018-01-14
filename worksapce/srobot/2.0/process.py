#coding=utf-8
import ssh

#杀死进程（根据进程id）
def kill_process(client,pid):
	cmd = 'kill -9 ' + pid
	client.exec_command(cmd)
	print 'kill '+pid +' success '

#获取进程id
def handle_processid(client,cmd = 'java'):
	cmd = 'ps aux|grep ' + cmd
	stdin, stdot, stderr = client.exec_command(cmd)
	list = stdot.readlines()

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
			kill_process(client,pid)
	
#启动项目
def start_process(client,env = 'dev'):
	print '开始启动 jar'
	cddir = 'cd /root/srobot/jar/'

	crawler_cmd = cddir + ";" + 'nohup java -jar -Dspring.profiles.active=%s crawler.jar &' % (env)
	manager_cmd = cddir + ";" + 'nohup java -jar -Dspring.profiles.active=%s manager.jar &' % (env)
	web_cmd 	= cddir + ";" + 'nohup java -jar -Dspring.profiles.active=%s web.jar &' % (env)

	client.exec_command(crawler_cmd)
	client.exec_command(manager_cmd)
	client.exec_command(web_cmd)
	print 'jar 启动成功'

#安装jar包(cawler,manager,web)
def update_jar(client,env,crawler_url,manager_url,web_url):
	if crawler_url == None:
		print '爬虫下载地址为空'
		return
	if manager_url == None:
		print '管理端下载地址为空'
		return
	if web_url == None:
		print 'web端下载地址为空'
		return

	# 处理进程(杀死进程)
	handle_processid(client)
	print '开始更新 jar'

	cmds = [
		'cd /root/srobot/jar/',
		'rm -rf *.jar',
		'wget -O crawler.jar ' + crawler_url,
		'wget -O manager.jar ' + manager_url,
		'wget -O web.jar ' + web_url
	]
	cmd = ';'.join(cmds)
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	print 'jar 下载成功'
	#启动项目
	start_process(client,env)


# 更新网页端
def update_html(client,html_url):
	if html_url == None:
		print 'vue 下载地址为空'
		return
	cmds = [
		'cd /home/www/',
		'rm -rf admin*',
		'wget ' + html_url,
		'unzip admin.zip'
	]
	cmd = ';'.join(cmds)
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	print 'html 更新成功'

def start():
	pass

#部署
def main(config = None):
	env 		= config['env']
	crawler_url = config['crawler_url']
	manager_url = config['manager_url']
	web_url 	= config['web_url']
	html_url 	= config['html_url']

	for server in config['server']:
		hostname = server['hostname']
		username = server['username']
		password = server['password']

		client = ssh.get_client(hostname,username,password)
		if client == None:
			continue
		update_html(client,html_url)
		update_jar(client,env,crawler_url,manager_url,web_url)
		ssh.close_client(client)
		print hostname + ' 部署完成'
