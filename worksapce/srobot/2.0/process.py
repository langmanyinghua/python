#coding=utf-8
import ssh

#杀死进程（根据进程id）
def kill_process(client,pid):
	cmd = 'kill -9 ' + pid
	client.exec_command(cmd)
	print 'kill '+pid +' success '

#获取进程id
def handle_processid(client,cmdprocess = 'java -jar'):
	cmd = 'ps aux|grep java'
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
		if cmd.startswith(cmdprocess):
			pid = line[1]
			kill_process(client,pid)


#安装jar包(cawler,manager,web)
def update_jar(client,env,crawler_url,manager_url,web_url):
	cmds = [
		'cd /root/srobot/jar/'
	]
	print '开始更新 jar'

	UPDATE_CRAWLER = False 
	UPDATE_MANAGER = False
	UPDATE_WEB 	   = False
	if crawler_url != None and crawler_url != '':
		UPDATE_CRAWLER = True
		handle_processid(client,'java -jar crawler')	#杀死robot端
		cmds.append('rm -rf crawler.jar')
		cmds.append('wget -O crawler.jar '+ crawler_url)
		
	if manager_url != None and manager_url != '':
		UPDATE_MANAGER = True
		handle_processid(client,'java -jar manager')	#杀死客户经理端
		cmds.append('rm -rf manager.jar')
		cmds.append('wget -O manager.jar '+ manager_url)
		
	if web_url != None and web_url != '':
		UPDATE_WEB = True
		handle_processid(client,'java -jar web')		#杀死后台管理系统端
		cmds.append('rm -rf web.jar')
		cmds.append('wget -O web.jar '+ web_url)

	if UPDATE_CRAWLER == False and UPDATE_MANAGER == False and UPDATE_WEB == False:
		print '不需要更新'
		return
	
	cmd = ';'.join(cmds)
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	print 'jar 下载成功'
	#启动项目
	start_process(client,env,UPDATE_CRAWLER,UPDATE_MANAGER,UPDATE_WEB)

#启动项目
def start_process(client,env = 'dev',UPDATE_CRAWLER = False,UPDATE_MANAGER = False,UPDATE_WEB = False):
	print '开始启动 jar'
	cddir = 'cd /root/srobot/jar/'

	if UPDATE_CRAWLER:
		crawler_cmd = cddir + ";" + 'nohup java -jar -Dspring.profiles.active=%s crawler.jar &' % (env)
		client.exec_command(crawler_cmd)

	if UPDATE_MANAGER:
		manager_cmd = cddir + ";" + 'nohup java -jar -Dspring.profiles.active=%s manager.jar &' % (env)
		client.exec_command(manager_cmd)

	if UPDATE_WEB:
		web_cmd 	= cddir + ";" + 'nohup java -jar -Dspring.profiles.active=%s web.jar &' % (env)
		client.exec_command(web_cmd)	
	print 'jar 启动成功'


# 更新网页端
def update_html(client,html_url):
	if html_url == None or html_url == '':
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
