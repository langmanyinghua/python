#coding=utf-8
import ssh

CONTOS6 = '6'
CONTOS7 = '7'

#获取系统版本
def get_version(client):
	stdin, stdot, stderr = client.exec_command('uname -r')
	result = stdot.read()
	if result.startswith('2.6'):
		return CONTOS6
	elif result.startswith('3.10'):
		return CONTOS7
	else:
		return CONTOS6

#安装wget
def install_wget(client):
	print '开始安装 wget'
	stdin, stdot, stderr = client.exec_command('yum -y install wget')
	print stdot.read()
	if len(stderr.read()) <= 0:
		print 'wget 安装成功'

#创建路径
def build_path(client):
	print '开始创建路径'
	cmd = 'mkdir -p /root/srobot/jar'
	client.exec_command(cmd)

	cmd = 'mkdir -p /home/www'
	client.exec_command(cmd)
	print ' 目录创建成功'

#安装jdk 8
def install_jdk(client):
	print '开始安装 jdk'
	#有些时候jdk 的名字可能不一样，所有安装好jdk 后需要检查确认
	jdkname = 'java-1.8.0-openjdk-devel.x86_64'
	#jdkname = 'java-1.8.0-openjdk-devel-debug.x86_64'

	cmd  = 'yum -y install '+jdkname
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	if len(stderr.read()) <= 0:
		print 'jdk 安装成功'
	else:
		print 'jdk 安装失败'

#安装Nginx
def install_nginx(client,version = CONTOS6):
	print '开始安装 nginx'
	# centos6.x 需要安装nginx yum 源
	if version == CONTOS6:
		cmd = 'yum -y install http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm'
		stdin, stdot, stderr = client.exec_command(cmd)
		print stdot.read()
		if len(stderr.read()) <= 0:
			print 'ngixn yum源 安装成功'
		else:
			print 'ngixn yum源 安装失败'

	#安装nginx
	cmd = 'yum -y install nginx.x86_64'
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	print 'ngixn 安装成功'

	#替换配置文件nginx.conf
	cmd = 'rm -rf /etc/nginx/nginx.conf'
	client.exec_command(cmd)

	cmd = 'wget -P /etc/nginx http://srobot.oss-cn-hangzhou.aliyuncs.com/deploy/nginx.conf'
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()

	cmd = 'nginx'
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()

	cmd = 'chkconfig nginx on'
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()


#安装FFmpeg
#centos7 
def install_ffmpeg(client,version = CONTOS6):
	print '开始安装 ffmpeg'
	#下载 dag.repo
	if version == CONTOS6:
		cmd = 'wget -P /etc/yum.repos.d http://srobot.oss-cn-hangzhou.aliyuncs.com/deploy/dag.repo';
	elif version == CONTOS7:
		cmd = 'rpm -Uvh http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-1.el7.nux.noarch.rpm'
	else:
		pass

	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	if len(stderr.read()) <= 0:
		print 'FFmpeg yum源安装失败'
		return
	#安装 ffmpeg
	cmd = 'yum -y install ffmpeg.x86_64'
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	if len(stderr.read()) <= 0:
		print 'ffmpeg 安装成功'
	else:
		print 'ffmpeg 安装失败'

	cmd = 'wget -P /root/srobot http://srobot.oss-cn-hangzhou.aliyuncs.com/deploy/converter.gz'
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	if len(stderr.read()) <= 0:
		print '请检查converter.gz的下载地址和下载后保存的路径(/root/srobot)是否创建成功'
		return

	cmd = 'tar -zvxf /root/srobot/converter.gz -C /root/srobot'
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	if len(stderr.read()) <= 0:
		print '解压成功'
		#删除文件
		cmd = 'rm -rf /root/srobot/converter.gz'
		client.exec_command(cmd)
	else:
		print '解压失败'

#安装zip和unzip
def install_zip_unzip(client):
	print '开始安装 zip and unzip'
	cmd = 'yum -y install zip unzip'
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	print stderr.read();
	if len(stderr.read()) <= 0:
		print 'zip and unzip 安装成功'
	else:
		print 'zip and unzip 安装失败'

#安装文件上传、下载创建
def install_rz_sz(client):
	print '开始安装 rz and sz'
	cmd = 'yum install -y lrzsz'
	stdin, stdot, stderr = client.exec_command(cmd)
	print stdot.read()
	if len(stderr.read()) <= 0:
		print 'rz and sz 安装成功'
	else:
		print 'rz and sz 安装失败'

#启动
def main(config = None):
	list = config['server']
	for server in list:
		hostname = server['hostname']
		username = server['username']
		password = server['password']

		client = ssh.get_client(hostname, username, password)
		if client == None:
			continue
		#设置当前系统版本
		version = get_version(client)

		install_wget(client)
		build_path(client)
		install_jdk(client)
		install_nginx(client,version)
		install_ffmpeg(client,version)
		install_rz_sz(client)
		install_zip_unzip(client)

		ssh.close_client(client)
		print hostname + ' 初始化环境完成 '
