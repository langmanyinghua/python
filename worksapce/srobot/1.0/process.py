#coding=utf-8
import os,sys,subprocess

#设置环境
env = 'prod-hg'

# 爬虫端jar url
crawler_url 	= 'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v1/crawler-1.0-SNAPSHOT.jar'
# 客户经理端 jar url
manager_url 	= 'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v1/manager-1.0-SNAPSHOT.jar'
# 管理端 jar url
web_url 		= 'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v1/web-1.0-SNAPSHOT.jar'
# vue url
html_url 		= 'http://srobot.oss-cn-hangzhou.aliyuncs.com/hg/v1/admin.zip'


#杀死进程（根据进程id）
def kill_process(pid):
	cmd = 'kill -9 ' + pid
	res = os.system(cmd)
	if res == 0:
		print ' kill '+pid +' success '

#获取进程id
def handle_processid(cmd = 'java'):
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
			kill_process(pid)

#安装jar包(cawler,manager,web)
def update_jar(crawler_url,manager_url,web_url):
	if crawler_url == None:
		print '爬虫下载地址为空'
		return
	if manager_url == None:
		print '管理端下载地址为空'
		return
	if web_url == None:
		print 'web端下载地址为空'
		return

	#切换工作路径
	path = '/root/srobot/jar/'
	os.chdir(path)

	# 处理进程(杀死进程)
	handle_processid()
	
	# 删除jar文件
	cmd = 'rm -rf *.jar'
	res = os.system(cmd)
	if res == 0:
		print '删除jar 文件成功'

	# 爬虫（crawler）
	# 下载jar
	cmd = 'wget -O crawler.jar ' + crawler_url
	res = os.system(cmd)
	if res == 0:
		print ' crawler下载成功'

	# 客户经理端（manager）
	# 下载jar
	cmd = 'wget -O manager.jar ' + manager_url
	res = os.system(cmd)
	if res == 0:
		print ' manager下载成功'

	# web端（web）
	# 下载jar
	cmd = 'wget -O web.jar ' + web_url
	res = os.system(cmd)
	if res == 0:
		print ' web下载成功'

	#启动项目
	start()


#启动项目
def start():
	path = '/root/srobot/jar/'
	os.chdir(path)

	cmd_crawler = 'nohup java -jar crawler.jar --spring.profiles.active=%s &' % (env)
	subprocess.Popen(cmd_crawler,shell='true')

	cmd_manager = 'nohup java -jar manager.jar --spring.profiles.active=%s &' % (env)
	subprocess.Popen(cmd_manager,shell='true')

	cmd_web = 'nohup java -jar web.jar --spring.profiles.active=%s &' % (env)
	subprocess.Popen(cmd_web,shell='true')
	print '启动成功'


# 更新网页端
def update_html(html_url):
	if html_url == None:
		print 'vue 下载地址为空'
		return

	#切换工作路径
	path = '/home/www/'
	os.chdir(path)

	#删除
	cmd = 'rm -rf admin*'
	res = os.system(cmd)
	if res == 0:
		print '删除html 文件成功'

	#下载
	cmd = 'wget ' + html_url
	res = os.system(cmd)
	if res == 0:
		print '下载成功'

	#解压
	cmd = 'unzip admin.zip'
	res = os.system(cmd)
	if res == 0:
		print 'html 解压成功'

#入口
def main():
	#更新html
	update_html(html_url)
	#更新jar
	update_jar(crawler_url,manager_url,web_url)

if __name__ == '__main__':
	#判断身份
	if os.geteuid() != 0:
		print '请以root身份运行脚本'
		sys.exit(1)
	else:
		main()

