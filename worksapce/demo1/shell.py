#coding=utf-8;
import os,sys

# 判断是否是root用户
if os.geteuid() != 0 :	
	print '当前用户不是root，请以root的身份运行脚本'
	sys.exit(1)

#输入版本号
version = raw_input('请输入要安装的pytohn版本 2.7/3.6') 
if version == '2.7':
	url = 'https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz'
	package_name = 'Python-2.7.13'
elif version == '3.6':
	url = 'https://www.python.org/ftp/python/3.6.4/Python-3.6.4.tgz'
	package_name = 'Python-3.6.4'
else:
	print '您输入的版本号有误，请输入 2.7/3.6'
	sys.exit(1)

#下载python
cmd = 'wget '+url
res = os.system(cmd)
if res != 0:
	print '下载python 失败，请检查网络,然后重新运行脚本'
	sys.exit(1)

#解压python
cmd = 'tar -zvxf '+package_name+'.tgz'
res = os.system(cmd)
if res != 0 :
	os.system('rm -rf '+package_name+'.tgz')
	print '解压源码包失败，请重新下载'
	sys.exit(1)

#安装python
cmd  = 'cd '+package_name +" && ./configure --prefix=/usr/local/python && make && make install"
res = os.system(cmd)
if res != 0 :
	print '编译安装失败，请检查依赖库'
	sys.exit(1)

print '安装 python' + version + '成功'



