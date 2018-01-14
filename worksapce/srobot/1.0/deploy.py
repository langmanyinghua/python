#coding=utf-8;
import os,sys,platform

CONTOS6 = '6'
CONTOS7 = '7'
#获取系统版本
def get_version():
	system = platform.dist()
	if system[1].startswith(CONTOS6):
		version = CONTOS6
	elif system[1].startswith(CONTOS7):
		version = CONTOS7
	else:
		version = CONTOS6
	return version
#设置当前系统版本
version = get_version()

#创建路径
def build_path():
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
def install_wget():
	if os.system('yum -y install wget') == 0:
		print 'wget 安装成功'
	else:
		print 'wget 操作异常'

#安装jdk 8
def install_jdk():
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
def install_mysql():
	#centos6.x 需要安装mysql yum 源
	if version == CONTOS6:
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
def install_init_mysql():
	print '初始化数据 暂时不做任何处理'
	pass

#下载、解压备份shell
def install_mysql_backup():
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
def install_nginx():
	# centos6.x 需要安装nginx yum 源
	if version == CONTOS6:
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
def install_ffmpeg():
	#下载 dag.repo
	if version == CONTOS6:
		cmd = 'wget -P /etc/yum.repos.d http://srobot.oss-cn-hangzhou.aliyuncs.com/deploy/dag.repo';
	elif version == CONTOS7:
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
def install_zip_unzip():
	cmd = 'yum -y install zip unzip'
	res = os.system(cmd)
	if res == 0:
		print 'zip and unzip 安装成功'
	else:
		print 'zip and unzip 安装失败'

#安装文件上传、下载创建
def install_rz_sz():
	cmd = 'yum install -y lrzsz'
	res = os.system(cmd)
	if res == 0:
		print 'rz and sz 安装成功'
	else:
		print 'rz and sz 安装失败'

#初始化
def install():
	build_path()			#创建路径
	install_wget()			#安装wget
	install_jdk()			#安装jdk

	#install_mysql()		#安装mysql
	#install_init_mysql()	#初始化mysql数据库
	#install_mysql_backup()	#添加msyql备份任务

	install_nginx()			#安装nginx

	install_zip_unzip()		#安装zip and unzip
	install_ffmpeg()		#安装FFmpeg
	install_rz_sz()			#安装rz and sz


if __name__ == '__main__':
	#判断身份
	if os.geteuid() != 0:
		print '请以root身份运行脚本'
		sys.exit(1)
	else:
		#初始化数据
		install()
