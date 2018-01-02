#coding=utf-8;
import os,sys,platform

#创建路径
def buildPath():
	cmd = 'mkdir -p /root/srobot/jar'
	res = os.system(cmd)
	if res == 0:
		print '目录创建成功'
	else:
		print '目录创建失败'

	cmd = 'mkdir -p /home/www/admin'
	res = os.system(cmd)
	if res == 0:
		print '目录创建成功'
	else:
		print '目录创建失败'

#安装wget
def installWget():
	if os.system('yum -y install wget') == 0:
		print 'wget 安装成功'
	else:
		print 'wget 操作异常'

#安装jdk 8
def installJdk():
	#有些时候jdk 的名字可能不一样，所有安装好jdk 后需要检查确认
	#jdkname = 'java-1.8.0-openjdk-devel.x86_64'
	jdkname = 'java-1.8.0-openjdk-devel-debug.x86_64'
	cmd  = 'yum -y install '+jdkname
	res  = os.system(cmd)
	if res == 0:
		print 'jdk 安装成功'
	else:
		print 'jdk 安装失败'

#安装mysql数据库
def installMysql():
	#安装mysql yum 源
	cmd = 'rpm -Uvh http://repo.mysql.com/mysql-community-release-el6-5.noarch.rpm'
	res = os.system(cmd)
	if res == 0:
		print 'mysql yum源 安装成功'
	else:
		print 'mysql yum源 安装失败'

	#安装数据库
	cmd = 'yum -y install mysql-community-server.x86_64'
	res = os.system(cmd)
	if res == 0:
		print 'mysql 安装成功'

		#替换配置文件
		cmd = 'rm -rf /etc/my.cnf'
		res = os.system(cmd)

		cmd = 'wget -P /etc http://srobot.oss-cn-hangzhou.aliyuncs.com/deploy/my.cnf'
		res = os.system(cmd)
		if res == 0:
			print '替换成功'
			#启动mysql 
			if os.system('service mysqld start') == 0:
				print 'msyql 启动成功'
			else:
				print 'msyql 启动失败'

		# 开机启动
		cmd = 'chkconfig mysqld on'
		res = os.system(cmd)
		if res == 0:
			print 'mysql 开机启动成功'
		else:
			print 'mysql 开机启动失败'
	
	else:
		print 'mysql 安装失败'

	
#添加初始化数据(暂时不做处理)
def installInitMysql():
	print '初始化数据 暂时不做任何处理'
	pass

#下载、解压备份shell
def installMysqlBackup():
	cmd = 'wget -P /home/www/ http://srobot.oss-cn-hangzhou.aliyuncs.com/deploy/backup.gz'
	res = os.system(cmd)
	if res != 0:
		print 'backup.gz的下载地址和下载后保存的路径(/home/www/)是否创建成功'
		return
	cmd = 'tar -zvxf /home/www/backup.gz -C /home/www/'
	res = os.system(cmd)
	if res == 0:
		print '解压成功'
		#删除文件
		cmd = 'rm -rf /home/www/backup.gz'
		os.system(cmd)
	else:
		print '解压失败'

	#添加备份
	cmd = "echo '0 8 * * * /home/backup/srobot_backup.sh' >> /var/spool/cron/root"
	res = os.system(cmd)
	if res == 0:
		print '定时备份设置成功'
	else:
		print '定时备份设置失败'

	#备份开机启动
	cmd = 'chkconfig --level 35 crond on'
	res = os.system(cmd)
	if res == 0:
		print '定时备份开机启动设置成功'
	else:
		print '定时备份开机启动设置失败'

#安装Nginx
def installNginx():
	#安装nginx yum 源
	cmd = 'yum -y install http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm'
	res = os.system(cmd)
	if res == 0:
		print 'ngixn yum源 安装成功'
	else:
		print 'ngixn yum源 安装失败'

	#安装数据库
	cmd = 'yum -y install nginx.x86_64'
	res = os.system(cmd)
	if res == 0:
		print 'ngixn 安装成功'

		#替换配置文件nginx.conf
		cmd = 'rm -rf /etc/nginx/nginx.conf'
		res = os.system(cmd)

		cmd = 'wget -P /etc/nginx http://srobot.oss-cn-hangzhou.aliyuncs.com/deploy/nginx.conf'
		res = os.system(cmd)
		if res == 0:
			print '替换成功'
			#启动nginx
			if os.system('nginx') == 0:
				print 'nginx 启动成功'
			else:
				print 'nginx 启动失败'

		# 开机启动
		cmd = 'chkconfig nginx on'
		res = os.system(cmd)
		if res == 0:
			print 'nginx 开机启动成功'
		else:
			print 'nginx 开机启动失败'
	else:
		print 'ngixn 安装失败'

#安装FFmpeg
#centos7 
def installFFmpeg():
	#下载 dag.repo
	system = platform.dist()
	cmd = ''
	if system[1].startswith('6.'):
		cmd = 'wget -P /etc/yum.repos.d http://srobot.oss-cn-hangzhou.aliyuncs.com/deploy/dag.repo';
	elif system[1].startswith('7.'):
		cmd = 'rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm'
	else:
		pass
	res = os.system(cmd)
	if res != 0:
		print 'FFmpeg yum源安装失败'
		return
	#安装 ffmpeg
	cmd = 'yum -y install ffmpeg.x86_64'
	res = os.system(cmd)
	if res == 0:
		print 'ffmpeg 安装成功'
	else:
		print 'ffmpeg 安装失败'

	cmd = 'wget -P /root/srobot http://srobot.oss-cn-hangzhou.aliyuncs.com/deploy/converter.gz'
	res = os.system(cmd)
	if res != 0:
		print '请检查converter.gz的下载地址和下载后保存的路径(/root/srobot)是否创建成功'
		return
	cmd = 'tar -zvxf /root/srobot/converter.gz -C /root/srobot'
	res = os.system(cmd)
	if res == 0:
		print '解压成功'
		#删除文件
		cmd = 'rm -rf /root/srobot/converter.gz'
		os.system(cmd)
	else:
		print '解压失败'

#安装zip和unzip
def installZipAndUnzip():
	cmd = 'yum -y install zip unzip'
	res = os.system(cmd)
	if res == 0:
		print 'zip and unzip 安装成功'
	else:
		print 'zip and unzip 安装失败'

#安装文件上传、下载创建
def installRzAndSz():
	cmd = 'yum install -y lrzsz'
	res = os.system(cmd)
	if res == 0:
		print 'rz and sz 安装成功'
	else:
		print 'rz and sz 安装失败'

#初始化
def install():
	buildPath()				#创建路径
	installWget()			#安装wget
	installJdk()			#安装jdk

	installMysql()			#安装mysql
	installInitMysql()		#初始化mysql数据库
	installMysqlBackup()	#添加msyql备份任务

	installNginx()			#安装nginx

	installZipAndUnzip()	#安装zip and unzip
	installFFmpeg()			#安装FFmpeg
	installRzAndSz()		#安装rz and sz


if __name__ == '__main__':
	#判断身份
	if os.geteuid() != 0:
		print '请以root身份运行脚本'
		sys.exit(1)
	else:
		#初始化数据
		install()
